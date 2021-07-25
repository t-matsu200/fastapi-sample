# -*- encoding: utf-8 -*-
from fastapi import APIRouter, Depends

from dependencies.request import State, base_state


def index_router():
    router = APIRouter()
    tags = ['index']

    @router.get('/', tags=tags)
    def index(state: State = Depends(base_state)):
        return {'state': state}

    return router
