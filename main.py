import uvicorn  # type: ignore
from fastapi import FastAPI

from ad_targeter.routes.clusters import router as clusters_router
from ad_targeter.routes.targeter import router as target_router
from settings import config


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(target_router)
    app.include_router(clusters_router)

    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host=config.host, port=config.port, log_level="info")
