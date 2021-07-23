# -*- encoding: utf-8 -*-
from fastapi import APIRouter, Depends

from dependencies.request import State, base_state

router = APIRouter()


@router.get('/')
def index(state: State = Depends(base_state)):
    return {'state': state}
