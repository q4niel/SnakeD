import os
import sys
import shutil
from data import Data
import dmd

def main() -> None:
    Data.init()

    if (os.path.exists(f"{Data.projDir}/{Data.outDir}")):
        shutil.rmtree(f"{Data.projDir}/{Data.outDir}")

    os.makedirs(f"{Data.projDir}/{Data.outDir}")

    builder:dmd.Builder = dmd.Builder()
    if not builder.isValid: return
    (
        builder
            .setName(f"{Data.binName}-{Data.Version.major}.{Data.Version.minor}.{Data.Version.patch}")
            .setSrcDir(f"{Data.projDir}/{Data.srcDir}")
            .setOutDir(f"{Data.projDir}/{Data.outDir}")
            .setLibDir(f"{Data.projDir}/{Data.libDir}")
    )
    
    for src in Data.binSources:
        builder.addSource(src)

    for lib in Data.binStatics:
        builder.addStatic(lib)

    builder.build()

    for src in Data.binSources:
        os.remove(f"{Data.projDir}/{Data.outDir}/{src}.o")

    if (2 <= len(sys.argv) and "run" == sys.argv[1]):
        os.system("clear")
        os.system(f"{Data.projDir}/{Data.outDir}/{Data.binName}-{Data.Version.major}.{Data.Version.minor}.{Data.Version.patch}")
        shutil.rmtree(f"{Data.projDir}/{Data.outDir}")

    return

if __name__ == "__main__": main()