import socket
import threading
import os

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
header = 100
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
path = r"C:\Users\User\Desktop\received"
os.chdir(path)
CONN_LIST = []
thread = []


def handel_client(conn, addr):
        meta = conn.recv(header).decode(FORMAT)
        filesize, filename = meta.strip().split()
        filesize = int(filesize)
        buff = 0
        f = open(os.path.join(filename), 'wb')
        while buff < filesize:
            data = conn.recv(1024)
            buff += len(data)
            f.write(data)
        print("Download....complete")
        f.close()
        conn.close()


def start():
    print(f"Starting server at [{HOST}]......", end="")
    server.listen()
    print("DONE")
    conn, addr = server.accept()
    no_of_files = int(conn.recv(header).decode(FORMAT))
    print("no_of_files:", no_of_files)
    while True:
        conn, addr = server.accept()
        CONN_LIST.append(conn)
        print("New client connected....." , addr)
        thread.append(threading.Thread(target=handel_client, args=(conn, addr,)))
        thread[-1].start()
start()