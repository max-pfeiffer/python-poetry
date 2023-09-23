from tests.constants import VERSION
from tests.utils import ImageTagComponents


def test_build_version(image_reference) -> None:
    components: ImageTagComponents = ImageTagComponents.create_from_reference(
        image_reference
    )
    assert components.version == VERSION
