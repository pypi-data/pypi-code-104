import asyncio
from typing import Optional

from api import FTWClient
from ftwgl.rcon import RCON


class GameServer:
    def __init__(self, id, dcid, ip: Optional[str], rcon: str, password: str, ftw_client: FTWClient):
        self.id = id
        self.dcid = dcid
        self.ip = ip
        self.rcon = rcon
        self.password = password
        self._ftw_client = ftw_client
        self._rcon_client: Optional[RCON] = None

    async def wait_until_setup(self):
        if self.ip is not None:
            return

        server = await self._ftw_client.server_get_with_id(self.id)
        while 'ip' not in server['config']:
            await asyncio.sleep(5)
            server = await self._ftw_client.request_server_get_with_id(self.id)
        self.ip = server['config']['ip']

    def rcon(self, command: str) -> str:
        if self._rcon_client is None:
            if self.ip is None:
                raise ValueError(f"GameServer ({self.id}) ip currently is None, likely still booting")
            else:
                self._rcon_client = RCON(server=self.ip, password=self.rcon)

        return self._rcon_client.rcon(command)
