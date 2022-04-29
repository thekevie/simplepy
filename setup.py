from setuptools import setup

import simplepy

author = simplepy.__author__
license = simplepy.__license__
version = simplepy.__version__
description = simplepy.__description__

with open('README.md') as f:
    README = f.read()

packages = [
    'simple-py',
]

setup(
    name='simple-py',
    author=author,
    url='https://github.com/kevys/simple-py',
    project_urls={"Issues": "https://github.com/kevys/simple-py/issues"},
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