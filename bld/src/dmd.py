import os
from typing import List, Self

def compile(filename:str, srcDir:str, outDir:str) -> bool:
    return (0 == os.system(f"dmd -c {srcDir}/{filename}.d -of{outDir}/{filename}.o"))

def link(outPath:str, name:str, srcs:List[str]) -> bool:
    appended:str = ""

    for src in srcs:
        appended += f"{outPath}/{src}.o "

    return (0 == os.system(f"dmd {appended} -of{outPath}/{name}"))

class Builder:
    def __init__(self) -> None:
        self.isValid:bool = (0 == os.system("dmd --version"))
        self.name:str = ""
        self.srcDir:str = ""
        self.outDir:str = ""
        self.srcs:List[str] = []
        return

    def setName(self, name:str) -> Self:
        self.name = name
        return self

    def setSrcDir(self, path:str) -> Self:
        self.srcDir = path
        return self

    def setOutDir(self, path:str) -> Self:
        self.outDir = path
        return self

    def addSource(self, file:str) -> Self:
        self.srcs.append(file)
        return self

    def build(self) -> bool:
        for src in self.srcs:
            if not compile(src, self.srcDir, self.outDir):
                return False

        return link(self.outDir, self.name, self.srcs)