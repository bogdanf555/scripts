import requests
import sys

if len(sys.argv) != 3:
    print("Error: you should pass 2 arguments: link_to_download_from_path_to_save_downloaded file")
    exit(1)

url = sys.argv[1]
r = requests.get(url, allow_redirects=True)

open(sys.argv[2], 'wb').write(r.content)
