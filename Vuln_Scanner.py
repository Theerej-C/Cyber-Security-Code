import socket
import os
import sys

def main():
        if len(sys.argv) == 2:
                filename = sys.argv[1]
                if not os.path.isfile(filename):
                        print("File does not exist")
                        exit(0)
                if not os.access(filename, os.R_OK):
                        print("There is no Permission for you")
                        exit(0)
        else:
                print("Usage" + str(sys.argv[0]) + "vuln file name")
                exit(0)

        port_list = [21,22,25,80,443,445]
        
        ip = "192.168.56.1"
        for port in port_list:
                banner = returnbanner(ip,port)
                if banner:
                        print(ip + "/" + str[port] + ":" + banner)
                
                        checkVuln(banner, filename)
                else:
                        print("NO results")
def returnbanner(ip,port):
        try:
                socket.setdefaulttimeout(2)
                s = socket.socket()
                s.connect((ip,port))
                banner = s.recv(1024)
                return banner
        except:
                return


def checkVuln(banner, filename):
        f = open(filename, "r")
        for line in r.readlines():
                if line.strip("\n") in banner:
                        print("Server is vulnerable")
                        
# text file should be in the same directory 
main()

