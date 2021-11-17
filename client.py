
import os
import verify
import fetchServer
from const import printhead, bcolors
import sys
import hashlib
import random
import string
import requests
import json
# =====================================================
SERVERURL = "http://localhost:8080"

os.system('clear')


def head():
    printhead()
    print(bcolors.BOLD+bcolors.HEADER+'Authors:' +
          bcolors.WARNING+' 👨 Moksh Chaudhary'+bcolors.ENDC)
    print(bcolors.BOLD+'\t 👩 Amrit Kaur'+bcolors.ENDC)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()


head()

sha1 = hashlib.sha1()
with open(sys.argv[1], 'rb') as f:
    while True:
        data = f.read(65536)
        if not data:
            break
        sha1.update(data)

print(bcolors.BOLD+bcolors.WARNING +
      'Fetching Server List ...'+bcolors.ENDC)

servefetch = fetchServer.fetchserverlist(SERVERURL)
os.system('clear')
head()
if servefetch != 'fail':
    serverlist = servefetch[0]
    serversha = servefetch[1]
    print(bcolors.OKGREEN+bcolors.BOLD +
          'Server List Fetch Complete'+bcolors.ENDC)
    print(f'Server List Signature : ' +
          bcolors.UNDERLINE + serversha+bcolors.ENDC)
    print(f'Number of Server Found : ' + bcolors.BOLD +
          f'{len(serverlist)}'+bcolors.ENDC)
    print()
else:
    print(bcolors.WARNING+bcolors.BOLD +
          'Server Fetch Failed     '+bcolors.ENDC)
    print()
    exit()

input('Press enter to continue ... ')


def newrecord(sha1, key):
    for i in range(len(serverlist)):
        url = serverlist[i]
        print(f'Uploading Server {i+1} : ', end='')
        payload = json.dumps([
            key,
            sha1.hexdigest()
        ])
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            response = requests.request(
                "POST", url, headers=headers, data=payload)
            print(bcolors.OKGREEN+bcolors.BOLD+'Success'+bcolors.ENDC)
        except requests.exceptions.RequestException as e:
            print(bcolors.FAIL+bcolors.BOLD+'Fail'+bcolors.ENDC)


while True:
    os.system('clear')
    head()
    print(bcolors.BOLD, end='')
# print('Please Select one:')
    print('   [1] Verify Integrity')
    print('   [2] Upload Record')
    print('   [3] View Server List')
    print('   [4] About')
    print('   [5] Exit')
    print(bcolors.ENDC)
    i = input(bcolors.OKBLUE+'Enter choice:'+bcolors.ENDC+' ')

    if(i == '1'):
        os.system('clear')
        printhead()
        print()
        s = input('Enter the File Key : ')
        print()
        os.system('clear')
        printhead()
        ss = sha1.hexdigest()
        PARAMS = {'filename': s, 'signature': ss}
        verify.Verify(PARAMS,  serverlist)
        input('Press enter to continue ...')

    if(i == '2'):
        os.system('clear')
        head()
        key = ''.join(random.choice(string.ascii_lowercase + string.digits)
                      for _ in range(6))
        newrecord(sha1, key)
        print()
        print(bcolors.OKGREEN+bcolors.BOLD+'Signature uploaded'+bcolors.ENDC)
        print('File Key: ' + bcolors.BOLD + key + bcolors.ENDC)
        print()
        input('Press enter to continue ...')

    if(i == '3'):
        os.system('clear')
        head()
        for i in serverlist:
            print(bcolors.BOLD+i+bcolors.ENDC)
        print()
        input('Press enter to continue ...')

    if(i == '4'):
        os.system('clear')
        head()
        os.system('cowsay -g Security is Money')
        print()
        print(bcolors.BOLD)
        print('Version : 0.1 Beta')
        print()
        print('Created by:')
        print('\t > Moksh Chaudhary')
        print('\t > Amrit Kaur')
        print(bcolors.OKBLUE)
        print('Technology used:')
        print('\t [1] Cryptography')
        print('\t [2] Node.js')
        print('\t [3] Python')
        print('\t [4] AWS EC2')
        print('\t [5] Docker')
        print('\t [6] Networking')
        print(bcolors.ENDC)

        input('Press enter to continue ...')

    if(i == '5'):
        exit()
