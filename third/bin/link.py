import os
import tarfile
import urllib.request
import urllib.parse
import urllib.error

def download(url:str, dstDir:str) -> str:
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

def get(url:str, dstDir:str, tar:bool=False) -> None:
    filename = download(url, dstDir)
    if "" == filename: return

    if tar: untar(filename, dstDir)
    return