from tests.utils import ImageTagComponents


def test_build_version(image_reference: str, image_version: str) -> None:
    components: ImageTagComponents = ImageTagComponents.create_from_reference(
        image_reference
    )
    assert components.version == image_version
