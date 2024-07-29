import typer
from rich import print

eli = typer.Typer()

@eli.callback()
def callback() -> None:
   pass

@eli.command("hi")
def hello(name: str):
    """
    Prints out a parameter

    :param name: str

    :return: None
    """
    print(f"{name=}")

def main():
    eli()
