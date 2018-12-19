#!/usr/bin/python
import os
import subprocess
import sys
import time

def monitor(interface):
    os.system("sudo ifconfig "+interface+" down")
    time.sleep(1)
    os.system("sudo iwconfig "+interface+" mode monitor")
    time.sleep(1)
    os.system("sudo ifconfig "+interface+" up")


def managed(interface):
    os.system("sudo ifconfig "+interface+" down")
    time.sleep(1)
    os.system("sudo iwconfig "+interface+" mode managed")
    time.sleep(1)
    os.system("sudo ifconfig "+interface+" up")

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
C  = '\033[36m' # cyan
O  = '\033[33m' # orange

if __name__ == "__main__":
    if os.geteuid():
        sys.exit('['+R+'*'+W+"] Please run as 'root' ")
    data_scope = subprocess.check_output("ifconfig").split("\n")
    devices = []
    for str in data_scope :
        if len(str) != 0:
    	    if str[0] == "w" :
    	        devices.append(str.split(":")[0])
    cnt = 1
    try :
        print("Please choose your interface :")
    except :
        print("Error !")
        quit()
    for device in devices :
        print (O+'%d '+W+"["+R+'%s'+W+"]")% (cnt,device)
        cnt = cnt + 1
    interface = devices[int(input(":"))-1]
    print("\n["+R+"*"+W+"] Choose your action :\n")
    print(C+"1- Managed Mode")
    print(R+"2- Monitor Mode")
    print(""+W)
    try :
        choice = input(":")
    except :
        print("Error !")
        quit()

    if(choice == 1):
        managed(interface)
        print("")
        subprocess.call("iwconfig")
        print("\n"+R+"%s "+W+"mode changed succesfully\n")% interface
    if(choice == 2):
        monitor(interface)
        print("")
        subprocess.call("iwconfig")
        print("\n"+R+"%s "+W+"mode changed succesfully")% interface
