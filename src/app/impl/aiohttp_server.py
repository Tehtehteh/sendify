from aiohttp import web


def make_app():
    return web.Application()


def run_app(app, port, **kwargs):
    web.run_app(app=app, port=port, **kwargs)
