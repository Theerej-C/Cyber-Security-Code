import sys 
import socket
import threading


def server_loop(local_host,local_port,remote_host,remote_port,recieve_first):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
        server.bind((local_host,local_port))
    except:
        print("Failed to listen int the %s / %d"%(local_host,local_port))
        
        sys.exit(0)
    print("Listening to the %s / %d"%(local_host,local_port))
    
    server.listen(5)
    
    while True:
        
        client_socket , args = server.accept()
        proxy_thread = threading.Thread(target=proxy_handler,args=(client_socket,remote_host,
                                                                   remote_port,recieve_first))
        proxy_thread.start()
    
    
def proxy_handler(client_socket,remote_host,remote_port,recieve_first):
    remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    remote_socket.connect((remote_host,remote_port))
    
    if recieve_first:
        remote_buffer = recieve_from(remote_socket)
        hex_dump(remote_buffer)
        
        remote_buffer = response_handler(remote_buffer)
        l = len(remote_buffer)
        if len(remote_buffer):
            print("Sending %s bytes of data to the local host"%l)
            client_socket.send(remote_buffer.encode())
            
            
    while True:
        local_buffer = recieve_from(client_socket)
        hex_dump(local_buffer)
        
        print("Recieved from the localHost %d bytes"%len(local_buffer))
        
        
        local_buffer = request_handler(local_buffer)
        
        if len(local_buffer):
            
            print("Sending Bytes to the remoteHost")
            remote_socket.send(local_buffer.encode())
            
        remote_buffer = recieve_from(remote_socket)
        
        if len(remote_buffer):
            
            hex_dump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            
            client_socket.send(remote_buffer.encode())
            print("Sent to localHost")
            
        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            
            print("No input or output is there")
            

            break

def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, unicode) else 2
    for i in xrange(0, len(src), length):
        s = src[i:i+length]
        hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        result.append( b"%04X %-*s %s" % (i, length*(digits + 1), hexa,
                                          text) )
    print(b'\n'.join(result))

def recieve_from(connect):
    
    buffer = ""
    connect.settimeout(2)
    
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
            
    except:
        pass
    return buffer
        
def response_handler(buffer):
    #code that can do anything to the buffer
    return buffer
def request_handler(buffer):
    #code that can do anything to the buffer
    return buffer
def main():
    if (sys.argv[1:]) != 5:
        print("Usage: ./Tcp_Proxy.py localhost localport remotehost remoteport recievefirst")
        print("Example: ./Tcp_Proxy.py 127.0.0.1 9000 145.89.67.6 9898 True")
        
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    
    recieve_first = sys.argv[5]
    
    if "True" in recieve_first:
        recieve_first = True
    else:
        recieve_first = False
        
    server_loop(local_host,local_port,remote_host,remote_port,recieve_first)
    
main()
