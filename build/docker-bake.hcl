variable "REGISTRY" {
  default = "docker.io"
}

variable "IMAGE_VERSION" {
  default = null
}

variable "CONTEXT" {
  default = "."
}

target "python-poetry" {  
  name = "poetry${replace(poetry_version, ".", "-")}-python${replace(python_version, ".", "-")}-${os_variant}"
  context = CONTEXT

  matrix = {
    #python_version = ["3.9.16", "3.10.11", "3.11.3"]
    #os_variant = ["bullseye", "slim-bullseye"]
    #poetry_version = ["1.3.2", "1.4.2", "1.5.1"]

    python_version = ["3.9.16"]
    os_variant = ["slim-bullseye"]
    poetry_version = ["1.5.1"]
  }
  
  args = {
    POETRY_VERSION = poetry_version
    OFFICIAL_PYTHON_IMAGE = "python:${python_version}-${os_variant}"
  }

  platforms = ["linux/amd64", "linux/arm64"]

  tags = ["${REGISTRY}/pfeiffermax/python-poetry:${IMAGE_VERSION}-poetry${poetry_version}-python${python_version}-${os_variant}"]
}