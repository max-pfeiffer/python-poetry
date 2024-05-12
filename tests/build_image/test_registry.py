"""Tests for container registry container."""

from furl import furl
from requests import Response, get
from requests.auth import HTTPBasicAuth
from testcontainers.registry import DockerRegistryContainer

from tests.constants import REGISTRY_PASSWORD, REGISTRY_USERNAME
from tests.utils import ImageTagComponents

BASIC_AUTH: HTTPBasicAuth = HTTPBasicAuth(REGISTRY_USERNAME, REGISTRY_PASSWORD)


def test_registry_with_images(
    registry_container: DockerRegistryContainer, image_reference: str
):
    """Test if registry container contains an image.

    :param registry_container:
    :param image_reference:
    :return:
    """
    furl_item: furl = furl(f"http://{registry_container.get_registry()}")
    furl_item.path /= "v2/_catalog"

    response: Response = get(furl_item.url, auth=BASIC_AUTH)

    assert response.status_code == 200
    assert response.json() == {"repositories": ["pfeiffermax/python-poetry"]}

    furl_item: furl = furl(f"http://{registry_container.get_registry()}")
    furl_item.path /= "v2/pfeiffermax/python-poetry/tags/list"

    response: Response = get(furl_item.url, auth=BASIC_AUTH)

    assert response.status_code == 200

    response_image_tags: list[str] = response.json()["tags"]
    image_tag: str = ImageTagComponents.create_from_reference(image_reference).tag

    assert image_tag in response_image_tags
