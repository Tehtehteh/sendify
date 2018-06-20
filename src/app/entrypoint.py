import threading

from .impl import aiohttp_server as impl


class Entrypoint(object):
    def __init__(self, entry_point_settings):
        self._settings = entry_point_settings
        self._stop_fn = exit  # Dangerous

    def start(self):
        thread = threading.Thread(self.start_impl)
        thread.start()

    def start_impl(self):
        app = impl.make_app()
        """:type: aiohttp.web.Application"""
        self._stop_fn = app.shutdown
        impl.run_app(app, port=self._settings.port)
