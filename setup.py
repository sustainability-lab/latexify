#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="latexify-matplotlib",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@institution.edu",
    description="Professional matplotlib formatting for LaTeX documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sustainability-lab/latexify",
    py_modules=["latexify"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    python_requires=">=3.7",
    install_requires=[
        "matplotlib>=3.0.0",
        "numpy>=1.15.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
        ],
    },
    keywords="matplotlib latex publication academic plots figures",
    project_urls={
        "Bug Reports": "https://github.com/sustainability-lab/latexify/issues",
        "Source": "https://github.com/sustainability-lab/latexify",
        "Documentation": "https://github.com/sustainability-lab/latexify/blob/main/README.md",
    },
)