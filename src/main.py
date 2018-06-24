import logging
import asyncio

from app import make_application

logging.basicConfig(format='[%(asctime)s] [%(pathname)s:%(lineno)d] %(levelname)8s: %(message)s')
log = logging.getLogger('application')
log.setLevel(logging.INFO)

loop = asyncio.get_event_loop()


async def main():
    app = await make_application()
    """:type: app.Application"""
    app.prepare()
    app.start()


if __name__ == '__main__':
    loop.run_until_complete(main())
