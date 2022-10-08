# References: using official Python images
# https://hub.docker.com/_/python
ARG OFFICIAL_PYTHON_IMAGE
ARG IMAGE_POETRY_VERSION
ARG APPLICATION_SERVER_PORT
FROM ${OFFICIAL_PYTHON_IMAGE}

LABEL maintainer="Max Pfeiffer <max@maxpfeiffer.ch>"

# References:
# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
# https://pip.pypa.io/en/stable/topics/caching/#avoiding-caching
# https://pip.pypa.io/en/stable/cli/pip/?highlight=PIP_NO_CACHE_DIR#cmdoption-no-cache-dir
# https://pip.pypa.io/en/stable/cli/pip/?highlight=PIP_DISABLE_PIP_VERSION_CHECK#cmdoption-disable-pip-version-check
# https://pip.pypa.io/en/stable/cli/pip/?highlight=PIP_DEFAULT_TIMEOUT#cmdoption-timeout
# https://pip.pypa.io/en/stable/topics/configuration/#environment-variables
# https://python-poetry.org/docs/#installation

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=${IMAGE_POETRY_VERSION} \
    POETRY_HOME="/opt/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

# https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential \
        curl \
    && curl -sSL https://install.python-poetry.org | python - \
    && apt-get purge --auto-remove -y \
      build-essential \
      curl
