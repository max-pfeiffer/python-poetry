"""Tests for image version."""

from tests.utils import ImageTagComponents


def test_build_version(image_reference: str, image_version: str) -> None:
    """Test build version.

    :param image_reference:
    :param image_version:
    :return:
    """
    components: ImageTagComponents = ImageTagComponents.create_from_reference(
        image_reference
    )
    assert components.version == image_version
