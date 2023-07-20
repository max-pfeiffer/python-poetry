import click

from build.utils import get_docker_bake_file, get_context
from pathlib import Path
from python_on_whales import DockerClient, Builder


@click.command()
@click.option(
    "--docker-hub-username",
    envvar="DOCKER_HUB_USERNAME",
    help="Docker Hub username",
)
@click.option(
    "--docker-hub-password",
    envvar="DOCKER_HUB_PASSWORD",
    help="Docker Hub password",
)
@click.option(
    "--version-tag", envvar="GIT_TAG_NAME", required=True, help="Version Tag"
)
@click.option("--registry", envvar="REGISTRY", help="Docker registry")
def main(
    docker_hub_username: str,
    docker_hub_password: str,
    version_tag: str,
    registry: str,
) -> None:
    context: Path = get_context()
    bake_file: Path = get_docker_bake_file()
    variables: dict = {
        "CONTEXT": str(context),
        "IMAGE_VERSION": version_tag,
    }
    if registry:
        variables["REGISTRY"] = registry

    docker_client: DockerClient = DockerClient()
    builder: Builder = docker_client.buildx.create(
        driver="docker-container", driver_options=dict(network="host")
    )

    docker_client.login(
        server=registry,
        username=docker_hub_username,
        password=docker_hub_password,
    )
    build_config: dict = docker_client.buildx.bake(
        targets=["python-poetry"],
        builder=builder,
        files=[bake_file],
        # set={"*.cache-to": '"type=gha,mode=max"', "*.cache-from": '"type=gha"'},
        set={"*.cache-to": '"type=gha"', "*.cache-from": '"type=gha"'},
        variables=variables,
        push=True,
    )
    print(build_config)

    # Cleanup
    docker_client.buildx.stop(builder)
    docker_client.buildx.remove(builder)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
