from unittest import TestCase
from app.fixtures import (
    invalid_shipment_json,
    valid_shipment_json
)
from app.models import ShippingProposal


class TestShippingProposal(TestCase):

    def test_parse_from_invalid(self):
        proposal = ShippingProposal.from_json(invalid_shipment_json)
        self.assertIsNone(proposal, msg="Proposal has malformed body")

    def test_parse_from_valid(self):
        proposal = ShippingProposal.from_json(valid_shipment_json)
        self.assertIsNotNone(proposal, msg="Proposal has valid body")


