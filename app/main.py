from fastapi import FastAPI

from app.api.notes_router import router 
from app.core.excepting import ValidationError, NotFoundError
from app.api.exception_handlers import (
    validation_exception_handler,
    not_found_exception_handler
)

app = FastAPI(title="Notes API ")

app.include_router(router)

app.add_exception_handler(
    ValidationError, validation_exception_handler
)
app.add_exception_handler(
    NotFoundError, not_found_exception_handler
)

