from fastapi import FastAPI
from core.database import engine, Base

router  = FastAPI(title="GhostType")

@router.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)