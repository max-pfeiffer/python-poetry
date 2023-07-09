import pytest

from tests.constants import IMAGE_REFERENCES, VERSION
from tests.utils import ImageTagComponents


@pytest.mark.parametrize("image_reference", IMAGE_REFERENCES)
def test_build_version(image_reference) -> None:
    components: ImageTagComponents = ImageTagComponents.create_from_reference(
        image_reference
    )
    assert components.version == VERSION
