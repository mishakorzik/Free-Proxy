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

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mAll")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mUSA")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mRussia")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mUkraine")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mIndia")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mItaly")
print("  # \033[1;34m[ 07 ] >> \033[1;36;40mCanada")
print("  # \033[1;34m[ 08 ] >> \033[1;36;40mFrance")
print("  # \033[1;34m[ 09 ] >> \033[1;36;40mThailand")
print("  # \033[1;34m[ 10 ] >> \033[1;36;40mPoland")
print("  # \033[1;34m[ 11 ] >> \033[1;36;40mNetherlands")
print("  # \033[1;34m[ 12 ] >> \033[1;36;40mMexico")
print("  # \033[1;34m[ 13 ] >> \033[1;36;40mKazakhstan")
print("  # \033[1;34m[ 14 ] >> \033[1;36;40mIran")
print("  # \033[1;34m[ 15 ] >> \033[1;36;40mEgypt")
print("  # \033[1;34m[ 16 ] >> \033[1;36;40mHong Kong")
print("  # \033[1;34m[ 17 ] >> \033[1;36;40mGermany")
print("  # \033[1;34m[ 18 ] >> \033[1;36;40mVietman")
print("  # \033[1;34m[ 19 ] >> \033[1;36;40mHungary")
print("  # \033[1;34m[ 20 ] >> \033[1;36;40mBrazilia")
print("  # \033[1;34m[ 21 ] >> \033[1;36;40mJapan")
print("  # \033[1;34m[ 22 ] >> \033[1;36;40mKambodia")
print("  # \033[1;34m[ 23 ] >> \033[1;36;40mChina")
print("  # \033[1;34m[ 24 ] >> \033[1;36;40mChile")
print('')
print("  # \033[1;34m[ 25 ] >> \033[1;36;40mSSL PROXY")
print("  # \033[1;34m[ 26 ] >> \033[1;36;40mSOCKS4 PROXY")
print("  # \033[1;34m[ 27 ] >> \033[1;36;40mSOCKS5 PROXY")
print("  # \033[1;34m[ 28 ] >> \033[1;36;40mUPDATE UTILITY")
print("  # \033[1;34m[ 29 ] >> \033[1;36;40mEXIT UTILITY")

op=int(raw_input("Options: "))

if(op==1):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=750&country=all"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==2):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=750&country=US"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==3):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=RU"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==4):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=UA"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==5):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=IN"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==6):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=IT"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==7):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=CA"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==8):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=FR"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==9):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=TH"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==10):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1000&country=PL"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==11):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=2100&country=NL"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==12):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1500&country=MX"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==13):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1500&country=KZ"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==14):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1500&country=IR"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==15):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1500&country=EG"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==16):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=2250&country=HK"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==17):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1500&country=DE"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==18):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1500&country=VN"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==19):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1500&country=HU"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==20):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1500&country=BR"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==21):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1500&country=JP"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==22):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1500&country=KH"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==23):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=1250&country=CN"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==24):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=2250&country=CL"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==25):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=500&country=all&ssl=all"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==26):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=750&country=all"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==27):
 proxyDomain = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=750&country=all"
 system = requests.get(proxyDomain).text
 print(system)
elif(op==28):
 print("Updating tool. Please wait a moment")
 os.system("cd src")
 os.system("bash ProxyUpdater.sh")
elif(op==29):
 print("\033[1;31;40mQuiting Utility...")
 time.sleep(0.8)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1.5)
 sys.exit()
