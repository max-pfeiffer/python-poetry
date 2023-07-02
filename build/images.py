from pathlib import Path
from typing import Optional

from python_on_whales import DockerClient, Builder, Image
from build.constants import (
    PLATFORMS,
    PYTHON_POETRY_IMAGE_NAME,
    BASE_IMAGES,
    POETRY_VERSIONS,
)


class DockerImage:
    def __init__(
        self,
        docker_client: DockerClient,
        builder: Builder,
        target_architecture: str,
        version: str,
    ):
        self.docker_client: DockerClient = docker_client
        self.builder: Builder = builder
        self.dockerfile_name: str = "Dockerfile"
        self.image_name: Optional[str] = None
        self.image_tag: Optional[str] = None
        self.version: Optional[str] = version
        self.target_architecture: str = target_architecture


class PythonPoetryImage(DockerImage):
    def __init__(
        self,
        docker_client: DockerClient,
        builder: Builder,
        target_architecture: str,
        version: str,
    ):
        super().__init__(docker_client, builder, target_architecture, version)
        self.dockerfile_directory: Path = Path(__file__).parent.resolve()

        # An image name is made up of slash-separated name components, optionally prefixed by a registry hostname.
        # see: https://docs.docker.com/engine/reference/commandline/tag/
        self.image_name = PYTHON_POETRY_IMAGE_NAME

    def build(self) -> Optional[Image]:
        self.image_tag = f"{self.version}-{self.target_architecture}"

        buildargs: dict[str, str] = {
            "OFFICIAL_PYTHON_IMAGE": BASE_IMAGES[self.target_architecture],
            "POETRY_VERSION": POETRY_VERSIONS[self.target_architecture],
        }

        # image: Image = self.docker_client.images.build(
        #     path=str(self.dockerfile_directory),
        #     dockerfile=self.dockerfile_name,
        #     tag=f"{self.image_name}:{self.image_tag}",
        #     buildargs=buildargs,
        # )[0]

        image: Image = self.docker_client.buildx.build(
            context_path=str(self.dockerfile_directory),
            tags=f"{self.image_name}:{self.image_tag}",
            build_args=buildargs,
            platforms=PLATFORMS,
            builder=self.builder,
        )

        return image
