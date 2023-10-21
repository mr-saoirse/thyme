#!/usr/local/bin/python3
import typer
import typing
import pandas as pd
from thyme import logger
from thyme.ai.agent import build_namespace
from thyme.ops import namespace_path, GitContext

app = typer.Typer()

namespace_app = typer.Typer()
app.add_typer(namespace_app, name="ns")

git_app = typer.Typer()
app.add_typer(git_app, name="git")


@git_app.command("changes")
def run_method(
    against_origin: typing.Optional[bool] = typer.Option(False, "--remote", "-r"),
):
    """

    get the local branch changes since commit or the changes from main

    poetry run thyme git changes --remote
    poetry run thyme git changes
    """
    with GitContext() as g:
        logger.info(g.get_changes(against_origin=against_origin))


@git_app.command("push")
def run_method():
    """ """
    with GitContext() as g:
        logger.info(g.push())


@git_app.command("rebase")
def run_method():
    """ """
    with GitContext() as g:
        logger.info(g.refresh_from_main())


@namespace_app.command("build")
def run_method(
    path: str = typer.Option(None, "--path", "-p"),
):
    path = namespace_path(path)

    logger.debug(path)

    build_namespace(path)


if __name__ == "__main__":
    app()
