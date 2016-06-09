# pasted from https://pythonhosted.org/an_example_pypi_project/setuptools.html
import os
from setuptools import setup


setup(
    name="sample_project",
    version="0.0.1",
    author ="Alex O",
    author_email="alexo@domain.com",
    description=("Example of good python project structure"),
    license="",
    keywords="setuptools example conda package tutorial",
    url="",
    packages=['sample_project'],
    long_description='longer description of the sample_project',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
