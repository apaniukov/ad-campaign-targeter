from fastapi import FastAPI

from ad_targeter.router import router as target_router

app = FastAPI()
app.include_router(target_router)
