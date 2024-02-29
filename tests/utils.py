from dataclasses import dataclass
from pathlib import Path

from docker_image import reference
from python_on_whales import DockerClient


@dataclass
class ImageTagComponents:
    registry: str
    image_name: str
    tag: str
    version: str
    poetry_version: str
    python_version: str
    os_variant: str

    @classmethod
    def create_from_reference(cls, tag: str):
        ref = reference.Reference.parse(tag)
        registry: str = ref.repository["domain"]
        image_name: str = ref.repository["path"]
        tag: str = ref["tag"]

        tag_parts: list[str] = tag.split("-")
        version: str = tag_parts[0]
        poetry_version: str = tag_parts[1].lstrip("poetry")
        python_version: str = tag_parts[2].lstrip("python")
        os_variant: str = "-".join(tag_parts[2:])
        return cls(
            registry=registry,
            image_name=image_name,
            tag=tag,
            version=version,
            poetry_version=poetry_version,
            python_version=python_version,
            os_variant=os_variant,
        )
