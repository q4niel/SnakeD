import os
from typing import List, Self

def compile(filename:str, srcDir:str, outDir:str) -> bool:
    return (0 == os.system(f"dmd -c {srcDir}/{filename}.d -of{outDir}/{filename}.o"))

def link(outPath:str, libPath:str, name:str, sources:List[str], statics:List[str]) -> bool:
    allSources:str = ""
    for src in sources:
        allSources += f"{outPath}/{src}.o "
    
    allStatics:str = ""
    for lib in statics:
        allStatics += f"-L{libPath}/{lib}.a "

    return (0 == os.system(f"dmd {allSources} {allStatics} -of{outPath}/{name}"))

class Builder:
    def __init__(self) -> None:
        self.isValid:bool = (0 == os.system("dmd --version"))
        self.name:str = ""
        self.srcDir:str = ""
        self.outDir:str = ""
        self.libDir:str = ""
        self.sources:List[str] = []
        self.statics:List[str] = []
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

    def setLibDir(self, path:str) -> Self:
        self.libDir = path
        return self

    def addSource(self, file:str) -> Self:
        self.sources.append(file)
        return self
    
    def addStatic(self, file:str) -> Self:
        self.statics.append(file)
        return self

    def build(self) -> bool:
        for src in self.sources:
            if not compile(src, self.srcDir, self.outDir):
                return False

        return link(self.outDir, self.libDir, self.name, self.sources, self.statics)