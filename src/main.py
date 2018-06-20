import logging
import asyncio

from .app import make_application

logging.basicConfig(format='[%(asctime)s] [%(pathname)s:%(lineno)d] %(levelname)8s: %(message)s')
log = logging.getLogger('application')
log.setLevel(logging.DEBUG)


async def main():
    input()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
