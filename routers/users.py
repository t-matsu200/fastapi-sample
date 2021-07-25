# -*- encoding: utf-8 -*-
import logging
import traceback

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from exception import InternalServerError
from model.users import Users

logger = logging.getLogger('uvicorn')


def users_router(get_db: callable):
    router = APIRouter()
    tags = ['users']

    @router.get('/users', tags=tags)
    def get_user(session: Session = Depends(get_db)):
        try:
            users = Users.find_all(session)
            return {'user': users}
        except Exception as e:
            logger.error(traceback.format_exc())
            raise InternalServerError(description='Occurred server error in /v1/users.')

    return router
