# -*- encoding: utf-8 -*-
# 認証処理があれば、こちらに実装する
from typing import Optional

from fastapi import Cookie
from pydantic import BaseModel


class User(BaseModel):
    name: Optional[str]


def auth(name=Cookie(None)) -> User:
    return User(name=name)
