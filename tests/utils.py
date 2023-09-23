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
