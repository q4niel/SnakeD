import os
import sys
import tomllib
from typing import List
from enum import Enum, auto

class OS(Enum):
    OTHER = auto()
    LINUX = auto()
    WINDOWS = auto()

class Data:    
    projDir:str = os.path.dirname (
        os.path.dirname (
            os.path.dirname (
                os.path.abspath(sys.argv[0])
            )
        )
    )
    os:OS = OS.OTHER

    binName:str = ""
    outDir:str = ""

    srcDir:str = ""
    binSources:List[str] = []

    libDir:str = ""
    glueDir:str = ""
    libs = []

    class Version:
        major:int = 0
        minor:int = 0
        patch:int = 0

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

        tomlPath:str = f"{Data.projDir}/build/build.toml"
        if not (os.path.exists(tomlPath)): return False

        with open(tomlPath, "rb") as file:
            data:dict = tomllib.load(file)

            Data.binName = data["name"]
            Data.outDir = data["outDir"]

            Data.srcDir = data["srcDir"]
            Data.binSources = data["srcs"]

            Data.libDir = data["libDir"]
            Data.glueDir = data["glueDir"]
            Data.libs = data["libs"]

            Data.Version.major = data["version"]["major"]
            Data.Version.minor = data["version"]["minor"]
            Data.Version.patch = data["version"]["patch"]

        return True