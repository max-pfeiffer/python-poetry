from pathlib import Path
from typing import Optional

import docker
from docker.models.images import Image

from build.constants import (
    PYTHON_POETRY_IMAGE_NAME,
    BASE_IMAGES,
    POETRY_VERSIONS,
)


class DockerImage:
    def __init__(self, docker_client: docker.client):
        self.docker_client: docker.client = docker_client
        self.absolute_module_directory_path: Path = Path(
            __file__
        ).parent.resolve()
        self.image_name: Optional[str] = None
        self.image_tag: Optional[str] = None
        self.version_tag: Optional[str] = None
        self.dockerfile_name: str = "Dockerfile"


class PythonPoetryImage(DockerImage):
    def __init__(self, docker_client: docker.client):
        super().__init__(docker_client)
        self.absolute_docker_image_directory_path: Path = (
            self.absolute_module_directory_path
        )

        # An image name is made up of slash-separated name components, optionally prefixed by a registry hostname.
        # see: https://docs.docker.com/engine/reference/commandline/tag/
        self.image_name = PYTHON_POETRY_IMAGE_NAME

    def build(self, target_architecture: str, version: str = None) -> Image:
        self.version_tag = version

        buildargs: dict[str, str] = {
            "OFFICIAL_PYTHON_IMAGE": BASE_IMAGES[target_architecture],
            "POETRY_VERSION": POETRY_VERSIONS[target_architecture],
        }
        tag: str = f"{self.image_name}:{self.version_tag}-{target_architecture}"

        image: Image = self.docker_client.images.build(
            path=str(self.absolute_docker_image_directory_path),
            dockerfile=self.dockerfile_name,
            tag=tag,
            buildargs=buildargs,
        )[0]
        return image
