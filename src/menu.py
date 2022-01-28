import requests
import os
import time
import sys

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mALL PROXY")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mUS PROXY")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mRU PROXY")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mSSL PROXY")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mSOCKS4 PROXY")
print("  # \033[1;34m[ 6 ] >> \033[1;36;40mSOCKS5 PROXY")
print("  # \033[1;34m[ 7 ] >> \033[1;36;40mUPDATE UTILITY")
print("  # \033[1;34m[ 8 ] >> \033[1;36;40mEXIT UTILITY")

op=int(raw_input("Options: "))

if(op==1):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=all"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==2):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=US"
 system = requests.get(proxyDomain)
 print(system)
elif(op==3):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=RU"
 system = requests.get(proxyDomain)
 print(system)
elif(op==4):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=750&country=all&ssl=all"
 system = requests.get(proxyDomain)
 print(system)
elif(op==5):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=750&country=all"
 system = requests.get(proxyDomain)
 print(system)
elif(op==6):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=750&country=all"
 system = requests.get(proxyDomain)
 print(system)
elif(op==7):
 print("Updating tool. Please wait a moment")
 os.system("cd src")
 os.system("bash ProxyUpdater.sh")
elif(op==8):
 print("\033[1;31;40mQuiting Utility...")
 time.sleep(0.8)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1.5)
 sys.exit()
