#!/usr/bin/env python2
# -*- coding: utf-8 

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

print " "+Green+"██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗"
print " "+Green+"██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝"
print " "+Green+"██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░"
print " "+Green+"██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░"
print " "+Green+"██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░"
print " "+Green+"╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░ v1.3"
print ""
print " "+Green+"          Developer : mishakorzhik"
print " "+Green+"          Code      : bash, python"
print ""
print " "+Blue+""

import time
import itertools
import threading
import sys

done = False
 
def animate():
    for c in itertools.cycle(['|', '/', '—', '\\']):
        if done:
            break
        sys.stdout.write('\rWAIT A MOMENT PROXY LOADING ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('')

t = threading.Thread(target=animate)
t.start()

 
time.sleep(6)
done = True

print ""+Purple+"---> Proxy has found!..."

time.sleep(2)


print""+Blue+""


import requests
from bs4 import BeautifulSoup

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
        
        print " "+Blue+"Additional server proxies"
        print " "+Blue+"139.59.112.102:80  Unknown  Singapore   Transparent"
        print " "+Blue+"51.81.31.62:54860   SOCKS5  Francia    hing anonymous"
        print " "+Blue+"46.101.130.118:8080   HTTPS   Germania   Transparent"
        print " "+Blue+"23.251.138.105:8080   HTTPS   california   Anonymous"
        print " "+Blue+"147.30.232.186:80    Unknown   Kazakhstan    Elite"
        print " "+Blue+"129.146.180.91:3128   HTTP     california    Unknown"
        print " "+Blue+"221.139.43.196:80     HTTP	Unknown    Anonymous"
        print " "+Blue+"217.79.181.109:443   HTTPS    Germania   hing anonymous"
        print " "+Blue+"91.109.149.204:8080   HTTP    Kaliningrad   Elite"
        print " "+Blue+"109.161.60.102:8080  Unknown    Russia      Anonymous"
        print " "+Blue+"3.211.17.212:80     HTTP      country:US   transparent"
        print " "+Blue+"3.211.65.185:80    HTTP     country:US  hing anonymous"
        print " "+Blue+"85.15.152.39:3128   HTTPS    Russian   hing anonymous"
        print " "+Blue+"104.248.63.15:30588  Unknown   Unknown   Elite"
        print " "+Blue+"104.248.63.18:30588   HTTPS   Unknown   Anonymous"
        print " "+Blue+"3.225.148.200:80      HTTP    country:US  Transparent"
        print " "+Blue+"104.248.63.17:30588   Unknown   Unknown   Unknown"
        print " "+Blue+"104.248.63.49:30588  HTTP    Unknown    Anonymous"
        print " "+Blue+"47.116.76.219:80    HTTP     Canada   hing anonymous"
        print " "+Blue+"94.26.193.137:8080   HTTP   St. Petersburg  Transparent"
        print " "+Blue+"194.67.78.220:80    HTTP    Moscow    Elite"
        print " "+Blue+"45.13.81.23:8080   Unknown  Unknown  Unknown"
        print " "+Blue+"18.216.242.158:80   Unknown  Unknown  Anonymous"
        print " "+Blue+"39.104.13.55:8080   HTTPS    China   Unknown"
        print " "+Blue+"177.206.186.9:8080   SOCKS4   Brazil   Elite"
        print " "+Blue+"182.253.176.45:80   HTTP    Indonesia   Unknown"
        print " "+Blue+"122.138.168.118:80  Unknown   China     Unknown"
        print " "+Blue+"13.57.207.226:80   Unknown   America   Unknown"
        print " "+Blue+"198.50.137.181:80  HTTPS    Canada    Unknown"
        print " "+Blue+"183.88.226.50:8080  HTTPS   Thailand  hing anonymous"
        print " "+Blue+"hing _anonymous proxies."
        print " "+Blue+"type: http, country: CA, 142.44.136.219:32769, high_anonymous"
        print " "+Blue+"type: http, country: US, 168.169.96.17:8080, anonymous"
        print " "+Blue+"type: http, country: FR, 51.222.197.146:32769, high_anonymous"
        print " "+Blue+"type: http, country: FR, 51.222.220.245:32769, high_anonymous"
        print " "+Blue+"type: http, country: MX, 169.57.1.85:80, high_anonymous"
        print " "+Blue+"type: http, country: MX, 169.57.1.84:80, high_anonymous"
        print " "+Blue+"type: http, country: MX, 169.57.1.84:8123, high_anonymous"
        print " "+Blue+"type: http, country: MX, 169.57.1.85:8123, high_anonymous"
        print " "+Blue+"type: http, country: US, 49.51.232.203:80, high_anonymous"
        print " "+Blue+"type: https, country: CA, 142.44.136.219:32769, high_anonymous"
        print " "+Blue+"type: http, country: FR, 159.8.114.37:8123, high_anonymous"
        print " "+Blue+"type: http, country: FR, 159.8.114.34:8123, high_anonymous"
        print " "+Blue+"type: http, country: NL, 52.178.32.225:80, transparent"
        print " "+Blue+"type: http, country: DE, 78.46.8.204:80, transparent"
        print " "+Blue+"Unknown proxy servers."
        print " "+Blue+"93.158.212.111:7808"
        print " "+Blue+"162.208.49.45:8089"
        print " "+Blue+"93.158.212.111:8089"
        print " "+Blue+"183.131.144.204:443"
        print " "+Blue+"58.246.199.122:3128"
        print " "+Blue+"93.158.212.111:7808"
        print " "+Blue+"210.39.18.236:8080"
        print " "+Blue+"61.234.249.127:8118"
        print " "+Blue+"95.143.41.21:7808"
        print " "+Blue+"61.234.249.107:8118"
        print " "+Blue+"27.115.75.114:8080"
        print " "+Blue+"167.88.37.141:80"
        print " "+Blue+"202.59.70.107:8080"
        print " "+Blue+"122.96.59.102:83"
        print " "+Blue+"122.96.59.102:82"
        print " "+Blue+"122.96.59.102:81"
        print " "+Blue+"122.96.59.106:83"
        print " "+Blue+"96.87.16.153:41344"
        print " "+Blue+"95.154.104.147:34153"
        print " "+Blue+"93.157.163.66:35081"
        print " "+Blue+"91.205.131.150:40694"
        print " "+Blue+"91.192.4.169:8090"
        print " "+Blue+"85.62.27.5:8888"
        print " "+Blue+"85.10.198.215:3838"
        print " "+Blue+"85.10.198.195:3838"
        print " "+Blue+"83.219.1.201:41380"
        print " "+Blue+"82.200.233.4:3128"
        print " "+Blue+"82.119.170.106:8080"
        print " "+Blue+"81.161.61.88:55978"
        print " "+Blue+"80.187.140.26:8080"
        print " "+Blue+"78.108.66.26:3128"
        print " "+Blue+"71.183.100.116:80"
        print " "+Blue+"69.63.73.171:53281"
        print " "+Blue+"58.84.190.2:53281"
        print " "+Blue+"52.179.231.206:80"
        print " "+Blue+"51.89.226.241:9999"
        print " "+Blue+"47.88.16.118:3128"
        print " "+Blue+"46.235.53.26:3128"
        print " "+Blue+"46.197.209.217:3128"
        print " "+Blue+"45.77.94.252:8080"
        print " "+Blue+"45.76.34.27:8080"
        print " "+Blue+"13.250.51.7:1080"
        print " "+Blue+"121.1.41.162:8080"
        print " "+Blue+"118.69.140.108:53281"
        print " "+Blue+"118.175.207.205:61293"

print" "+Red+" Proxy succesfull! Tranks for download ⋙" 

    





