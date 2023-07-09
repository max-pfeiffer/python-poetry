from pathlib import Path


def get_context() -> Path:
    return Path(__file__).parent.resolve()


def get_docker_bake_file() -> Path:
    docker_bake_file: Path = Path(__file__).parent.resolve() / "docker-bake.hcl"
    return docker_bake_file
