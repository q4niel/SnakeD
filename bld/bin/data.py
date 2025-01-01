import os
import sys
import tomllib
from typing import List
from platform import OS

class Data:    
    projDir:str = os.path.dirname (
        os.path.dirname (
            os.path.dirname (
                os.path.abspath(sys.argv[0])
            )
        )
    )
    os:OS = OS.OTHER

    srcDir:str = ""
    outDir:str = ""
    binName:str = ""
    binSources:List[str] = []

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

        tomlPath:str = f"{Data.projDir}/bld/cfg.toml"
        if not (os.path.exists(tomlPath)): return False

        with open(tomlPath, "rb") as file:
            data:dict = tomllib.load(file)

            Data.srcDir = data["srcDir"]
            Data.outDir = data["outDir"]
            Data.binName = data["name"]
            Data.binSources = data["sources"]

            Data.Version.major = data["version"]["major"]
            Data.Version.minor = data["version"]["minor"]
            Data.Version.patch = data["version"]["patch"]

        return True