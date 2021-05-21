number=int(raw_input("\033[1;33;40mEnter the number of proxies you want to generate(Max:50) :"))
if(number>50):
 print("\033[1;31;40mEnter a number <=40. Quiting...")
 time.sleep(1.5)

print("          \033[1;32;40m[2] \033[1;36;40mUS PROXY")
print("          \033[1;32;40m[3] \033[1;36;40mUK PROXY")
print("          \033[1;32;40m[4] \033[1;36;40mSSL PROXY")
print("          \033[1;32;40m[5] \033[1;36;40mANONYMOUS PROXY")
print("          \033[1;32;40m[6] \033[1;36;40mSOCKS PROXY")

op=int(raw_input("Diya>>>"))
if(op==1):
 generate("https://free-proxy-list.net",number) 
elif(op==2):
 generate("https://us-proxy.org",number) 
elif(op==3):
 generate("https://free-proxy-list.net/uk-proxy.html",number)
elif(op==4):
 generate("https://www.sslproxies.org",number)
elif(op==5):
 generate("https://free-proxy-list.net/anonymous-proxy.html",number)
elif(op==6):
 socks(number)
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1.5)
 sys.exit()
