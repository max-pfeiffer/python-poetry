from dataclasses import dataclass


@dataclass
class ImageTagComponents:
    image_name: str
    version: str
    target_architecture: str

    @classmethod
    def create_from_tag(cls, tag: str):
        tag_parts: list[str] = tag.split(":")
        image_name: str = tag_parts[0]
        image_tag: str = tag_parts[1]

        image_tag_parts: list[str] = image_tag.split("-")
        target_architecture_index = [
            index
            for index, tag_part in enumerate(image_tag_parts)
            if tag_part.startswith("python")
        ][0]

        version: str = "-".join(image_tag_parts[:target_architecture_index])
        target_architecture: str = "-".join(
            image_tag_parts[target_architecture_index:]
        )
        return cls(
            image_name=image_name,
            version=version,
            target_architecture=target_architecture,
        )


def create_version_tag_for_example_images(version: str, target: str) -> str:
    version_tag: str = f"{version}-{target}"
    return version_tag
