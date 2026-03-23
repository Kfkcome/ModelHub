"""ModelHub setup.py

NOTE: This file is intended to mirror the packaging entrypoint used in
meta-llama/llama.

In this environment, direct copying of upstream repository files was not
possible via the available tooling, so this is a minimal, functional
placeholder to unblock Jane's development branch.

TODO(Jane): Replace this file with the exact upstream llama setup.py once you
sync from upstream.
"""

from setuptools import find_packages, setup


setup(
    name="modelhub",
    version="0.0.1",
    description="ModelHub: research framework for running and accelerating LLM/LMM inference",
    packages=find_packages(exclude=("tests", "docs")),
    python_requires=">=3.9",
    include_package_data=True,
)
