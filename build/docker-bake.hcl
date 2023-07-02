variable "REGISTRY" {
  default = null
}

variable "IMAGE_VERSION" {
  default = null
}

variable "IMAGE_NAME" {
  default = "pfeiffermax/python-poetry"
}

variable "CONTEXT" {
  default = "."
}

target "python-poetry" {  
  name = "poetry${replace(poetry_version, ".", "-")}-python${replace(python_version, ".", "-")}-${os_variant}"
  context = CONTEXT

  matrix = {
    python_version = ["3.9.16", "3.10.11", "3.11.3"]
    os_variant = ["bullseye", "slim-bullseye"]
    poetry_version = ["1.3.2", "1.4.2", "1.5.1"]
  }
  
  args = {
    POETRY_VERSION = poetry_version
    OFFICIAL_PYTHON_IMAGE = "python:${python_version}-${os_variant}"
  }

  platforms = ["linux/amd64", "linux/arm64"]

  tags = ["${REGISTRY}/${IMAGE_NAME}:${IMAGE_VERSION}-poetry${poetry_version}-python${python_version}-${os_variant}"]
}