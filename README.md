# fastapi-sample
fast api パッケージの雛形

## execute
```
# gunicornで起動
$ gunicorn --config "python:gunicorn_conf" -k uvicorn.workers.UvicornWorker app:app

# 開発時はこちら
$ python3 cli.py
```

# docker-compose
## 起動
```
$ docker-compose up -d (--build)
```
## 停止
```
$ docker-compose down
```
