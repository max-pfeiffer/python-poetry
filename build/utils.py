from pathlib import Path
from python_on_whales import DockerClient


def get_context() -> Path:
    return Path(__file__).parent.resolve()


def get_docker_bake_file() -> Path:
    docker_bake_file: Path = Path(__file__).parent.resolve() / "docker-bake.hcl"
    return docker_bake_file


def extract_image_tags_from_build_config(build_config: dict) -> list[str]:
    image_tags: list[str] = []
    targets: dict = build_config["target"]
    for value in targets.values():
        image_tags.extend(value["tags"])
    return image_tags


def generate_image_tags(
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
    images_tags = extract_image_tags_from_build_config(build_config)
    return images_tags
