from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from datetime import datetime, timezone
from typing import Any


def create_error_response(message: Any,status_code: int = 500)-> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "success":False,
            "data": None,
            "error": message,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
)

def register_exception_handlers(app_instance: FastAPI):

    @app_instance.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return create_error_response(exc.detail, exc.status_code)

    @app_instance.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return create_error_response(exc.errors(), 422)

    @app_instance.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return create_error_response("Internal Server Error", 500)