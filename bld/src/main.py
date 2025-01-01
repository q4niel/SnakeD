import os
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
    )
    
    for src in Data.binSources:
        builder.addSource(src)
    builder.build()

    for src in Data.binSources:
        os.remove(f"{Data.projDir}/{Data.outDir}/{src}.o")

    return

if __name__ == "__main__": main()