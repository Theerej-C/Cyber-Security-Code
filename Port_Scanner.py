from socket import *
import optparse
from threading import *

def main():
        parser = optparse.OptionParser("Usage of Program: " + "-I <target host> -p <target port>")
        parser.add_option("-I","--IP",dest="IP",type = 'string',help ='Specify the target Host')
        parser.add_option("-p","--port",dest="port",type = "string",help="Specify the target port")
        (options, args) = parser.parse_args()
        IP = options.IP 
        port = options.port 
        port = str(options.port).split(',')
        if (IP == None) | (port[0]==None):
                print(parser.usage)
                exit(0)
        portScan(IP,port)

def portScan(IP,port):
        try:
                IpAddress = gethostbyname(IP)
        except: 
                IpAddress = gethostbyname(IP)
                print("Invalid Host Name")
        print("Scanning")
        setdefaulttimeout(2) 
        for port1 in port: 
                t = Thread(target = NetScan, args=(IP,int(port1))) 
                t.start()
def NetScan(IP,port):
        try:
                soc = socket(AF_INET, SOCK_STREAM)
                soc.connect((IP,port))
                print("%d port is open" %port)
        except:
                print("%d port is closed" %port)
        finally:
                soc.close()
               
main()
