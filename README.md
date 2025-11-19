[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
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

This multi arch image supports AMD64 and ARM64 architectures.

**Docker Hub:** [pfeiffermax/python-poetry](https://hub.docker.com/r/pfeiffermax/python-poetry)

**GitHub Repository:** [https://github.com/max-pfeiffer/python-poetry](https://github.com/max-pfeiffer/python-poetry)

## Docker Image Features
**Poetry versions:**
* v1.7.1
* v1.8.5
* v2.2.1

**Python versions:**
* v3.11
* v3.12
* v3.13

**Operating system:**
* [Debian Bookworm v13.2](https://www.debian.org/releases/trixie/)
* [Debian Bookworm slim v13.2](https://www.debian.org/releases/trixie/)

**CPU architectures**
* linux/amd64
* linux/arm64/v8
