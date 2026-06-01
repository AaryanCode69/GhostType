from fastapi import FastAPI
from core.database import engine, Base
import models.user
import api.routes_auth
from core.exceptions import register_exception_handlers

router  = FastAPI(title="GhostType")

register_exception_handlers(router)

@router.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

router.include_router(api.routes_auth.router)