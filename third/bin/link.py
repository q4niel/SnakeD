import os
import tarfile
import zipfile
import urllib.request
import urllib.parse
import urllib.error
from data import Data, OS

def download(lib:Data.LibsEntry, dstDir:str) -> str:
    url:str = ""
    match Data.os:
        case OS.LINUX:
            url = lib["linux"]
        case OS.WINDOWS:
            url = lib["windows"]

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            if response.status != 200:
                print(f"Failed to download. Status code: {response.status}")
                return ""
    
            filename = os.path.basename(urllib.parse.urlparse(url).path)
            filePath = os.path.join(dstDir, filename)
    
            with open(filePath, "wb") as file:
                while chunk := response.read(1024):
                    file.write(chunk)
    
            print(f"Downloaded {filename} successfully!")
            return filename

    except urllib.error.HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
        return ""

    except urllib.error.URLError as e:
        print(f"URL error occurred: {e.reason}")
        return ""

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""

def untar(file:str, dir:str) -> None:
    with tarfile.open(f"{dir}/{file}", "r:gz") as tar:
        tar.extractall(path=dir)
    os.remove(f"{dir}/{file}")

def extract(file:str, dir:str, libName:str) -> None:
    fullPath:str = f"{dir}/{file}"
    extension:int = 0

    match Data.os:
        case OS.LINUX:
            with tarfile.open(fullPath, "r:gz") as archive:
                archive.extractall(path=dir)
            extension = 7
        case OS.WINDOWS:
            with zipfile.ZipFile(fullPath, "r") as archive:
                archive.extractall(path=dir)
            extension = 4

    os.remove(fullPath)
    os.rename(fullPath[:-extension], libName)
    return

def get(lib:Data.LibsEntry) -> None:
    libDir:str = f"{Data.projDir}/{Data.libDir}"

    filename = download(lib, libDir)
    if "" == filename: return

    extract(filename, libDir, f"{libDir}/{lib["name"]}")
    return