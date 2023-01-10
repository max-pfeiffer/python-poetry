PYTHON_POETRY_IMAGE_NAME: str = "pfeiffermax/python-poetry"
TARGET_ARCHITECTURES: list[str] = [
    "poetry1.1.15-python3.7.16-bullseye",
    "poetry1.1.15-python3.7.16-slim-bullseye",
    "poetry1.1.15-python3.8.16-bullseye",
    "poetry1.1.15-python3.8.16-slim-bullseye",
    "poetry1.1.15-python3.9.16-bullseye",
    "poetry1.1.15-python3.9.16-slim-bullseye",
    "poetry1.1.15-python3.10.9-bullseye",
    "poetry1.1.15-python3.10.9-slim-bullseye",
    "poetry1.2.2-python3.7.16-bullseye",
    "poetry1.2.2-python3.7.16-slim-bullseye",
    "poetry1.2.2-python3.8.16-bullseye",
    "poetry1.2.2-python3.8.16-slim-bullseye",
    "poetry1.2.2-python3.9.16-bullseye",
    "poetry1.2.2-python3.9.16-slim-bullseye",
    "poetry1.2.2-python3.10.9-bullseye",
    "poetry1.2.2-python3.10.9-slim-bullseye",
    "poetry1.3.2-python3.7.16-bullseye",
    "poetry1.3.2-python3.7.16-slim-bullseye",
    "poetry1.3.2-python3.8.16-bullseye",
    "poetry1.3.2-python3.8.16-slim-bullseye",
    "poetry1.3.2-python3.9.16-bullseye",
    "poetry1.3.2-python3.9.16-slim-bullseye",
    "poetry1.3.2-python3.10.9-bullseye",
    "poetry1.3.2-python3.10.9-slim-bullseye",
]
BASE_IMAGES: dict = {
    TARGET_ARCHITECTURES[
        0
    ]: "python:3.7.16-bullseye@sha256:bf85a74f4ace82f3503c2199aaae10e7a8e370bc7e42fd246c5774891f1fab0b",
    TARGET_ARCHITECTURES[
        1
    ]: "python:3.7.16-slim-bullseye@sha256:aa949f5f10e9b28e1f9561fff73d1a359fa8517d4e543451a714d1a4ecc61c56",
    TARGET_ARCHITECTURES[
        2
    ]: "python:3.8.16-bullseye@sha256:3a519327ab069a4e356a8aa279e80b7ef6270e17c5df1493dd0a5b281755e95a",
    TARGET_ARCHITECTURES[
        3
    ]: "python:3.8.16-slim-bullseye@sha256:75b74d058401381b056d00f903dff58262d884025f772ed635a68e9699c36b87",
    TARGET_ARCHITECTURES[
        4
    ]: "python:3.9.16-bullseye@sha256:b8ddeb68904299c09a39aff59d4a713862253b137fdd7ace3a3b7ba0391971b1",
    TARGET_ARCHITECTURES[
        5
    ]: "python:3.9.16-slim-bullseye@sha256:9e0b4391fc41bc35c16caef4740736b6b349f6626fd14eba32793ae3c7b01908",
    TARGET_ARCHITECTURES[
        6
    ]: "python:3.10.9-bullseye@sha256:ec616023dfe571ffc262f28ec23c2f4226b8036d3f2b8475183de9fa6efbd9f4",
    TARGET_ARCHITECTURES[
        7
    ]: "python:3.10.9-slim-bullseye@sha256:e5c7f6da1694b867cc209956f9040e98ae372290f108f7f3d2dc84a331fe2801",
    TARGET_ARCHITECTURES[
        8
    ]: "python:3.7.16-bullseye@sha256:bf85a74f4ace82f3503c2199aaae10e7a8e370bc7e42fd246c5774891f1fab0b",
    TARGET_ARCHITECTURES[
        9
    ]: "python:3.7.16-slim-bullseye@sha256:aa949f5f10e9b28e1f9561fff73d1a359fa8517d4e543451a714d1a4ecc61c56",
    TARGET_ARCHITECTURES[
        10
    ]: "python:3.8.16-bullseye@sha256:3a519327ab069a4e356a8aa279e80b7ef6270e17c5df1493dd0a5b281755e95a",
    TARGET_ARCHITECTURES[
        11
    ]: "python:3.8.16-slim-bullseye@sha256:75b74d058401381b056d00f903dff58262d884025f772ed635a68e9699c36b87",
    TARGET_ARCHITECTURES[
        12
    ]: "python:3.9.16-bullseye@sha256:b8ddeb68904299c09a39aff59d4a713862253b137fdd7ace3a3b7ba0391971b1",
    TARGET_ARCHITECTURES[
        13
    ]: "python:3.9.16-slim-bullseye@sha256:9e0b4391fc41bc35c16caef4740736b6b349f6626fd14eba32793ae3c7b01908",
    TARGET_ARCHITECTURES[
        14
    ]: "python:3.10.9-bullseye@sha256:ec616023dfe571ffc262f28ec23c2f4226b8036d3f2b8475183de9fa6efbd9f4",
    TARGET_ARCHITECTURES[
        15
    ]: "python:3.10.9-slim-bullseye@sha256:e5c7f6da1694b867cc209956f9040e98ae372290f108f7f3d2dc84a331fe2801",
    TARGET_ARCHITECTURES[
        16
    ]: "python:3.7.16-bullseye@sha256:bf85a74f4ace82f3503c2199aaae10e7a8e370bc7e42fd246c5774891f1fab0b",
    TARGET_ARCHITECTURES[
        17
    ]: "python:3.7.16-slim-bullseye@sha256:aa949f5f10e9b28e1f9561fff73d1a359fa8517d4e543451a714d1a4ecc61c56",
    TARGET_ARCHITECTURES[
        18
    ]: "python:3.8.16-bullseye@sha256:3a519327ab069a4e356a8aa279e80b7ef6270e17c5df1493dd0a5b281755e95a",
    TARGET_ARCHITECTURES[
        19
    ]: "python:3.8.16-slim-bullseye@sha256:75b74d058401381b056d00f903dff58262d884025f772ed635a68e9699c36b87",
    TARGET_ARCHITECTURES[
        20
    ]: "python:3.9.16-bullseye@sha256:b8ddeb68904299c09a39aff59d4a713862253b137fdd7ace3a3b7ba0391971b1",
    TARGET_ARCHITECTURES[
        21
    ]: "python:3.9.16-slim-bullseye@sha256:9e0b4391fc41bc35c16caef4740736b6b349f6626fd14eba32793ae3c7b01908",
    TARGET_ARCHITECTURES[
        22
    ]: "python:3.10.9-bullseye@sha256:ec616023dfe571ffc262f28ec23c2f4226b8036d3f2b8475183de9fa6efbd9f4",
    TARGET_ARCHITECTURES[
        23
    ]: "python:3.10.9-slim-bullseye@sha256:e5c7f6da1694b867cc209956f9040e98ae372290f108f7f3d2dc84a331fe2801",
}
PYTHON_VERSIONS: dict = {
    TARGET_ARCHITECTURES[0]: "3.7.16",
    TARGET_ARCHITECTURES[1]: "3.7.16",
    TARGET_ARCHITECTURES[2]: "3.8.16",
    TARGET_ARCHITECTURES[3]: "3.8.16",
    TARGET_ARCHITECTURES[4]: "3.9.16",
    TARGET_ARCHITECTURES[5]: "3.9.16",
    TARGET_ARCHITECTURES[6]: "3.10.9",
    TARGET_ARCHITECTURES[7]: "3.10.9",
    TARGET_ARCHITECTURES[8]: "3.7.16",
    TARGET_ARCHITECTURES[9]: "3.7.16",
    TARGET_ARCHITECTURES[10]: "3.8.16",
    TARGET_ARCHITECTURES[11]: "3.8.16",
    TARGET_ARCHITECTURES[12]: "3.9.16",
    TARGET_ARCHITECTURES[13]: "3.9.16",
    TARGET_ARCHITECTURES[14]: "3.10.9",
    TARGET_ARCHITECTURES[15]: "3.10.9",
    TARGET_ARCHITECTURES[16]: "3.7.16",
    TARGET_ARCHITECTURES[17]: "3.7.16",
    TARGET_ARCHITECTURES[18]: "3.8.16",
    TARGET_ARCHITECTURES[19]: "3.8.16",
    TARGET_ARCHITECTURES[20]: "3.9.16",
    TARGET_ARCHITECTURES[21]: "3.9.16",
    TARGET_ARCHITECTURES[22]: "3.10.9",
    TARGET_ARCHITECTURES[23]: "3.10.9",
}
POETRY_VERSIONS: dict = {
    TARGET_ARCHITECTURES[0]: "1.1.15",
    TARGET_ARCHITECTURES[1]: "1.1.15",
    TARGET_ARCHITECTURES[2]: "1.1.15",
    TARGET_ARCHITECTURES[3]: "1.1.15",
    TARGET_ARCHITECTURES[4]: "1.1.15",
    TARGET_ARCHITECTURES[5]: "1.1.15",
    TARGET_ARCHITECTURES[6]: "1.1.15",
    TARGET_ARCHITECTURES[7]: "1.1.15",
    TARGET_ARCHITECTURES[8]: "1.2.2",
    TARGET_ARCHITECTURES[9]: "1.2.2",
    TARGET_ARCHITECTURES[10]: "1.2.2",
    TARGET_ARCHITECTURES[11]: "1.2.2",
    TARGET_ARCHITECTURES[12]: "1.2.2",
    TARGET_ARCHITECTURES[13]: "1.2.2",
    TARGET_ARCHITECTURES[14]: "1.2.2",
    TARGET_ARCHITECTURES[15]: "1.2.2",
    TARGET_ARCHITECTURES[16]: "1.3.2",
    TARGET_ARCHITECTURES[17]: "1.3.2",
    TARGET_ARCHITECTURES[18]: "1.3.2",
    TARGET_ARCHITECTURES[19]: "1.3.2",
    TARGET_ARCHITECTURES[20]: "1.3.2",
    TARGET_ARCHITECTURES[21]: "1.3.2",
    TARGET_ARCHITECTURES[22]: "1.3.2",
    TARGET_ARCHITECTURES[23]: "1.3.2",
}
