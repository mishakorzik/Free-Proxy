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
echo ██████╗░░█████╗░███╗░░██╗███████╗
echo ██╔══██╗██╔══██╗████╗░██║██╔════╝
echo ██║░░██║██║░░██║██╔██╗██║█████╗░░
echo ██║░░██║██║░░██║██║╚████║██╔══╝░░
echo ██████╔╝╚█████╔╝██║░╚███║███████╗
echo ╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝
echo Developer: mishakorzhik
echo Update on: 17 05 2021
echo Run command: python2 Free-Proxy.py
