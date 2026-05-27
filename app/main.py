from fastapi import FastAPI

router  = FastAPI()

@router.get("/health")
async def root():
    return {
        "message" : "200 Ok"
    }