from pathlib import Path
import typer
from prefect import flow, get_run_logger, serve

app = typer.Typer()


@flow
def flow_main(arg1: str, arg2: str) -> None:
    log = get_run_logger()
    log.info("I got args %s %s", arg1, arg2)
    return


@app.command()
def main(
    arg1: str = typer.Option("arg1_value"), arg2: str = typer.Option("arg1_value")
):
    path = Path(__file__)
    flow_main.from_source(
        source=str(path.parent.resolve()),
        entrypoint=f"{path.name}:flow_main",
    ).serve(
        name="a-silly-flow",
        version="1.2.3",
        parameters={
            "arg1": arg1,
            "arg2": arg2,
        },
    )
