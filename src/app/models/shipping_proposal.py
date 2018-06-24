import logging

import trafaret as t
from trafaret_validator import TrafaretValidator


logger = logging.getLogger('application')


class ShippingProposalValidator(TrafaretValidator):
    origin = t.String
    destination = t.String
    package_type = t.Enum("letter", "package", "pallet")
    dimensions = t.List(t.Int)
    weight = t.Float


class ShippingProposal(object):

    def __init__(self, origin, destination, package_type, dimensions, weight):
        logger.info('Creating new ShippingProposal instance')
        self.origin = origin
        self.destination = destination
        self.package_type = package_type
        self.dimensions = dimensions
        self.weight = weight

    def __str__(self):
        return f'ShippingProposal (FROM:{self.origin}, TO:{self.destination}, TYPE:{self.package_type}, ' \
               f'WEIGHT:{self.weight}, DIMENSIONS:{self.dimensions}.'

    @classmethod
    async def from_request(cls, req):
        json = await req.json()
        return cls.from_json(json)

    @classmethod
    def from_json(cls, _json):
        is_valid = cls.validate(_json)
        if not is_valid:
            logging.warning('Validation failed for ShippingProposal')
            return None
        kwargs = {
            'origin': _json['origin'],
            'destination': _json['destination'],
            'package_type': _json['package_type'],
            'dimensions': _json['dimensions'],
            'weight': _json['weight']
        }
        return cls(**kwargs)

    @classmethod
    def validate(cls, _json):
        validator = ShippingProposalValidator()
        if not validator.validate_params(_json):
            logger.error(validator.errors)
            return False
        return True
