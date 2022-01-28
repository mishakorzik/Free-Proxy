g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

apt-get update
apt-get upgrade
apt-get upgraded
sleep 1
echo -e $b">"$w" installing modules: "$g"git"$w
sleep 1
apt-get install git
sleep 1
echo -e $b">"$w" installing modules: "$g"python2"$w
sleep 1
apt-get install python2
sleep 1
echo -e $b">"$w" installing modules: "$g"requests"$w
sleep 1
pip2 install requests
sleep 1
cd
cd Free-Proxy 
rm -rf IMG_20210510_150717.jpg
rm -rf IMG_20210510_150700.jpg
rm -rf IMG_20210510_150436.jpg
rm -rf IMG_20210510_145354.jpg

