# -*- encoding: utf-8 -*-
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from database import TestDatabase, SqliteDatabase, Database
from db_config import db_config
from response import ApiJSONResponse
from routers.index import index_router
from routers.users import users_router
from midlewares.timer import timer
from handlers.exception import (
    http_exception_handler,
    default_exception_handler,
    HTTPError
)


def create_app(logger=None, is_test=False):
    logger = logger or logging.getLogger('uvicorn')

    fast_app = FastAPI(default_response_class=ApiJSONResponse)
    if is_test:
        sqlalchemy_db = TestDatabase()
        sqlalchemy_db.setup_database()
    else:
        # sqlalchemy_db = SqliteDatabase()
        sqlalchemy_db = Database(**db_config)

    fast_app.include_router(index_router())
    fast_app.include_router(users_router(sqlalchemy_db.get_db), prefix='/v1')

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
