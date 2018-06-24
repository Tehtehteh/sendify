import asyncio

from unittest import TestCase
from app.fixtures import (
    valid_shipment_json,
    DummyShipmentBackend,
    countries_for_dummy_shipment_backend_1
)
from app.models import ShippingProposal


class TestShippingProposal(TestCase):

    def _run_coro(self, coro):
        return self.loop.run_until_complete(coro)

    @classmethod
    def setUpClass(cls):
        cls.loop = asyncio.get_event_loop()
        cls.test_backend_1 = DummyShipmentBackend(name="Test Dummy backend №1",
                                                  supported_countries=countries_for_dummy_shipment_backend_1,
                                                  supported_package_types=["letter"],
                                                  fixed_price=13.37)
        cls.test_backend_2 = DummyShipmentBackend(name="Test Dummy backend №2",
                                                  supported_countries=[],
                                                  supported_package_types=[])

    def test_one_backend_available(self):
        proposal = ShippingProposal.from_json(valid_shipment_json)
        result = self._run_coro(self.test_backend_1.process(proposal))
        self.assertEquals(result, {
            'carrier': self.test_backend_1.name,
            'price': 13.37,
            'product': 'economic',
            'expected_transit_time': '5-10 days'
        }, msg="Should equal test_backend_1 with fixed price")

    def test_no_backends_available(self):
        proposal = ShippingProposal.from_json(valid_shipment_json)
        proposal.origin = 'NON-EXISTING COUNTRY'
        result = self._run_coro(self.test_backend_2.process(proposal))
        self.assertIsNone(result, msg="No shipping proposals for NON-EXISTING COUNTRIES!!!")
