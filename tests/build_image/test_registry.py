from furl import furl
from requests import Response, get
from requests.auth import HTTPBasicAuth

from tests.constants import REGISTRY_PASSWORD, REGISTRY_USERNAME
from tests.registry_container import DockerRegistryContainer
from tests.utils import ImageTagComponents

BASIC_AUTH: HTTPBasicAuth = HTTPBasicAuth(REGISTRY_USERNAME, REGISTRY_PASSWORD)


def test_registry(registry_container: DockerRegistryContainer):
    furl_item: furl = furl(f"http://{registry_container.get_registry()}")
    furl_item.path /= "v2/_catalog"

    response: Response = get(furl_item.url, auth=BASIC_AUTH)

    assert response.status_code == 200


def test_registry_with_images(
    registry_container: DockerRegistryContainer, images: list[str]
):
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
    image_tags: list[str] = [
        ImageTagComponents.create_from_reference(reference).tag
        for reference in images
    ]
    difference = set(image_tags).difference(set(response_image_tags))

    assert not difference
