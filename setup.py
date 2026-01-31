"""Setup configuration for adk-testing project."""

from setuptools import setup, find_packages

setup(
    name="adk-testing",
    version="0.1.0",
    description="Multi-agent routing system using Google ADK",
    author="Vikram",
    python_requires=">=3.9",
    packages=find_packages(where=".", include=["agents*"]),
    install_requires=[
        "google-adk",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "ruff>=0.1.0",
        ],
    },
)