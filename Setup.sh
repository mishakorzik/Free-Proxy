clear
sleep 1
echo Installing packages please wait...
echo By mishakorzhik
sleep 2
cd
apt-get update
apt-get upgrade
apt-get install git 
apt-get install python2
pip2 install requests
pip2 install bs4
chmod +x Free-Proxy
cd Free-Proxy
sleep 1
echo succesfull installed!
sleep 1 
rm -rf IMG_20210510_150717.jpg
rm -rf IMG_20210510_150700.jpg
rm -rf IMG_20210510_150436.jpg
rm -rf IMG_20210510_145354.jpg
rand1=$( shuf -i 0-${#colors[@]} -n 1 )
rand2=$( shuf -i 0-${#colors[@]} -n 1 )
# Colors
r='\e[91m'
g='\e[92m'
y='\e[93m'
b='\e[94m'
p='\e[95m'
c='\e[96m'
w='\e[97m'
n='\e[0m'
# effect colors
bd='\e[1m'
dm='\e[2m'
it='\e[3m'
ul='\e[4m'
rv='\e[7m'
echo -e "\t${colors[rand1]} ██████╗░░█████╗░███╗░░██╗███████╗
echo -e "\t${colors[rand1]} ██╔══██╗██╔══██╗████╗░██║██╔════╝
echo -e "\t${colors[rand1]} ██║░░██║██║░░██║██╔██╗██║█████╗░░
echo -e "\t${colors[rand1]} ██║░░██║██║░░██║██║╚████║██╔══╝░░
echo -e "\t${colors[rand1]} ██████╔╝╚█████╔╝██║░╚███║███████╗
echo -e "\t${colors[rand1]} ╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝
echo -e "\t${colors[rand1]}         Developer: mishakorzhik
echo -e "\t${colors[rand1]}          Update on: 16 05 2021
echo -e "\t${colors[rand2]}    Run command: python2 Free-Proxy.py
