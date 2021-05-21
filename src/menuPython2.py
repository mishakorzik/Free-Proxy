import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

print("          \033[1;32;40m[1] \033[1;36;40mNEW PROXY")
print("          \033[1;32;40m[2] \033[1;36;40mUS PROXY")
print("          \033[1;32;40m[3] \033[1;36;40mUK PROXY")
print("          \033[1;32;40m[4] \033[1;36;40mSSL PROXY")
print("          \033[1;32;40m[5] \033[1;36;40mANONYMOUS PROXY")
print("          \033[1;32;40m[6] \033[1;36;40mSOCKS PROXY")

op=int(raw_input("Diya>>>"))

if(op==1):
 proxyDomain = "https://free-proxy-list.net" 

 system = requests.get(proxyDomain)
 
 mranonymous_systemSoup = BeautifulSoup(system.content,'html.parser')

 sosBlackhats = mranonymous_systemSoup.find('table',{"id" : "proxylisttable"})
 for row in sosBlackhats.find_all('tr'):
    columns = row.find_all('td')
    try:
        print "%s:%s\t%-20s\t%-10s"  % (columns[0].get_text(),columns[1].get_text(),columns[3].get_text(),columns[4].get_text())
    except:
        pass
elif(op==2):
 generate("https://us-proxy.org",40) 
elif(op==3):
 generate("https://free-proxy-list.net/uk-proxy.html",40)
elif(op==4):
 generate("https://www.sslproxies.org",40)
elif(op==5):
 generate("https://free-proxy-list.net/anonymous-proxy.html",40)
elif(op==6):
 print " "+Blue+"177.206.186.9:8080   SOCKS4   Brazil   Elite"
 print " "+Blue+"51.81.31.62:54860   SOCKS5  Francia    hing anonymous"
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1.5)
 sys.exit()
