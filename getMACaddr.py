import sys
import csv

def getEthName():
    # Get name of the Ethernet interface
    try:
        for root, dirs,files in os.walk('/sys/class/net'):
            for dir in dirs:
                if dir[:3]=='enx' or dir[:3]=='eth':
                    Sinterface=dir   
    except:
        interface="None"
    return interface


def getMAC(interface='eth0'):
    # Return the MAC address of the specified interface
    try:
        str1 = open('/sys/class/net/%s/address' %interface).read()
    except:
        str1 = "00:00:00:00:00:00"

    return str1[0:17]

if __name__ == "__main__":
    ethName = getEthName()
    ethMAC = getMAC('eth0')
    name = sys.argv[1]
    row = [name, ethMAC]
    print(ethMAC)
    with open('MAC adresses.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

