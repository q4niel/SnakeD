import os
import sys
import shutil
from data import Data
import dmd

def main() -> None:
    if not Data.init():
        print("Data initialization failed")
        return

    if (os.path.exists(f"{Data.projDir}/{Data.outDir}")):
        shutil.rmtree(f"{Data.projDir}/{Data.outDir}")

    os.makedirs(f"{Data.projDir}/{Data.outDir}")

    builder:dmd.Builder = dmd.Builder()
    if not builder.isValid: return
    (
        builder
            .setName(f"{Data.binName}")
            .setOutDir(f"{Data.projDir}/{Data.outDir}")
            .setSrcDir(f"{Data.projDir}/{Data.srcDir}")
            .setLibDir(f"{Data.projDir}/{Data.libDir}")
            .setGlueDir(f"{Data.projDir}/{Data.glueDir}")
    )
    
    for src in Data.binSources:
        builder.addSource(src)

    for lib in Data.libs:
        builder.addLib(lib)

    builder.build()

    for src in Data.binSources:
        os.remove(f"{Data.projDir}/{Data.outDir}/{src}.o")

    if (2 <= len(sys.argv) and "run" == sys.argv[1]):
        os.system("clear")
        os.system(f"{Data.projDir}/{Data.outDir}/{Data.binName}")
        shutil.rmtree(f"{Data.projDir}/{Data.outDir}")

    return

if __name__ == "__main__": main()