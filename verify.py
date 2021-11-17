import requests
from const import bcolors


def Verify(PARAMS, serverlist):
    print(bcolors.OKBLUE+bcolors.BOLD +
          'Verifying with grid Network 🌎'+bcolors.ENDC)
    tr = 0
    fa = 0
    print()
    for i in range(len(serverlist)):
        URL = serverlist[i]+"/verify"

        print("Server "+f'{i+1}: ' + bcolors.BOLD +
              bcolors.OKBLUE + 'Connecting ...' + bcolors.ENDC, end='\r')
        try:
            r = requests.get(url=URL, params=PARAMS, timeout=4)
            rtext = r.text
            print('                                  ', end='\r')
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            rtext = 'Timeout'
            print('                                  ', end='\r')

        if(rtext == 'True'):
            tr = tr+1
            print("Server "+f'{i+1}: ' + bcolors.BOLD +
                  bcolors.OKGREEN + 'Verified' + bcolors.ENDC)
        if(rtext == 'False'):
            fa = fa+1
            print("Server "+f'{i+1}: ' + bcolors.BOLD +
                  bcolors.FAIL + 'No Match' + bcolors.ENDC)
        if(rtext == 'Timeout'):
            fa = fa+1
            print("Server "+f'{i+1}: ' + bcolors.BOLD +
                  bcolors.FAIL + 'Server Timeout' + bcolors.ENDC)

    print()
    print('====================================')
    print(f'Authentic : '+bcolors.OKGREEN + bcolors.BOLD +
          f'{tr}    '+bcolors.ENDC+'Not-Authentic : ' + bcolors.FAIL + bcolors.BOLD + f'{fa}' + bcolors.ENDC)
    print('====================================')
    print()
    print(bcolors.BOLD+'File authenticity ', end='')
    if(tr > fa):
        print('verified ✅')
    else:
        print('not verified ❌')
    print(bcolors.ENDC)
