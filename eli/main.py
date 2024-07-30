import typer

from eli.genyai.genai import genyai

eli = typer.Typer()


@eli.callback()
def callback() -> None:
    pass


@eli.command("//")
def help(query: str) -> None:
    genyai.get_command(query)


@eli.command("")
def main():
    eli()
