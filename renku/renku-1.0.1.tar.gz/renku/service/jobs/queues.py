# -*- coding: utf-8 -*-
#
# Copyright 2020 - Swiss Data Science Center (SDSC)
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
"""Job queues."""
import os

from rq import Queue

from renku.service.cache.base import BaseCache

CLEANUP_QUEUE_FILES = "cache.cleanup.files"
CLEANUP_QUEUE_PROJECTS = "cache.cleanup.projects"

DATASETS_JOB_QUEUE = "datasets.jobs"
MIGRATIONS_JOB_QUEUE = "project.migrations"
GRAPH_JOB_QUEUE = "graph.jobs"

DELAYED_CTRL_DATASETS_CREATE = "delayed.ctrl.DatasetsCreateCtrl"
DELAYED_CTRL_DATASETS_ADD = "delayed.ctrl.DatasetsAddFileCtrl"
DELAYED_CTRL_DATASETS_REMOVE = "delayed.ctrl.DatasetsRemoveCtrl"
DELAYED_CTRL_DATASETS_IMPORT = "delayed.ctrl.DatasetsImportCtrl"
DELAYED_CTRL_DATASETS_EDIT = "delayed.ctrl.DatasetsEditCtrl"
DELAYED_CTRL_DATASETS_UNLINK = "delayed.ctrl.DatasetsUnlinkCtrl"
DELAYED_CTRL_PROJECT_MIGRATE = "delayed.ctrl.MigrateProjectCtrl"
DELAYED_CTRL_CONFIG_SET = "delayed.ctrl.SetConfigCtrl"


QUEUES = [
    CLEANUP_QUEUE_FILES,
    CLEANUP_QUEUE_PROJECTS,
    DATASETS_JOB_QUEUE,
    MIGRATIONS_JOB_QUEUE,
    GRAPH_JOB_QUEUE,
    DELAYED_CTRL_DATASETS_CREATE,
    DELAYED_CTRL_DATASETS_ADD,
    DELAYED_CTRL_DATASETS_REMOVE,
    DELAYED_CTRL_DATASETS_IMPORT,
    DELAYED_CTRL_DATASETS_EDIT,
    DELAYED_CTRL_DATASETS_UNLINK,
    DELAYED_CTRL_PROJECT_MIGRATE,
    DELAYED_CTRL_CONFIG_SET,
]


class WorkerQueues:
    """Worker queues."""

    connection = BaseCache.cache

    @staticmethod
    def describe():
        """List possible queues."""
        return QUEUES

    @staticmethod
    def get(name):
        """Get specific queue object."""
        return Queue(
            name, connection=WorkerQueues.connection, default_timeout=int(os.getenv("WORKER_DEFAULT_JOBS_TIMEOUT", 600))
        )
