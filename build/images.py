from pathlib import Path
from typing import Optional

from docker.models.images import Image
from docker.client import DockerClient
from build.constants import (
    PYTHON_POETRY_IMAGE_NAME,
    BASE_IMAGES,
    POETRY_VERSIONS,
)


class DockerImage:
    def __init__(
        self,
        docker_client: DockerClient,
        target_architecture: str,
        version: str,
    ):
        self.docker_client: DockerClient = docker_client
        self.dockerfile_name: str = "Dockerfile"
        self.image_name: Optional[str] = None
        self.image_tag: Optional[str] = None
        self.version: Optional[str] = version
        self.target_architecture: str = target_architecture


class PythonPoetryImage(DockerImage):
    def __init__(
        self,
        docker_client: DockerClient,
        target_architecture: str,
        version: str,
    ):
        super().__init__(docker_client, target_architecture, version)
        self.dockerfile_directory: Path = Path(__file__).parent.resolve()

        # An image name is made up of slash-separated name components, optionally prefixed by a registry hostname.
        # see: https://docs.docker.com/engine/reference/commandline/tag/
        self.image_name = PYTHON_POETRY_IMAGE_NAME

    def build(self) -> Image:
        self.image_tag = f"{self.version}-{self.target_architecture}"

        buildargs: dict[str, str] = {
            "OFFICIAL_PYTHON_IMAGE": BASE_IMAGES[self.target_architecture],
            "POETRY_VERSION": POETRY_VERSIONS[self.target_architecture],
        }

        image: Image = self.docker_client.images.build(
            path=str(self.dockerfile_directory),
            dockerfile=self.dockerfile_name,
            tag=f"{self.image_name}:{self.image_tag}",
            buildargs=buildargs,
        )[0]
        return image
