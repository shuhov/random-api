import os
from pathlib import Path

import setuptools

from random_api.project import version

root = Path(__file__).resolve().parents[1]
requirements_path = os.path.join("root", "requirements.txt")
with open(requirements_path, "r") as f:
    install_require = f.readlines()

setuptools.setup(
    version=version,
    description="Random-api",
    url="https://github.com/shuhov/random-api",
    packages=setuptools.find_packages(),
    install_require=install_require,
    include_package_data="True",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
