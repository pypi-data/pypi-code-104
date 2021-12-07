# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 - 2021 TU Wien.
#
# Invenio-Utilities-TUW is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Some utilities for InvenioRDM."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = [
    "pytest-invenio>=1.4.0",
]

extras_require = {
    "docs": [
        "Sphinx>=4.2.0",
    ],
    "tests": tests_require,
}

extras_require["all"] = []
for reqs in extras_require.values():
    extras_require["all"].extend(reqs)

setup_requires = [
    "Babel>=2.8",
]

install_requires = [
    "invenio-app-rdm>=7.0.0",
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("invenio_utilities_tuw", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="invenio-utilities-tuw",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords="invenio utilities tu wien",
    license="MIT",
    author="TU Wien",
    author_email="tudata@tuwien.ac.at",
    url="https://gitlab.tuwien.ac.at/fairdata/invenio-utilities-tuw",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "flask.commands": ["tuw = invenio_utilities_tuw.cli:utilities"],
        "invenio_base.apps": [
            "invenio_utilities_tuw = invenio_utilities_tuw:InvenioUtilitiesTUW",
        ],
        "invenio_i18n.translations": [
            "messages = invenio_utilities_tuw",
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 4 - Beta",
    ],
)
