import asyncio
import threading
import logging

from .impl import aiohttp_server as impl


logger = logging.getLogger('application')


class WebEntrypoint(object):
    def __init__(self, entry_point_settings):
        self._settings = entry_point_settings
        self.loop = asyncio.new_event_loop()
        self._stop_fn = exit  # Dangerous
        self.web_impl = impl.make_app()

    def start(self):
        thread = threading.Thread(target=self.start_impl, args=(self.loop,))
        thread.start()

    def start_impl(self, loop):
        logger.info('Starting web entrypoint on %s port', self._settings['app']['port'])
        asyncio.set_event_loop(loop)
        self._stop_fn = self.web_impl.shutdown
        impl.run_app(self.web_impl, port=self._settings['app']['port'], handle_signals=False, print=None)
        loop.run_forever()
