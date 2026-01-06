from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.excepting import ValidationError, NotFoundError
from app.api.response import build_response


def validation_exception_handler(
    request: Request,
    exc: ValidationError
):
    return JSONResponse(
        status_code=400,
        content=build_response(
            success=False,
            message=str(exc),
            data=None
        )
    )


def not_found_exception_handler(
    request: Request,
    exc: NotFoundError
):
    return JSONResponse(
        status_code=404,
        content=build_response(
            success=False,
            message=str(exc),
            data=None
        )
    )
