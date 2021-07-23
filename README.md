# fastapi-sample
fast api パッケージの雛形

## execute
```
# gunicornで起動
$ gunicorn --config "python:gunicorn_conf" -k uvicorn.workers.UvicronWorker app:app

# 開発時はこちら
$ python3 cli.py
```
