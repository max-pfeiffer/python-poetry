from dataclasses import dataclass

from docker_image import reference
from python_on_whales import DockerClient
from pathlib import Path


@dataclass
class ImageTagComponents:
    registry: str
    image_name: str
    tag: str
    version: str
    target_architecture: str
    poetry_version: str
    python_version: str

    @classmethod
    def create_from_reference(cls, tag: str):
        ref = reference.Reference.parse(tag)
        registry: str = ref.repository["domain"]
        image_name: str = ref.repository["path"]
        tag: str = ref["tag"]

        tag_parts: list[str] = tag.split("-")
        target_architecture_index = [
            index
            for index, tag_part in enumerate(tag_parts)
            if tag_part.startswith("poetry")
        ][0]
        python_version_index = [
            index
            for index, tag_part in enumerate(tag_parts)
            if tag_part.startswith("python")
        ][0]

        version: str = "-".join(tag_parts[:target_architecture_index])
        target_architecture: str = "-".join(
            tag_parts[target_architecture_index:]
        )
        poetry_version: str = tag_parts[target_architecture_index].lstrip(
            "poetry"
        )
        python_version: str = tag_parts[python_version_index].lstrip("python")
        return cls(
            registry=registry,
            image_name=image_name,
            tag=tag,
            version=version,
            target_architecture=target_architecture,
            poetry_version=poetry_version,
            python_version=python_version,
        )


def create_version_tag_for_example_images(version: str, target: str) -> str:
    version_tag: str = f"{version}-{target}"
    return version_tag


def extract_image_references_from_build_config(build_config: dict) -> list[str]:
    image_tags: list[str] = []
    targets: dict = build_config["target"]
    for value in targets.values():
        image_tags.extend(value["tags"])
    return image_tags


def generate_image_references(
    bake_file: Path, context: Path, version: str
) -> list[str]:
    pow_docker_client: DockerClient = DockerClient()
    build_config: dict = pow_docker_client.buildx.bake(
        targets=["python-poetry"],
        files=[bake_file],
        variables=dict(
            REGISTRY="localhost:5000",
            CONTEXT=str(context),
            IMAGE_VERSION=version,
        ),
        print=True,
    )
    images_tags = extract_image_references_from_build_config(build_config)
    return images_tags
