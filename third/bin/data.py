import os
import sys
import tomllib
from typing import List, TypedDict
from enum import Enum, auto

class OS(Enum):
    OTHER = auto()
    LINUX = auto()
    WINDOWS = auto()

class Data:
    class LibsEntry(TypedDict):
        name:str
        linux:str
        windows:str

    projDir:str = os.path.dirname (
        os.path.dirname (
            os.path.dirname (
                os.path.abspath(sys.argv[0])
            )
        )
    )
    os:OS = OS.OTHER

    libDir:str = ""
    libs:List[LibsEntry] = []

    @staticmethod
    def init() -> bool:
        match os.name:
            case "posix":
                Data.os = OS.LINUX
            case "nt":
                Data.os = OS.WINDOWS
            case _:
                print("Unsupported OS")
                return False

        tomlPath:str = f"{Data.projDir}/third/install.toml"
        if not (os.path.exists(tomlPath)): return False

        with open(tomlPath, "rb") as file:
            data:dict = tomllib.load(file)

            Data.libDir = data["libDir"]
            Data.libs = data["libs"]

        return True