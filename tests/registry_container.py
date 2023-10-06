import time
from io import BytesIO
from tarfile import TarFile, TarInfo
from typing import Optional

import bcrypt
from testcontainers.core.container import DockerContainer


class DockerRegistryContainer(DockerContainer):
    # https://docs.docker.com/registry/
    credentials_path: str = "/htpasswd/credentials.txt"

    def __init__(
        self,
        image: str = "registry:latest",
        port: int = 5000,
        username: str = None,
        password: str = None,
        **kwargs,
    ) -> None:
        super().__init__(image=image, **kwargs)
        self.port: int = port
        self.username: Optional[str] = username
        self.password: Optional[str] = password
        self.with_exposed_ports(self.port)

    def _copy_credentials(self):
        # Create credentials and write them to the container
        hashed_password: str = bcrypt.hashpw(
            self.password.encode("utf-8"),
            bcrypt.gensalt(rounds=12, prefix=b"2a"),
        ).decode("utf-8")
        content = f"{self.username}:{hashed_password}".encode("utf-8")

        with BytesIO() as tar_archive_object, TarFile(
            fileobj=tar_archive_object, mode="w"
        ) as tmp_tarfile:
            tarinfo: TarInfo = TarInfo(name=self.credentials_path)
            tarinfo.size = len(content)
            tarinfo.mtime = time.time()

            tmp_tarfile.addfile(tarinfo, BytesIO(content))
            tar_archive_object.seek(0)
            self.get_wrapped_container().put_archive("/", tar_archive_object)

    def start(self):
        if self.username and self.password:
            self.with_env("REGISTRY_AUTH_HTPASSWD_REALM", "local-registry")
            self.with_env("REGISTRY_AUTH_HTPASSWD_PATH", self.credentials_path)
            super().start()
            self._copy_credentials()
            return self
        else:
            super().start()
            return self

    def get_registry(self) -> str:
        host: str = self.get_container_host_ip()
        port: str = self.get_exposed_port(self.port)
        return f"{host}:{port}"
