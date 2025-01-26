from setuptools import setup, find_packages

setup(
    name="core",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=2.0.0",
        "pydantic>=2.0.0",
    ],
) 