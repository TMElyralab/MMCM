#!/usr/bin/env python
import subprocess
import os
import pkg_resources

from setuptools import setup, find_packages

ProjectDir = os.path.dirname(__file__)
result = subprocess.run(["pip", "install", "basicsr"], capture_output=True, text=True)
result = subprocess.run(
    ["pip", "install", "--no-cache-dir", "-U", "openmim"],
    capture_output=True,
    text=True,
)
result = subprocess.run(["mim", "install", "mmengine"], capture_output=True, text=True)
result = subprocess.run(
    ["mim", "install", "mmcv>=2.0.1"], capture_output=True, text=True
)
result = subprocess.run(
    ["mim", "install", "mmdet>=3.1.0"], capture_output=True, text=True
)
result = subprocess.run(
    ["mim", "install", "mmpose>=1.1.0"], capture_output=True, text=True
)

with open(os.path.join(ProjectDir, "requirements.txt"), "r") as f:
    requirements = f.read().splitlines()
requirements = [x for x in requirements if x and not x.startswith("#")]
requirements = [x.split(" ")[0] if "index-url" in x else x for x in requirements]

setup(
    name="mmcm",  # used in pip install
    version="1.0.0",
    author="anchorxia",
    author_email="anchorxia@tencent.com",
    description="process package for multi media cross modal",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/TMElyralab/MMCM",
    packages=find_packages("."),
    package_dir={"": "."},
    # include_package_data=True,  # please edit MANIFEST.in
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
)
