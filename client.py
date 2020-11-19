import socket
import pyaes
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()

port=12345

s.bind((host,port))

s.listen(5)

print('hello')
y=input("enter the user id : ")
x=input("enter the password(must contains 10 letters among them 3 should be digit) : ")
z=input("enter your message : ")

while True:
    c,addr=s.accept()
    
    print("got the connection from",addr)
    
    e=str(x)
    
    c.send(e.encode())
    
    c.send(z.encode())
    
    print(c.recv(1024).decode())
    
    c.close()
