#!/usr/bin/env python

from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()
requirements = [x for x in requirements if x and not x.startswith("#")]
setup(
    name="mmcm",  # used in pip install
    version="1.0.0",
    author="anchorxia",
    author_email="anchorxia@tencent.com",
    description="process package for multi media cross modal",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/TMElyralab/MMCM",
    # include_package_data=True,  # please edit MANIFEST.in
    packages=find_packages("mmcm"),
    package_dir={"": "mmcm"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    dependency_links=["https://download.pytorch.org/whl/cu118"],
)
