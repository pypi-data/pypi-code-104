
from flask import request

from assemblyline.odm.messages.changes import Operation
from assemblyline.odm.models.heuristic import Heuristic
from assemblyline.odm.models.service import Service
from assemblyline.remote.datatypes.events import EventSender
from assemblyline_service_server.api.base import api_login, make_api_response, make_subapi_blueprint
from assemblyline_service_server.config import LOGGER, STORAGE, config

SUB_API = 'service'
service_api = make_subapi_blueprint(SUB_API, api_version=1)
service_api._doc = "Perform operations on service"

event_sender = EventSender('changes.services',
                           host=config.core.redis.nonpersistent.host,
                           port=config.core.redis.nonpersistent.port)


@service_api.route("/register/", methods=["PUT", "POST"])
@api_login()
def register_service(client_info):
    """

    Data Block:
    {
    TODO: service manifest
    }

    Result example:
    {'keep_alive': true}
    """
    data = request.json
    keep_alive = True

    try:
        # Get heuristics list
        heuristics = data.pop('heuristics', None)

        # Patch update_channel, registry_type before Service registration object creation
        data['update_channel'] = data.get('update_channel', config.services.preferred_update_channel)
        data['docker_config']['registry_type'] = data['docker_config'] \
            .get('registry_type', config.services.preferred_registry_type)
        for dep in data.get('dependencies', {}).values():
            dep['container']['registry_type'] = dep.get('registry_type', config.services.preferred_registry_type)

        # Pop unused registration data
        for x in ['file_required', 'tool_version']:
            data.pop(x, None)

        # Create Service registration object
        service = Service(data)

        # Fix service version, we don't need to see the stable label
        service.version = service.version.replace('stable', '')

        # Save service if it doesn't already exist
        if not STORAGE.service.exists(f'{service.name}_{service.version}'):
            STORAGE.service.save(f'{service.name}_{service.version}', service)
            STORAGE.service.commit()
            LOGGER.info(f"{client_info['client_id']} - {client_info['service_name']} registered")
            keep_alive = False

        # Save service delta if it doesn't already exist
        if not STORAGE.service_delta.exists(service.name):
            STORAGE.service_delta.save(service.name, {'version': service.version})
            STORAGE.service_delta.commit()
            LOGGER.info(f"{client_info['client_id']} - {client_info['service_name']} "
                        f"version ({service.version}) registered")

        new_heuristics = []
        if heuristics:
            plan = STORAGE.heuristic.get_bulk_plan()
            for index, heuristic in enumerate(heuristics):
                heuristic_id = f'#{index}'  # Set heuristic id to it's position in the list for logging purposes
                try:
                    # Append service name to heuristic ID
                    heuristic['heur_id'] = f"{service.name.upper()}.{str(heuristic['heur_id'])}"

                    # Attack_id field is now a list, make it a list if we receive otherwise
                    attack_id = heuristic.get('attack_id', None)
                    if isinstance(attack_id, str):
                        heuristic['attack_id'] = [attack_id]

                    heuristic = Heuristic(heuristic)
                    heuristic_id = heuristic.heur_id
                    plan.add_upsert_operation(heuristic_id, heuristic)
                except Exception as e:
                    LOGGER.exception(f"{client_info['client_id']} - {client_info['service_name']} "
                                     f"invalid heuristic ({heuristic_id}) ignored: {str(e)}")
                    raise ValueError("Error parsing heuristics")

            for item in STORAGE.heuristic.bulk(plan)['items']:
                if item['update']['result'] != "noop":
                    new_heuristics.append(item['update']['_id'])
                    LOGGER.info(f"{client_info['client_id']} - {client_info['service_name']} "
                                f"heuristic {item['update']['_id']}: {item['update']['result'].upper()}")

            STORAGE.heuristic.commit()

        service_config = STORAGE.get_service_with_delta(service.name, as_obj=False)

        # Notify components watching for service config changes
        event_sender.send(service.name, {
            'operation': Operation.Added,
            'name': service.name
        })

    except ValueError as e:  # Catch errors when building Service or Heuristic model(s)
        return make_api_response("", err=e, status_code=400)

    return make_api_response(dict(
        keep_alive=keep_alive,
        new_heuristics=new_heuristics,
        service_config=service_config or dict(),
    ))
