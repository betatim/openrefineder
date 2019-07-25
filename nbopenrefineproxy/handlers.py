from urllib.parse import urlunparse, urlparse

from tornado import web

from notebook.base.handlers import IPythonHandler
from notebook.utils import url_path_join as ujoin

from nbserverproxy.handlers import SuperviseAndProxyHandler
import os

class OpenRefineProxyHandler(SuperviseAndProxyHandler):
    name = 'OpenRefine'

    def get_cmd(self):
        path = os.path.join(os.environ['HOME'], 'openrefine')
        os.makedirs(path, exist_ok=True)
        cmd = ['openrefine-3.1/refine',
               '-p', str(self.port),
               '-d',path
               ]
        return cmd

    def get_env(self):
        return {}


class AddSlashHandler(IPythonHandler):
    """Handler for adding trailing slash to URLs that need them"""
    @web.authenticated
    def get(self, *args):
        src = urlparse(self.request.uri)
        dest = src._replace(path=src.path + '/')
        self.redirect(urlunparse(dest))


def setup_handlers(web_app):
    web_app.add_handlers('.*', [
        (ujoin(web_app.settings['base_url'], 'openrefine/(.*)'),
         OpenRefineProxyHandler, dict(state={'port':3333})),
        (ujoin(web_app.settings['base_url'], 'openrefine'), AddSlashHandler)
        ])
