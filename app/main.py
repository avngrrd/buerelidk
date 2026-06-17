from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.services.opendota import OpenDotaClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.opendota = OpenDotaClient()
    yield
    await app.state.opendota.close()


app = FastAPI(title="Dota Stats", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}
