import os
import sys
import tomllib
from typing import List

class Data:
    projDir:str = os.path.dirname (
        os.path.dirname (
            os.path.dirname (
                os.path.abspath(sys.argv[0])
            )
        )
    )

    libDir:str = ""
    libLinks:List[str] = []

    @staticmethod
    def init() -> bool:
        tomlPath:str = f"{Data.projDir}/third/config.toml"
        if not (os.path.exists(tomlPath)): return False

        with open(tomlPath, "rb") as file:
            data:dict = tomllib.load(file)

            Data.libDir = data["libDir"]
            Data.libLinks = data["libLinks"]

        return True