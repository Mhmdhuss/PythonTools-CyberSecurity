import sys
import requests

def fuzz():
    for word in sys.stdin:
        res = requests.get(url=f"http://10.10.11.161/{word}")
        if res.status_code == 404:
            fuzz()
        else:
            data = res.json()
            print(res)
            print(res.status_code)
            print(data)

fuzz()