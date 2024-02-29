"""Build utilities."""

from pathlib import Path


def get_context() -> Path:
    """Docker build context.

    :return:
    """
    return Path(__file__).parent.resolve()


def get_image_reference(
    registry: str,
    image_version: str,
    poetry_version: str,
    python_version: str,
    os_variant: str,
) -> str:
    """Docker Hub image reference.

    :param registry:
    :param image_version:
    :param poetry_version:
    :param python_version:
    :param os_variant:
    :return:
    """
    reference: str = (
        f"{registry}/pfeiffermax/python-poetry:"
        f"{image_version}-poetry{poetry_version}-python{python_version}-{os_variant}"
    )
    return reference
