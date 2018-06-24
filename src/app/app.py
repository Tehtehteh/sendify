from .settings import create_settings
from .entrypoint import WebEntrypoint
from .controllers import (
    health, shipping_proposal
)
from .fixtures import (
    DummyShipmentBackend,
    countries_for_dummy_shipment_backend_1,
    countries_for_dummy_shipment_backend_2
)


class Application(object):
    def __init__(self, settings):
        self.settings = settings
        self.web_entry_point = WebEntrypoint(self.settings.settings_dict)

    def prepare(self):

        # Mocking shipment backends
        dummy_shipment_backend_1 = DummyShipmentBackend(name='Dummy Backend_1 Inc.',
                                                        supported_countries=countries_for_dummy_shipment_backend_1,
                                                        supported_package_types=['letter'])
        dummy_shipment_backend_2 = DummyShipmentBackend(name='Dummy Backend_2 Inc.',
                                                        supported_countries=countries_for_dummy_shipment_backend_2,
                                                        supported_package_types=['letter', 'package'])

        # Set shipment backends to application instance
        self.web_entry_point.web_impl['shipment_backends'] = [dummy_shipment_backend_1, dummy_shipment_backend_2]

        # Prepare routes for web entry
        self.web_entry_point.web_impl.router.add_get('/api/v1/_healthz', health)
        self.web_entry_point.web_impl.router.add_post('/api/v1/shipping', shipping_proposal)

    def start(self):
        self.web_entry_point.start()


async def make_application():
    settings = await create_settings()
    return Application(settings=settings)
