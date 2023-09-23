from pathlib import Path

from build.utils import get_context, get_docker_bake_file

SLEEP_TIME: float = 3.0
REGISTRY_USERNAME: str = "foo"
REGISTRY_PASSWORD: str = "bar"
BAKE_FILE: Path = get_docker_bake_file()
CONTEXT: Path = get_context()
