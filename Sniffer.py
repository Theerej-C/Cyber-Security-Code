import socket
import os
import struct
from ctypes import *

host = "10.0.2.15"  

class IP(Structure):
        _fields_ =[ 
                ("ihl",         c_ubyte, 4),
                ("version",     c_ubyte, 4),
                ("tos",         c_ubyte), 
                ("len",         c_ushort),
                ("id",          c_ushort),
                ("offset",      c_ushort),
                ("ttl",         c_ubyte),
                ("protocol_num",c_ubyte),
                ("sum",         c_ushort),
                ("src",         c_uint32),
                ("dst",         c_uint32),
        ]

        def __new__(self,soc_buff=None):
                return self.from_buffer_copy(soc_buff)

        def __init__(self,soc_buff=None):
                self.format = {1:"ICMP", 6:"TCP", 17:"UDP"}

                self.source = socket.inet_ntoa(struct.pack("@I",self.src))
                self.destination = socket.inet_ntoa(struct.pack("@I",self.dst))

                try:
                        self.protocol = self.format[self.protocol_num]
                except:
                        self.protocol = str(self.protocol_num)

if os.name == "nt":
        socket_proto = socket.IPPROTO_IP
else:
        socket_proto = socket.IPPROTO_ICMP

soc = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_proto)

soc.bind((host,0))

soc.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL,1)

if os.name == "nt":
        soc.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

try:
        while True:
                buffer = soc.recvfrom(65565) [0]
                header = IP(buffer[0:20])

                print("Protocol is %s %s -> %s"%(header.protocol, header.source, header.destination))

except keyboardInterrupt:
        if os.name == 'nt':
                soc.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


