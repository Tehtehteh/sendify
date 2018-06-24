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
        model_json = await req.json()
        return cls.from_json(model_json)

    @classmethod
    def from_json(cls, model_json):
        is_valid = cls.validate(model_json)
        if not is_valid:
            logging.warning('Validation failed for ShippingProposal')
            return None
        return cls(**model_json)

    @classmethod
    def validate(cls, _json):
        validator = ShippingProposalValidator()
        if not validator.validate_params(_json):
            logger.error(validator.errors)
            return False
        return True
