import httpx

from app.core.config import settings

BASE_URL = "https://api.opendota.com/api"


def _params(extra: dict | None = None) -> dict:
    params = {}
    if settings.opendota_api_key:
        params["api_key"] = settings.opendota_api_key
    if extra:
        params.update(extra)
    return params


class OpenDotaClient:
    def __init__(self):
        self._client = httpx.AsyncClient(base_url=BASE_URL, timeout=15)

    async def get_player(self, account_id: int) -> dict:
        r = await self._client.get(f"/players/{account_id}", params=_params())
        r.raise_for_status()
        return r.json()

    async def get_player_matches(self, account_id: int, limit: int = 20) -> list[dict]:
        r = await self._client.get(
            f"/players/{account_id}/matches",
            params=_params({"limit": limit}),
        )
        r.raise_for_status()
        return r.json()

    async def get_match(self, match_id: int) -> dict:
        r = await self._client.get(f"/matches/{match_id}", params=_params())
        r.raise_for_status()
        return r.json()

    async def get_heroes(self) -> list[dict]:
        r = await self._client.get("/heroes", params=_params())
        r.raise_for_status()
        return r.json()

    async def get_items(self) -> dict:
        r = await self._client.get("/constants/items", params=_params())
        r.raise_for_status()
        return r.json()

    async def close(self):
        await self._client.aclose()
