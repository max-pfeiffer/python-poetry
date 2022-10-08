PYTHON_POETRY_IMAGE_NAME: str = "pfeiffermax/python-poetry"
TARGET_ARCHITECTURES: list[str] = [
    "python3.9.14-bullseye-poetry1.2.1",
    "python3.9.14-slim-bullseye-poetry1.2.1",
    "python3.10.7-bullseye-poetry1.2.1",
    "python3.10.7-slim-bullseye-poetry1.2.1",
]
BASE_IMAGES: dict = {
    TARGET_ARCHITECTURES[0]: "python:3.9.14-bullseye",
    TARGET_ARCHITECTURES[1]: "python:3.9.14-slim-bullseye",
    TARGET_ARCHITECTURES[2]: "python:3.10.7-bullseye",
    TARGET_ARCHITECTURES[3]: "python:3.10.7-slim-bullseye",
}
PYTHON_VERSIONS: dict = {
    TARGET_ARCHITECTURES[0]: "3.9.14",
    TARGET_ARCHITECTURES[1]: "3.9.14",
    TARGET_ARCHITECTURES[2]: "3.10.7",
    TARGET_ARCHITECTURES[3]: "3.10.7",
}
POETRY_VERSIONS: dict = {
    TARGET_ARCHITECTURES[0]: "1.2.1",
    TARGET_ARCHITECTURES[1]: "1.2.1",
    TARGET_ARCHITECTURES[2]: "1.2.1",
    TARGET_ARCHITECTURES[3]: "1.2.1",
}
