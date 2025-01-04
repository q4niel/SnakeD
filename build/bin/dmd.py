import os
from typing import List, Self
from data import Data

def compile(filename:str, srcDir:str, outDir:str) -> bool:
    return (0 == os.system(f"dmd -c {srcDir}/{filename}.d -of{outDir}/{filename}.o"))

def link(outPath:str, libPath:str, name:str, sources:List[str], libs:List[Data.LibsEntry]) -> bool:
    appendedSources:str = ""
    for src in sources:
        appendedSources += f"{outPath}/{src}.o "

    appendedGlues:str = ""
    appendedLibs:str = ""
    for lib in libs:
        appendedGlues += f"{Data.glueDir}/{lib["glue"]} "
        appendedLibs += f"-L{libPath}/{lib["linux"]} "

    return (0 == os.system(f"dmd {appendedSources} {appendedGlues} {appendedLibs} -of{outPath}/{name}"))

class Builder:
    def __init__(self) -> None:
        self.isValid:bool = (0 == os.system("dmd --version"))

        self.name:str = ""
        self.outDir:str = ""

        self.srcDir:str = ""
        self.sources:List[str] = []

        self.libDir:str = ""
        self.glueDir:str = ""
        self.libs:List[Data.LibsEntry] = []
        return

    def setName(self, name:str) -> Self:
        self.name = name
        return self

    def setOutDir(self, path:str) -> Self:
        self.outDir = path
        return self

    def setSrcDir(self, path:str) -> Self:
        self.srcDir = path
        return self

    def addSource(self, file:str) -> Self:
        self.sources.append(file)
        return self

    def setLibDir(self, path:str) -> Self:
        self.libDir = path
        return self

    def setGlueDir(self, path:str) -> Self:
        self.glueDir = path
        return self

    def addLib(self, lib:Data.LibsEntry) -> Self:
        self.libs.append(lib)
        return self

    def build(self) -> bool:
        for src in self.sources:
            if not compile(src, self.srcDir, self.outDir):
                return False

        return link(self.outDir, self.libDir, self.name, self.sources, self.libs)