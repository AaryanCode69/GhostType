from fastapi import FastAPI
from core.database import engine, Base
import models.user
import api.routes_auth

router  = FastAPI(title="GhostType")

@router.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)