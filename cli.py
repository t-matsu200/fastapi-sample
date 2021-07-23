# -*- encoding: utf-8 -*-
import uvicorn
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description='Sample API')
    parser.add_argument('--host', default='127.0.0.1',
                        help='Bind socket to this host')
    parser.add_argument('--port', default=8080, type=int,
                        help='Bind socket to this port')
    return parser.parse_args()


def main():
    args = parse_args()
    uvicorn.run('app:app', host=args.host, port=args.port, log_level='info')


if __name__ == '__main__':
    main()
