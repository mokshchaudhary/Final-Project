import requests
import hashlib
from const import bcolors


def fetchserverlist(SERVERURL):
    # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    try:
        r = requests.get(url=SERVERURL)
        Serverlist = list(r.text.split(","))
        str = ""
        ServerSha = hashlib.sha1(
            str.join(Serverlist).encode()).hexdigest()[:10]
        return Serverlist, ServerSha

    except requests.exceptions.RequestException as e:
        return 'fail'
