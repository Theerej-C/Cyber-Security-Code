import socket
import threading
import subprocess
import getopt
import sys


listen = False
command = False
up = False
execute = ""
target = ""
dest = ""
port = 0


def usage():
    print("Usage:")
    print("-l --listen             -listen on the host")
    
    print("-e --execute=file       -execute the given file")
    print("-c --command            -initialize a command prompt")
    print("-u --upload=dest        -upload a file at a destination")
    print
    print
    print("Example:")
    
    print("     file.name -t targethost -p port -l -c")
    
    sys.exit(0)
    
def main():
    global listen 
    global command
    global up
    global execute
    global dest
    global port
    
    
    if not len(sys.argv[1:]):
        usage()
        
    try:
        opt,arg = getopt.getopt(sys.argv[1:],"h:l:e:t:p:c:u",["help","listen","execute",
                                               "target","port","command","upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o,a in opt:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen=True
        elif o in ("-e","--execute"):
            execute=a
        elif o in ("-c","--command"):
            command = True
        elif o in ("-u","--upload"):
            dest = a
        elif o in ("-t","--target"):
            target = a 
        elif o in ("-p","--port"):
            port = a
        else:
            assert False,"Unhandled Option" 
        

    if not listen and len(target) and port>0:
        buffer = sys.stdin.read()
    
        client_send(buffer)
    
    if listen:
        server_loop()
    
main()

def client_send(buffer):
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
        s.connect((target,port))
        
        if len(buffer):
            s.send(buffer.encode())
            
        while true:
            recv_len = 1
            response = ""
            
            while recv_len:
                data = s.recv(1024)
                recv_len = len(data)
                response += data
                
            print(response)
            
        buffer = raw_input("")
        
        buffer+="\n"
        
        s.send(buffer.encode())
        
    except:
        
        print("Exception Exist")
        
        s.close()
        
def main_server_loop():
    global target
    
    if not len(target):
        target = "0.0.0.0"
        
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    server.bind((target,port))
        
    server.listen(5)
    
    while True:
        
        client_soc,addr = server.accept()
        process_server = threading.Thread(target=client_handler,args=(client_soc,))
        process_server.start()
        
        
        
    
    
    
