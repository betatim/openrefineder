from nbopenrefineproxy.handlers import setup_handlers


# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'nbopenrefineproxy',
    }]


def _jupyter_nbextension_paths():
    return [{
        "section": "tree",
        "dest": "nbopenrefineproxy",
        "src": "static",
        "require": "nbopenrefineproxy/tree"
    }]


def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
