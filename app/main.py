from fastapi import FastAPI

app = FastAPI(title="Dota Stats")


@app.get("/health")
def health():
    return {"status": "ok"}
