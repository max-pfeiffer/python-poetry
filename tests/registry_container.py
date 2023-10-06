import tarfile
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Optional

import bcrypt
from testcontainers.core.container import DockerContainer
from testcontainers.core.utils import setup_logger

logger = setup_logger(__name__)


class DockerRegistryContainer(DockerContainer):
    # https://docs.docker.com/registry/
    def __init__(
        self,
        image: str = "registry:latest",
        port: int = 5000,
        username: str = None,
        password: str = None,
        **kwargs,
    ) -> None:
        super().__init__(image=image, **kwargs)
        self.port = port
        self.username: Optional[str] = username
        self.password: Optional[str] = password
        self.with_exposed_ports(self.port)

    def start(self):
        if self.username and self.password:
            # Create password and password file contents
            hashed_password: str = bcrypt.hashpw(
                self.password.encode("utf-8"),
                bcrypt.gensalt(rounds=12, prefix=b"2a"),
            ).decode("utf-8")
            content = f"{self.username}:{hashed_password}"

            # Write password file to container and start it
            with TemporaryDirectory() as tmp_dir:
                tmp_htpasswd_file: Path = Path(tmp_dir) / "credentials.txt"
                tmp_tarfile: Path = Path(tmp_dir) / "htpasswd.tar"
                container_path: str = f"/htpasswd/{tmp_htpasswd_file.name}"

                tmp_htpasswd_file.write_text(content)

                with tarfile.open(tmp_tarfile, "w") as htpasswd_tarfile:
                    htpasswd_tarfile.add(
                        tmp_htpasswd_file, arcname=container_path
                    )

                self.with_env("REGISTRY_AUTH_HTPASSWD_REALM", "local-registry")
                self.with_env("REGISTRY_AUTH_HTPASSWD_PATH", container_path)

                logger.info("Pulling image %s", self.image)
                docker_client = self.get_docker_client()
                self._container = docker_client.client.containers.create(
                    self.image,
                    command=self._command,
                    detach=True,
                    environment=self.env,
                    ports=self.ports,
                    name=self._name,
                    volumes=self.volumes,
                    **self._kwargs,
                )
                with open(tmp_tarfile, "r") as data_stream:
                    self._container.put_archive("/", data_stream)

                self._container.start()
                logger.info("Container started: %s", self._container.short_id)
                return self
        else:
            super().start()
            return self

    def get_registry(self) -> str:
        host: str = self.get_container_host_ip()
        port: str = self.get_exposed_port(self.port)
        return f"{host}:{port}"
