import socket
import threading
import os
os.chdir(r"C:\Users\User\Desktop\wallpaper")
names=list(os.listdir())
HOST='192.168.0.109'
PORT=5050
HDL=100
path=r"C:\Users\User\Desktop\wallpaper"
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
no_of_files=str(len(names))
sd=no_of_files+" "*(HDL-len(no_of_files))
client.send(sd.encode('utf-8'))
c=0
def sendf(filename):
        global c
        filesize=int(os.path.getsize(os.path.join(filename)))
        print(filesize)
        sendData=str(filesize)+" "+str(filename)
        sendData+=" "*(HDL-len(sendData))
        print(len(sendData.encode('utf-8')))
        client.send(sendData.encode('utf-8'))
        f=open(os.path.join(filename),"rb")
        sendData=f.read()
        print("sending...."+filename)
        client.send(sendData)
        f.close()
        print(client.recv(10).decode('utf-8'))
        c+=1

for filename in names:
    thread=threading.Thread(target=sendf,args=(filename,))
    thread.start()
    thread.join()
# samplestring="121213 dfdsgdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaak.txt"
# samplestring+=" "*(100-len(samplestring))
# samplestring=samplestring.encode('utf-8')
# print(len(samplestring))
# client.send(samplestring)