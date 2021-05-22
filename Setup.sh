clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
sleep 1
echo Installing packages please wait...
echo By mishakorzhik
sleep 2
cd
apt-get update
apt-get upgrade
sleep 1
echo -e $b">"$w" installing modules: "$g"git"$w
sleep 1
apt-get install git
sleep 1
echo -e $b">"$w" installing modules: "$g"python2"$w
sleep 1
apt-get install python
apt-get install python2
sleep 1
echo -e $b">"$w" installing modules: "$g"requests"$w
sleep 1
pkg install pip
pip2 install requests
sleep 1
echo -e $b">"$w" installing modules: "$g"bs4"$w
sleep 1
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
echo ██████╗░░█████╗░███╗░░██╗███████╗
echo ██╔══██╗██╔══██╗████╗░██║██╔════╝
echo ██║░░██║██║░░██║██╔██╗██║█████╗░░
echo ██║░░██║██║░░██║██║╚████║██╔══╝░░
echo ██████╔╝╚█████╔╝██║░╚███║███████╗
echo ╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝
echo Developer: mishakorzhik
echo Update on: 22 05 2021
echo Run command: bash FreeProxy.sh
