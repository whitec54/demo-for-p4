#!/usr/bin/python3
import socket
import sh
from threading import Thread
from time import sleep

TODO = []



def listen():
    # create a socket object
    serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) 

    host = "localhost"                           
    port = 8181

    serversocket.bind((host, port))                                  

    serversocket.listen()
    print("passed listen")                                        

    while True:
        clientsocket,addr = serversocket.accept()
        print("passed accept")    

        print("Got a connection from %s" % str(addr))
        data = clientsocket.recv(1024).decode()
        print("Got a message %s" % str(data))

        TODO.append({
            'in':'./input.txt',
            'out':'./output.txt',
            'exe':data
        })
            
        msg = 'Gonna do that work'+ "\r\n"
        clientsocket.send(msg.encode('ascii'))
        clientsocket.close()

def look_for_work():
    while True:
        if TODO:
            print("doing work")
            work = TODO[-1]
            del TODO[-1]
            do_work(work["exe"], work["in"], work["out"])
        else:
            print("No work")

        sleep(5)

def do_work(exe, in_f_name, out_f_name):
    in_file = open(in_f_name, "r")
    out_file = open(out_f_name + "_" + exe[2:], "w")

    executable = sh.Command(exe)
    executable(_in=in_file, _out=out_file)

    in_file.close()
    out_file.close()

if __name__ == "__main__":
    t = Thread(target=listen)
    t.start()

    t2 = Thread(target=look_for_work)
    t2.start()

