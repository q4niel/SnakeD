import os
import shutil
from data import Data
import link

def main() -> None:
    if not Data.init():
        print("Data initialization failed")
        return

    if (os.path.exists(f"{Data.projDir}/{Data.libDir}")):
        shutil.rmtree(f"{Data.projDir}/{Data.libDir}")

    os.makedirs(f"{Data.projDir}/{Data.libDir}")

    for lib in Data.libs:
        link.get(lib)

    return

if __name__ == "__main__": main()