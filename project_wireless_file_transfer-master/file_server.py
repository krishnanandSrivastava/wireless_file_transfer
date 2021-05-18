import socket
import threading
import os

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
HEADER = 100
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
CONN_LIST = []
thread = []
path = r"C:\Users\User\Desktop\received"
meta_data = ""

def rec_meta(conn):
    global meta_data
    meta_data = str(conn.recv(HEADER).decode(FORMAT))

def rec_file(conn,filename,filesize):
    f = open(rf"C:\Users\User\Desktop\received\{filename}", 'wb')
    data = conn.recv(filesize)
    f.write(data)
    f.close()

def file_trans(conn):
    try:
        global meta_data
        print(conn, ".....connected")
        meta_data = str(conn.recv(HEADER).decode(FORMAT))
        print(len(meta_data))
        c = 0
        for i in range(int(meta_data)):
            t2=threading.Thread(target=rec_meta,args=(conn,))
            t2.start()
            t2.join()
            # print(len(meta_data))
            c += 1
            print(c)
            filesize, filename = meta_data.strip().split(" ")
            filesize = int(filesize)
            filename = filename.strip()
            print("receiving", filename, filesize)
            t3=threading.Thread(target=rec_file,args=(conn,filename,filesize))
            t3.start()
            t3.join()
            conn.send("1111111111".encode('utf-8'))
        conn.close()
    except:
        conn.close()


def start():
    print(f"Starting server at {HOST}.......", end="")
    server.listen()
    print("DONE")
    while True:
        conn, addr = server.accept()
        CONN_LIST.append(conn)
        thread.append(threading.Thread(target=file_trans, args=(conn,)))
        thread[-1].start()


start()
