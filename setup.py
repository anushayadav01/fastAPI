#!/usr/bin/python3
#-------------------------------------------------------------
#Setup script
#-------------------------------------------------------------
from setuptools import setup, find_packages

setup(
    name='fastAPI',
    packages=find_packages(),
    version='1.0.0',
    url='https://github.com/anushayadav01/fastAPI',
    classifiers=[
        "Topic :: Utilities",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.0",
        "Topic :: Software Development :: Embedded Systems",
    ],

    install_requires=[
        "python-daemon>=2.0",
        "fastapi_websocket_rpc",
        "fastapi",
        "uvicorn",
        "pydantic",
        "tenacity"
    ],
)
