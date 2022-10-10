PYTHON_POETRY_IMAGE_NAME: str = "pfeiffermax/python-poetry"
TARGET_ARCHITECTURES: list[str] = [
    "poetry1.1.15-python3.9.14-bullseye",
    "poetry1.1.15-python3.9.14-slim-bullseye",
    "poetry1.1.15-python3.10.7-bullseye",
    "poetry1.1.15-python3.10.7-slim-bullseye",
    "poetry1.2.2-python3.9.14-bullseye",
    "poetry1.2.2-python3.9.14-slim-bullseye",
    "poetry1.2.2-python3.10.7-bullseye",
    "poetry1.2.2-python3.10.7-slim-bullseye",
]
BASE_IMAGES: dict = {
    TARGET_ARCHITECTURES[0]: "python:3.9.14-bullseye",
    TARGET_ARCHITECTURES[1]: "python:3.9.14-slim-bullseye",
    TARGET_ARCHITECTURES[2]: "python:3.10.7-bullseye",
    TARGET_ARCHITECTURES[3]: "python:3.10.7-slim-bullseye",
    TARGET_ARCHITECTURES[4]: "python:3.9.14-bullseye",
    TARGET_ARCHITECTURES[5]: "python:3.9.14-slim-bullseye",
    TARGET_ARCHITECTURES[6]: "python:3.10.7-bullseye",
    TARGET_ARCHITECTURES[7]: "python:3.10.7-slim-bullseye",
}
PYTHON_VERSIONS: dict = {
    TARGET_ARCHITECTURES[0]: "3.9.14",
    TARGET_ARCHITECTURES[1]: "3.9.14",
    TARGET_ARCHITECTURES[2]: "3.10.7",
    TARGET_ARCHITECTURES[3]: "3.10.7",
    TARGET_ARCHITECTURES[4]: "3.9.14",
    TARGET_ARCHITECTURES[5]: "3.9.14",
    TARGET_ARCHITECTURES[6]: "3.10.7",
    TARGET_ARCHITECTURES[7]: "3.10.7",
}
POETRY_VERSIONS: dict = {
    TARGET_ARCHITECTURES[0]: "1.1.15",
    TARGET_ARCHITECTURES[1]: "1.1.15",
    TARGET_ARCHITECTURES[2]: "1.1.15",
    TARGET_ARCHITECTURES[3]: "1.1.15",
    TARGET_ARCHITECTURES[4]: "1.2.2",
    TARGET_ARCHITECTURES[5]: "1.2.2",
    TARGET_ARCHITECTURES[6]: "1.2.2",
    TARGET_ARCHITECTURES[7]: "1.2.2",
}
