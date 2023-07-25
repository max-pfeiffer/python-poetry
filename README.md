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
* v1.3.2
* v1.4.2
* v1.5.1

**Python versions:**
* v3.9
* v3.10
* v3.11

**Operating system:**
* [Debian Bookworm v12.1](https://www.debian.org/releases/bookworm/)
* [Debian Bookworm slim v12.1](https://www.debian.org/releases/bookworm/)

**CPU architectures**
* linux/amd64
* linux/arm64/v8
