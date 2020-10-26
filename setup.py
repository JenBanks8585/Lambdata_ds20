import setuptools

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_DS20", # the name that you will install via pip
    version="1.0",
    author="JenBanks",
    author_email="jenlaman@gmail.com",
    description="DS helper",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/JenBanks8585/Lambdata_ds20",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
