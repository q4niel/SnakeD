import os
import shutil
from data import Data
from get import download

def main() -> None:
    Data.init()

    if (os.path.exists(f"{Data.projDir}/{Data.libDir}")):
        shutil.rmtree(f"{Data.projDir}/{Data.libDir}")

    os.makedirs(f"{Data.projDir}/{Data.libDir}")

    for link in Data.libLinks:
        download(link, f"{Data.projDir}/{Data.libDir}")

    return

if __name__ == "__main__": main()