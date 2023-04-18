"""Setup."""
from setuptools import find_packages, setup


def load_long_description(filename: str) -> str:
    """Convert README.md to a string."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="ipfsclient",
    version="0.0.3",
    author="Nathaniel Schultz",
    author_email="nate@nanoswap.finance",
    description="IPFS RPC Client",
    long_description=load_long_description("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/nanoswap/ipfsclient",
    project_urls={
        "Bug Tracker": "https://github.com/nanoswap/ipfsclient/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: The Unlicense (Unlicense)"
    ],
    package_dir={'ipfsclient': "ipfsclient"},
    packages=find_packages("ipfsclient"),
    python_requires=">=3.11"
)
