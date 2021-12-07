# -*- coding: utf-8 -*-
#
# Copyright 2017-2021 - Swiss Data Science Center (SDSC)
# A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
# Eidgenössische Technische Hochschule Zürich (ETHZ).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""cwltool based provider.

This implementation provides a plugin for executing workflows using ``cwltool``,
by simply exporting the workflow into a CWL format and then using ``cwltool``
to run the exported CWL file.

.. code-block:: console

   $ renku workflow execute --provider cwltool example_workflow


.. topic:: Specifying custom parameters for cwltool (``--config``)

   You can specify custom configuration parameters for ``cwltool`` executer
   by providing a YAML file for the ``--config`` option. The YAML file
   should contain both the ``LoadingContext`` and ``RuntimeContext`` key-value
   pairs.

.. code-block:: console

   $ renku workflow execute --config config.yaml --provider cwltool example_workflow
"""

import os
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict
from urllib.parse import unquote
from uuid import uuid4

import cwltool.factory
import networkx as nx
from cwltool.context import LoadingContext, RuntimeContext

from renku.core.commands.echo import progressbar
from renku.core.errors import WorkflowExecuteError
from renku.core.models.workflow.composite_plan import CompositePlan
from renku.core.models.workflow.provider import IWorkflowProvider
from renku.core.plugins import hookimpl
from renku.core.plugins.workflow import workflow_converter


class CWLToolProvider(IWorkflowProvider):
    """A workflow executor provider using cwltool."""

    @hookimpl
    def workflow_provider(self):
        """Workflow provider name."""
        return (self, "cwltool")

    @hookimpl
    def workflow_execute(self, dag: nx.DiGraph, basedir: Path, config: Dict[str, Any]):
        """Executes a given workflow using cwltool."""
        # run cwl with cwltool
        argv = sys.argv
        sys.argv = ["cwltool"]

        runtime_args = {"rm_tmpdir": False, "move_outputs": "leave", "preserve_entire_environment": True}
        loading_args = {"relax_path_checks": True}
        if config:
            # update both RuntimeContext and LoadingContext parameters with user supplied values
            # context.ContextBase takes care that only available parameters are set in a given class
            runtime_args.update(config)
            loading_args.update(config)

        # Keep all environment variables.
        runtime_context = RuntimeContext(kwargs=runtime_args)
        loading_context = LoadingContext(kwargs=loading_args)

        factory = cwltool.factory.Factory(loading_context=loading_context, runtime_context=runtime_context)

        output_paths = []

        workflows = list(dag.nodes)
        if len(workflows) > 1:
            workflow = CompositePlan(
                id=CompositePlan.generate_id(), plans=workflows, name=f"plan-collection-{uuid4().hex}"
            )
        else:
            workflow = workflows[0]

        with tempfile.NamedTemporaryFile() as f:
            # export Plan to cwl
            converter = workflow_converter("cwl")
            converter(workflow=workflow, basedir=basedir, output=Path(f.name), output_format=None)

            process = factory.make(os.path.relpath(str(f.name)))

            try:
                outputs = process()
            except cwltool.factory.WorkflowStatus:
                raise WorkflowExecuteError()

            sys.argv = argv

            # Move outputs to correct location in the repository.
            output_dirs = process.factory.executor.output_dirs

            def remove_prefix(location, prefix="file://"):
                if location.startswith(prefix):
                    return unquote(location[len(prefix) :])
                return unquote(location)

            locations = {remove_prefix(output["location"]) for output in outputs.values()}
            # make sure to not move an output if it's containing directory gets moved
            locations = {
                location
                for location in locations
                if not any(location.startswith(d) for d in locations if location != d)
            }

            with progressbar(locations, label="Moving outputs") as bar:
                for location in bar:
                    for output_dir in output_dirs:
                        if location.startswith(output_dir):
                            output_path = location[len(output_dir) :].lstrip(os.path.sep)
                            destination = basedir / output_path
                            output_paths.append(destination)
                            if destination.is_dir():
                                shutil.rmtree(str(destination))
                                destination = destination.parent
                            shutil.move(location, str(destination))
                            continue

        return output_paths
