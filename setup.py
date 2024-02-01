"""Setup script."""

from setuptools import find_packages
from setuptools import setup


setup(
    name="keras",
    description="Multi-backend Keras.",
    long_description_content_type="text/markdown",
    version="3.0.4",
    url="https://github.com/keras-team/keras",
    author="Keras team",
    author_email="keras-users@googlegroups.com",
    license="Apache License 2.0",
    install_requires=[
        "absl-py",
        "numpy",
        "rich",
        "namex",
        "h5py",
        "dm-tree",
        "ml-dtypes",
    ],
    # Supported Python versions
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
    packages=find_packages(exclude=("*_test.py",)),
)
