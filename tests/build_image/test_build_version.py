from tests.utils import ImageTagComponents


def test_build_version(python_poetry_image, version) -> None:
    components: ImageTagComponents = ImageTagComponents.create_from_tag(
        python_poetry_image
    )
    assert components.version == version
