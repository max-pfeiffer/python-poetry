[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![codecov](https://codecov.io/gh/max-pfeiffer/python-poetry/branch/main/graph/badge.svg?token=WQI2SJJLZN)](https://codecov.io/gh/max-pfeiffer/python-poetry)
![pipeline workflow](https://github.com/max-pfeiffer/python-poetry/actions/workflows/pipeline.yml/badge.svg)
![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/pfeiffermax/python-poetry?sort=semver)
![Docker Pulls](https://img.shields.io/docker/pulls/pfeiffermax/python-poetry)
# python-poetry - Docker Image
A Python Docker image with [Poetry](https://python-poetry.org/) installed and
ready to use. You can use this image as a builder base or base image for your
own applications which use [Poetry](https://python-poetry.org/) for dependency
management.

Basis of this image are the [official Python](https://hub.docker.com/_/python)
and [Debian images](https://hub.docker.com/_/debian).

This multiarch image supports AMD64 and ARM64 architectures.

**Docker Hub:** [pfeiffermax/python-poetry](https://hub.docker.com/r/pfeiffermax/python-poetry)

**GitHub Repository:** [https://github.com/max-pfeiffer/python-poetry](https://github.com/max-pfeiffer/python-poetry)

## Docker Image Features
**Poetry versions:**
* v1.5.1
* v1.6.1
* v1.7.1

**Python versions:**
* v3.10
* v3.11
* v3.12

**Operating system:**
* [Debian Bookworm v12.1](https://www.debian.org/releases/bookworm/)
* [Debian Bookworm slim v12.1](https://www.debian.org/releases/bookworm/)

**CPU architectures**
* linux/amd64
* linux/arm64/v8
