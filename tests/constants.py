from pathlib import Path
from random import randrange

from semver import VersionInfo

from build.utils import get_context, get_docker_bake_file
from tests.utils import generate_image_references

SLEEP_TIME: float = 3.0
REGISTRY_USERNAME: str = "foo"
REGISTRY_PASSWORD: str = "bar"
VERSION: str = str(
    VersionInfo(
        major=randrange(100), minor=randrange(100), patch=randrange(100)
    )
)
BAKE_FILE: Path = get_docker_bake_file()
CONTEXT: Path = get_context()
IMAGE_REFERENCES: list[str] = generate_image_references(
    BAKE_FILE, CONTEXT, VERSION
)
