import setuptools

setuptools.setup(
    name="nbopenrefineproxy",
    version='0.0.1',
    url="https://github.com/betatim/nbopenrefineproxy",
    author="Tim Head",
    description="Jupyter extension to proxy OpenRefine sessions",
    packages=setuptools.find_packages(),
    keywords=['Jupyter'],
    classifiers=['Framework :: Jupyter'],
    install_requires=[
        'notebook',
        'nbserverproxy >= 0.3.2'
    ],
    package_data={'nbopenrefineproxy': ['static/*']},
)
