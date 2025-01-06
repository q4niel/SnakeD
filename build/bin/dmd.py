import os
from typing import List, Self
from data import Data, OS

def compile(filename:str, srcDir:str, outDir:str) -> bool:
    extension:str = ""
    match Data.os:
        case OS.LINUX:
            extension = ".o"
        case OS.WINDOWS:
            extension = ".obj"

    return (0 == os.system(f"dmd -c {srcDir}/{filename}.d -of{outDir}/{filename}{extension}"))

def link(outPath:str, libPath:str, name:str, sources:List[str], libs:List[Data.LibsEntry], flags:List[str] = []) -> bool:
    objectExtension:str = ""
    libType:str = ""
    binExtension:str = ""
    match Data.os:
        case OS.LINUX:
            objectExtension = ".o"
            libType = "linux"
            binExtension = ""
        case OS.WINDOWS:
            objectExtension = ".obj"
            libType = "windows"
            binExtension = ".exe"

    appendedSources:str = ""
    for src in sources:
        appendedSources += f"{outPath}/{src}{objectExtension} "

    appendedGlues:str = ""
    appendedLibs:str = ""
    for lib in libs:
        appendedLibs += f"-L{libPath}/{lib[libType]} "
        for glue in lib["glues"]:
            appendedGlues += f"{Data.glueDir}/{glue} "

    appendedFlags:str = ""
    for flag in flags:
        appendedFlags += f"{flag} "

    return (0 == os.system(f"dmd {appendedSources}{appendedGlues}{appendedLibs}{appendedFlags}-of{outPath}/{name}{binExtension}"))

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

        self.flags:List[str] = []
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

    def addFlags(self, flags:List[str]) -> Self:
        self.flags = flags
        return self

    def build(self) -> bool:
        for src in self.sources:
            if not compile(src, self.srcDir, self.outDir):
                return False

        return link(self.outDir, self.libDir, self.name, self.sources, self.libs, self.flags)