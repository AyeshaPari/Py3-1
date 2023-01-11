import os, platform, time
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
        os.system('clear')
        print(' [•] Checking update......')
        time.sleep(4)
        os.system('xdg-open https://www.github.com/SPOILT-X')


import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
        os.system('xdg-open https://www.github.com/SPOILT-X')

        from Py3_enc import Main
 
        Main()
 
