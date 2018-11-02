#!/usr/bin/python3           # This is client.py file

import socket



def send_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    host = "localhost"                        
    port = 8181
    s.connect((host, port)) 
    s.send("./double.py".encode())            
    msg = s.recv(1024)                                 

    s.close()
    print("listener said:")
    print (msg.decode('ascii'))

if __name__ == "__main__":
    send_message()