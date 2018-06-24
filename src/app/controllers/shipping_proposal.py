import asyncio
import logging

from aiohttp import web
from ..models import ShippingProposal


logger = logging.getLogger('application')


async def shipping_proposal(request):
    logger.info('Received request: %s', request)

    # Creating shipment instance
    shipment = await ShippingProposal.from_request(request)
    if not shipment:
        return web.HTTPBadRequest(body="Validation failed")

    # Sending """requests""" to shipment backends
    logger.info('Sending request with shipment proposal %s to backends', shipment)
    proposals = await asyncio.gather(*[backend.process(shipment) for backend in request.app['shipment_backends']],
                                     return_exceptions=True)

    # Filtering them, because coroutine can return None
    proposals = list(filter(lambda x: x is not None and not isinstance(x, Exception), proposals))
    return web.json_response(proposals)
