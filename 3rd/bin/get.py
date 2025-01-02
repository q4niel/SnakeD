import os
import urllib.request
import urllib.parse
import urllib.error

def download(url:str, dstDir:str) -> bool:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            if response.status != 200:
                print(f"Failed to download. Status code: {response.status}")
                return False
    
            filename = os.path.basename(urllib.parse.urlparse(url).path)
            filePath = os.path.join(dstDir, filename)
    
            with open(filePath, "wb") as file:
                while chunk := response.read(1024):
                    file.write(chunk)
    
            print(f"Downloaded {filename} successfully!")
            return True

    except urllib.error.HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
        return False

    except urllib.error.URLError as e:
        print(f"URL error occurred: {e.reason}")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False