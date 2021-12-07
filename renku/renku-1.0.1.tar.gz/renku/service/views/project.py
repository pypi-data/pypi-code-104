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
"""Renku service project view."""
from flask import request

from renku.service.config import SERVICE_PREFIX
from renku.service.controllers.project_edit import ProjectEditCtrl
from renku.service.controllers.project_show import ProjectShowCtrl
from renku.service.views.api_versions import V1_0, VersionedBlueprint
from renku.service.views.decorators import accepts_json, handle_common_except, requires_cache, requires_identity

PROJECT_BLUEPRINT_TAG = "project"
project_blueprint = VersionedBlueprint(PROJECT_BLUEPRINT_TAG, __name__, url_prefix=SERVICE_PREFIX)


@project_blueprint.route("/project.show", methods=["POST"], provide_automatic_options=False, versions=[V1_0])
@handle_common_except
@accepts_json
@requires_cache
@requires_identity
def show_project_view(user_data, cache):
    """
    Show project metadata view.

    ---
    post:
      description: Show project metadata.
      requestBody:
        content:
          application/json:
            schema: ProjectShowRequest
      responses:
        200:
          description: Metadata of the project.
          content:
            application/json:
              schema: ProjectShowResponseRPC
      tags:
        - project
    """
    return ProjectShowCtrl(cache, user_data, dict(request.json)).to_response()


@project_blueprint.route("/project.edit", methods=["POST"], provide_automatic_options=False, versions=[V1_0])
@handle_common_except
@accepts_json
@requires_cache
@requires_identity
def edit_project_view(user_data, cache):
    """
    Edit project metadata view.

    ---
    post:
      description: Edit project metadata.
      requestBody:
        content:
          application/json:
            schema: ProjectEditRequest
      responses:
        200:
          description: Status of the requested project edits.
          content:
            application/json:
              schema: ProjectEditResponseRPC
      tags:
        - project
    """
    return ProjectEditCtrl(cache, user_data, dict(request.json)).to_response()
