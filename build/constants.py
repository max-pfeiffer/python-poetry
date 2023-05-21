PYTHON_POETRY_IMAGE_NAME: str = "pfeiffermax/python-poetry"
TARGET_ARCHITECTURES: list[str] = [
    "poetry1.3.2-python3.9.16-bullseye",
    "poetry1.3.2-python3.9.16-slim-bullseye",
    "poetry1.3.2-python3.10.11-bullseye",
    "poetry1.3.2-python3.10.11-slim-bullseye",
    "poetry1.3.2-python3.11.3-bullseye",
    "poetry1.3.2-python3.11.3-slim-bullseye",
    "poetry1.4.2-python3.9.16-bullseye",
    "poetry1.4.2-python3.9.16-slim-bullseye",
    "poetry1.4.2-python3.10.11-bullseye",
    "poetry1.4.2-python3.10.11-slim-bullseye",
    "poetry1.4.2-python3.11.3-bullseye",
    "poetry1.4.2-python3.11.3-slim-bullseye",
    "poetry1.5.0-python3.9.16-bullseye",
    "poetry1.5.0-python3.9.16-slim-bullseye",
    "poetry1.5.0-python3.10.11-bullseye",
    "poetry1.5.0-python3.10.11-slim-bullseye",
    "poetry1.5.0-python3.11.3-bullseye",
    "poetry1.5.0-python3.11.3-slim-bullseye",
]
BASE_IMAGES: dict = {
    TARGET_ARCHITECTURES[
        0
    ]: "python:3.9.16-bullseye@sha256:b8ddeb68904299c09a39aff59d4a713862253b137fdd7ace3a3b7ba0391971b1",
    TARGET_ARCHITECTURES[
        1
    ]: "python:3.9.16-slim-bullseye@sha256:9e0b4391fc41bc35c16caef4740736b6b349f6626fd14eba32793ae3c7b01908",
    TARGET_ARCHITECTURES[
        2
    ]: "python:3.10.11-bullseye@sha256:7f8f3cf6668c563e44a2285ce2eca9f8b82f96038449f07183126c95979f7d21",
    TARGET_ARCHITECTURES[
        3
    ]: "python:3.10.11-slim-bullseye@sha256:12af6fa557c55d85754107e59d0e21530d7a253757e128b3682d138e58712e54",
    TARGET_ARCHITECTURES[
        4
    ]: "python:3.11.3-bullseye@sha256:89cbc1829d74f72436c96302c49218291eb464705c726cc27d71c32fec1d9082",
    TARGET_ARCHITECTURES[
        5
    ]: "python:3.11.3-slim-bullseye@sha256:551c9529e77896518ac5693d7e98ee5e12051d625de450ac2a68da1eae15ec87",
    TARGET_ARCHITECTURES[
        6
    ]: "python:3.9.16-bullseye@sha256:b8ddeb68904299c09a39aff59d4a713862253b137fdd7ace3a3b7ba0391971b1",
    TARGET_ARCHITECTURES[
        7
    ]: "python:3.9.16-slim-bullseye@sha256:9e0b4391fc41bc35c16caef4740736b6b349f6626fd14eba32793ae3c7b01908",
    TARGET_ARCHITECTURES[
        8
    ]: "python:3.10.11-bullseye@sha256:7f8f3cf6668c563e44a2285ce2eca9f8b82f96038449f07183126c95979f7d21",
    TARGET_ARCHITECTURES[
        9
    ]: "python:3.10.11-slim-bullseye@sha256:12af6fa557c55d85754107e59d0e21530d7a253757e128b3682d138e58712e54",
    TARGET_ARCHITECTURES[
        10
    ]: "python:3.11.3-bullseye@sha256:89cbc1829d74f72436c96302c49218291eb464705c726cc27d71c32fec1d9082",
    TARGET_ARCHITECTURES[
        11
    ]: "python:3.11.3-slim-bullseye@sha256:551c9529e77896518ac5693d7e98ee5e12051d625de450ac2a68da1eae15ec87",
    TARGET_ARCHITECTURES[
        12
    ]: "python:3.9.16-bullseye@sha256:b8ddeb68904299c09a39aff59d4a713862253b137fdd7ace3a3b7ba0391971b1",
    TARGET_ARCHITECTURES[
        13
    ]: "python:3.9.16-slim-bullseye@sha256:9e0b4391fc41bc35c16caef4740736b6b349f6626fd14eba32793ae3c7b01908",
    TARGET_ARCHITECTURES[
        14
    ]: "python:3.10.11-bullseye@sha256:7f8f3cf6668c563e44a2285ce2eca9f8b82f96038449f07183126c95979f7d21",
    TARGET_ARCHITECTURES[
        15
    ]: "python:3.10.11-slim-bullseye@sha256:12af6fa557c55d85754107e59d0e21530d7a253757e128b3682d138e58712e54",
    TARGET_ARCHITECTURES[
        16
    ]: "python:3.11.3-bullseye@sha256:89cbc1829d74f72436c96302c49218291eb464705c726cc27d71c32fec1d9082",
    TARGET_ARCHITECTURES[
        17
    ]: "python:3.11.3-slim-bullseye@sha256:551c9529e77896518ac5693d7e98ee5e12051d625de450ac2a68da1eae15ec87",
}
PYTHON_VERSIONS: dict = {
    TARGET_ARCHITECTURES[0]: "3.9.16",
    TARGET_ARCHITECTURES[1]: "3.9.16",
    TARGET_ARCHITECTURES[2]: "3.10.11",
    TARGET_ARCHITECTURES[3]: "3.10.11",
    TARGET_ARCHITECTURES[4]: "3.11.3",
    TARGET_ARCHITECTURES[5]: "3.11.3",
    TARGET_ARCHITECTURES[6]: "3.9.16",
    TARGET_ARCHITECTURES[7]: "3.9.16",
    TARGET_ARCHITECTURES[8]: "3.10.11",
    TARGET_ARCHITECTURES[9]: "3.10.11",
    TARGET_ARCHITECTURES[10]: "3.11.3",
    TARGET_ARCHITECTURES[11]: "3.11.3",
    TARGET_ARCHITECTURES[12]: "3.9.16",
    TARGET_ARCHITECTURES[13]: "3.9.16",
    TARGET_ARCHITECTURES[14]: "3.10.11",
    TARGET_ARCHITECTURES[15]: "3.10.11",
    TARGET_ARCHITECTURES[16]: "3.11.3",
    TARGET_ARCHITECTURES[17]: "3.11.3",
}
POETRY_VERSIONS: dict = {
    TARGET_ARCHITECTURES[0]: "1.3.2",
    TARGET_ARCHITECTURES[1]: "1.3.2",
    TARGET_ARCHITECTURES[2]: "1.3.2",
    TARGET_ARCHITECTURES[3]: "1.3.2",
    TARGET_ARCHITECTURES[4]: "1.3.2",
    TARGET_ARCHITECTURES[5]: "1.3.2",
    TARGET_ARCHITECTURES[6]: "1.4.2",
    TARGET_ARCHITECTURES[7]: "1.4.2",
    TARGET_ARCHITECTURES[8]: "1.4.2",
    TARGET_ARCHITECTURES[9]: "1.4.2",
    TARGET_ARCHITECTURES[10]: "1.4.2",
    TARGET_ARCHITECTURES[11]: "1.4.2",
    TARGET_ARCHITECTURES[12]: "1.5.0",
    TARGET_ARCHITECTURES[13]: "1.5.0",
    TARGET_ARCHITECTURES[14]: "1.5.0",
    TARGET_ARCHITECTURES[15]: "1.5.0",
    TARGET_ARCHITECTURES[16]: "1.5.0",
    TARGET_ARCHITECTURES[17]: "1.5.0",
}
