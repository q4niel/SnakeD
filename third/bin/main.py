import os
import shutil
from data import Data
import link

def main() -> None:
    Data.init()

    if (os.path.exists(f"{Data.projDir}/{Data.libDir}")):
        shutil.rmtree(f"{Data.projDir}/{Data.libDir}")

    os.makedirs(f"{Data.projDir}/{Data.libDir}")

    for l in Data.libLinks:
        link.get(l, f"{Data.projDir}/{Data.libDir}", tar=True)

    return

if __name__ == "__main__": main()