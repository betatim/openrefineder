# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'openrefine': {
        'command': ['/home/jovyan/.openrefine/refine', '-p', '{port}', '-d', '/home/jovyan/openrefine', '-i', '0.0.0.0'],
        'port': 3333,
        'timeout': 60,
        'launcher_entry': {
            'enabled': True,
            'title': 'OpenRefine Session',
        },
    },
}
