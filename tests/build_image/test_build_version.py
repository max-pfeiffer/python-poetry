import pytest

from tests.constants import IMAGE_TAGS, VERSION
from tests.utils import ImageTagComponents


@pytest.mark.parametrize("image_tag", IMAGE_TAGS)
def test_build_version(image_tag) -> None:
    components: ImageTagComponents = ImageTagComponents.create_from_tag(
        image_tag
    )
    assert components.version == VERSION
