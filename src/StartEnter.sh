clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
echo "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╭━━━━╮╱╱╭━━━╮╭╮╱╱╱╱╱╭╮"
echo "┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃╭━━╯╱╭╯╰╮╱╱╱╱╱┃╭╮╭╮┃╱╱┃╭━╮┣╯╰╮╱╱╱╭╯╰╮"
echo "┃╰━╯┣━┳━━┳━━┳━━╮┃╰━━┳━╋╮╭╋━━┳━╮╰╯┃┃┣┻━╮┃╰━━╋╮╭╋━━┳┻╮╭╯"
echo "┃╭━━┫╭┫┃━┫━━┫━━┫┃╭━━┫╭╮┫┃┃┃━┫╭╯╱╱┃┃┃╭╮┃╰━━╮┃┃┃┃╭╮┃╭┫┃"
echo "┃┃╱╱┃┃┃┃━╋━━┣━━┃┃╰━━┫┃┃┃╰┫┃━┫┃╱╱╱┃┃┃╰╯┃┃╰━╯┃┃╰┫╭╮┃┃┃╰╮"
echo "╰╯╱╱╰╯╰━━┻━━┻━━╯╰━━━┻╯╰┻━┻━━┻╯╱╱╱╰╯╰━━╯╰━━━╯╰━┻╯╰┻╯╰━╯"
echo "Please press enter to launch..."
read a1
echo -e $b">"$w" verify modules: "$g"python2"$w
pkg install python
echo -e $b">"$w" verify modules: "$g"pip3"$w
pkg install pip3
echo -e $b">"$w" verify modules: "$g"requests"$w
pip3 install requests
echo -e $b">"$w" verify modules: "$g"lolcat"$w
pip2 install lolcat
pip install lolcat
gem install lolcat
clear
clear
cd 
cd
cd Free-Proxy
cd src
sleep 1
bash Free-Proxy.sh
sleep 1
python2 menu.py
