Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

import time
import itertools
import threading
import sys

done = False
 
def animate():
    for c in itertools.cycle(['Starting', 'sTarting', 'stArting', 'staRting', 'starTing','startIng', 'startiNg', 'StartinG']):
        if done:
            break
        sys.stdout.write('\r ' + c)
        sys.stdout.flush()
        time.sleep(0.25)
    sys.stdout.write('')

t = threading.Thread(target=animate)
t.start()

 
time.sleep(4)
done = True

print " "+Red+"░██████╗████████╗░█████╗░██████╗░████████╗██╗███╗░░██╗░██████╗░"
print " "+Red+"██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██║████╗░██║██╔════╝░"
print " "+Red+"╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░██║██╔██╗██║██║░░██╗░"
print " "+Red+"░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██║██║╚████║██║░░╚██╗"
print " "+Red+"██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝"
print " "+Red+"╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░"
