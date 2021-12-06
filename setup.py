from setuptools import setup

import games

author = games.__author__
license = games.__license__
version = games.__version__
description = games.__description__

with open('README.md') as f:
    README = f.read()

packages = [
    'games',
]

setup(
    name='python-games',
    author=author,
    url='https://github.com/kevys/python-games',
    project_urls={"Issues": "https://github.com/kevys/python-games/issues"},
    version=version,
    packages=packages,
    license=license,
    description=description,
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires='>=3.8.0',
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)