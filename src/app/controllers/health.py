import aiohttp

from aiohttp import web


async def health(req):
    return web.json_response({'ok': True})
