from .settings import create_settings
from .entrypoint import Entrypoint


class Application(object):
    def __init__(self, settings):
        self.settings = settings
        self.entry_point = Entrypoint(self.settings.entrypoint)


async def make_application():
    settings = await create_settings()
    return Application(settings=settings)
