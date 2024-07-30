import platform

from rich import print

from eli.genyai import model
from eli.genyai.schema import OperatingSystem


class Genai:
    def __init__(self):
        self.operating_system = platform.system().lower()
        self.system = OperatingSystem(os=self.operating_system)

    def get_command(self, query: str):
        response = model.generate_content(f"No yapping. {query} on {self.system.os}. Do not explain it.")
        print(response.text)


genyai = Genai()
