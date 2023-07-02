from tests.utils import ImageTagComponents
from tests.constants import VERSION, IMAGE_TAGS
import pytest


@pytest.mark.parametrize("image_tag", IMAGE_TAGS)
def test_build_version(image_tag) -> None:
    components: ImageTagComponents = ImageTagComponents.create_from_tag(
        image_tag
    )
    assert components.version == VERSION
