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

def main_server_loop():
    global target
    
    if not len(target):
        target = "0.0.0.0"
        
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    server.bind((target,port))
        
    server.listen(5)
    
    while True:
        
        client_soc,addr = server.accept()
        process_server = threading.Thread(target=client_handle,args=(client_soc,))
        process_server.start() 
        
def client_handle(client_soc):
    if len(dest):
        file_buffer=""
        
        while True:
            data=client_soc.recv(1024)
            
            if not data:
                break
            else:
                file_buffer+=data
                
        try:
            file_desc = open(dest,"wb")
            file_desc.write(file_buffer)
            file_desc.close()
            
            client_soc.send("Sucessfully written in the destination".encode())
            
                
        except:
            client_soc.send("Failed to upload to destination".encode())
            
    if len(execute):
        output=run_command(execute)
        
        client_soc.send(output.encode())
        
    if command:
        
        while True:
            client_soc.send("<NET>.".encode())
            
            cmd_buffer = ""
            
            while "\n" not in cmd_buffer:
                cmd_buffer += client_soc.recv(1024)
                
            response = run_command(cmd_buffer)
            
            client_socket.send(response.encode())
            
def run_command(command):
    command = command.rstrip()
    
    try:
        output=subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
        
    except:
        print("Command not Executed:")
        
    return output
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
            port = int(a)
        else:
            assert False,"Unhandled Option" 
        

    if not listen and len(target) and port>0:
        buffer = sys.stdin.read()
    
        client_send(buffer)
    
    if listen:
        main_server_loop()
    
main()
