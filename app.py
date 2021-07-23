# -*- encoding: utf-8 -*-
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from response import ApiJSONResponse
from routers import endpoint_routers
from midlewares.timer import timer
from handlers.exception import (
    http_exception_handler,
    default_exception_handler,
    HTTPError
)


def create_app(logger=None):
    logger = logger or logging.getLogger('uvicorn')

    fast_app = FastAPI(default_response_class=ApiJSONResponse)

    for router in endpoint_routers:
        fast_app.include_router(router, prefix='/v1')
        for r in router.routes:
            logger.info(f'OK: {list(r.methods)}:{r.path}')

    fast_app.add_exception_handler(HTTPError, http_exception_handler)
    fast_app.add_exception_handler(Exception, default_exception_handler)
    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*']
    )
    fast_app.add_middleware(BaseHTTPMiddleware, dispatch=timer)

    @fast_app.on_event('startup')
    async def startup():
        logger.info('Start up api.')

    @fast_app.on_event('shutdown')
    async def shutdown():
        logger.info('Shutdown api.')

    return fast_app


app = create_app()
