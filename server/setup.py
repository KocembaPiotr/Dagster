from setuptools import find_packages, setup

setup(
    name="server",
    packages=find_packages(exclude=["server_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
