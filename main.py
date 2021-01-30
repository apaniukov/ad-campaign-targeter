from fastapi import FastAPI

from ad_targeter.routes.clusters import router as clusters_router
from ad_targeter.routes.targeter import router as target_router

app = FastAPI()
app.include_router(target_router)
app.include_router(clusters_router)
