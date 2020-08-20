from setuptools import setup

VERSION = '1.1.0'

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="add_vhost_5",
    version=VERSION,
    description="Creates a virtual host in the local development machine",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="VirtualHost development environment local apache",
    url="https://github.com/danilocgsilva/add_vhost_5",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["add_vhost_5"],
    entry_points={"console_scripts": [
        "avhost=add_vhost_5.__main__:avhost",
        "avhostcheck=add_vhost_5.__main__:avhostcheck"
    ],},
    include_package_data=True
)
