import socket
import threading
import os

HOST = '192.168.0.109'
HEADER = 100
FORMAT = 'utf-8'
port = 5050
path = r"C:\Users\User\Desktop\wallpaper"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
os.chdir(path)
name_of_files = list(os.listdir())
no_of_files = len(name_of_files)
print(no_of_files)
client.connect((HOST, port))
nfsend = str(no_of_files) + " " * (HEADER - len(str(no_of_files)))
client.send(nfsend.encode(FORMAT))
print(name_of_files)
client.close()
def sendF(client,name):
    filesize = int(os.path.getsize(os.path.join(name)))
    fmeta = str(filesize) + " " + name
    fmeta += " " * (HEADER - len(fmeta))
    client.send(fmeta.encode(FORMAT))
    with open(os.path.join(name), 'rb') as f:
        bytesToSend = f.read(1024)
        print("sending", name)
        client.send(bytesToSend)
        while bytesToSend != b"":
            bytesToSend = f.read(1024)
            client.send(bytesToSend)

for name in name_of_files:
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST,port))
    thread=threading.Thread(target=sendF,args=(client,name))
    thread.start()
    thread.join()
    client.close()