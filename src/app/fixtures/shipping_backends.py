import random

from logging import getLogger

logger = getLogger('application')


class DummyShipmentBackend(object):

    def __init__(self, name, supported_countries, supported_package_types, fixed_price=None):
        self.supported_countries = supported_countries
        self.supported_package_types = supported_package_types
        self.name = name
        self.fixed_price = fixed_price

    def __str__(self):
        return f'{self.name} shipment backend'

    def is_proposal_valid(self, proposal):
        """
        :param proposal: ..models.ShippingProposal
        :return: boolean
        """
        return all((proposal.destination in self.supported_countries, proposal.origin in self.supported_countries,
                    proposal.package_type in self.supported_package_types))

    async def process(self, proposal):
        logger.info('%s is processing shipment proposal.', self)
        if self.is_proposal_valid(proposal):
            logger.info('%s is valid to %s', proposal, self)
            return {
                'carrier': self.name,
                'price': self.fixed_price if self.fixed_price is not None else random.randint(10, 100),
                'product': 'economic',
                'expected_transit_time': '5-10 days'
            }
        else:
            logger.info('%s does not support shipment %s', self, proposal)
