# -*- encoding: utf-8 -*-
from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic.error_wrappers import ValidationError
from exception import (
    HTTPError, BadRequest, InternalServerError, error_handler
)


def http_exception_handler(request: Request, e: HTTPError) -> JSONResponse:
    """Base handler"""
    return JSONResponse(status_code=e.code, content=e.to_dict())


def default_exception_handler(request: Request, e: Exception) -> JSONResponse:
    """Handler of default exception"""
    if isinstance(e, ValidationError):
        return http_exception_handler(
            request,
            BadRequest(description='Invalid parameters')
        )
    return http_exception_handler(
        request,
        InternalServerError(description='Request failed')
    )
