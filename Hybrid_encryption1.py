import random
import string
import socket
import hashlib
import base64
import pyaes
import blowfish
from pyDes import *
import random
import string
s=socket.socket()

host=socket.gethostname()

port=12345

s.connect((host,port))

password=(s.recv(1024).decode())

text=s.recv(1024).decode()

count=0

for i in range(0,22):
    password=password+"x"
pas=list(password)

l=len(text)
text1=list(text)

text2=[]
for i in range(0,int(l/3)):
    text2.append(text1[i])
textf=''.join(text2) #first part of text == textf

text4=[]
for i in range(int(l/3),int(2*l/3)):
    text4.append(text1[i])
textff=''.join(text4) #second part of text == textff

text6=[]
for i in range(int(2*l/3),int(l)):
    text6.append(text1[i])
textfff=''.join(text6) #third part of text == textfff

print("the three parts of the plaintext we recieved\n")
print(textf)
print(textff)
print(textfff,"\n\n\n")

k=[]
for i in pas:
   if i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
       k.append(int(i))
       count=count+1
   if count==3:
       break
print(k)
x1=k[0]%3
x2=k[1]%3
x3=k[2]%3

#-----------------for encryption---------------------------------------
print("encryption of those parts of message on the basis of key")
final_encrypt = []
# algorithm for first part
count1=len(textf)
if x1==0:
 plaintext =textf
 key=password
 key = key.encode('utf-8')
 aes = pyaes.AESModeOfOperationCTR(key)
 ciphertextf = aes.encrypt(plaintext)
 print("Encrypted with AES algorithm")
 final_encrypt.append(ciphertextf)
 print(ciphertextf,"\n")
 
elif x1==1:
 key= bytes(password, 'utf-8')
 cipher = blowfish.Cipher(key)
 if len(textf)%8!=0:
     for i in range(0,8-len(textf)%8):
         textf=textf+"#"
 plaintext =bytes(textf, 'utf-8')
 encrypted_data1 = b"".join(cipher.encrypt_ecb(plaintext))
 print("Encrypted with Blowfish algorithm")
 final_encrypt.append(encrypted_data1)
 print(encrypted_data1,"\n")
 
elif x1==2:
 p1=[]
 if len(textf)%8!=0:
     for i in range(0,8-len(textf)%8):
         textf=textf+"#"
 
 for i in range(0,8):
     p1.append(pas[i])
 pa1=''.join(p1)
 key=pa1
 key = key.encode('utf-8')
 d = des(key)
 ciphertexta1 = d.encrypt(textf)
 final_encrypt.append(ciphertexta1)
 print("Encrypted with DES algorithm")
 print(ciphertexta1,"\n")
 
#for second part
count2=len(textff)
if x2==0:
 plaintext =textff
 key=password
 key = key.encode('utf-8')
 aes = pyaes.AESModeOfOperationCTR(key)
 ciphertextff = aes.encrypt(plaintext)
 final_encrypt.append(ciphertextff)
 print("Encrypted with AES algorithm")
 
 print(ciphertextff,"\n")
 
elif x2==1:
 key= bytes(password, 'utf-8')
 cipher = blowfish.Cipher(key)
 if len(textff)%8!=0:
     for i in range(0,8-len(textff)%8):
         textff=textff+"#"
 plaintext =bytes(textff, 'utf-8')
 encrypted_data2 = b"".join(cipher.encrypt_ecb(plaintext))
 print("Encrypted with Blowfish algorithm")
 final_encrypt.append(encrypted_data2)
 print(encrypted_data2,"\n")
 
elif x2==2:
 p2=[]
 if len(textff)%8!=0:
     for i in range(0,8-len(textff)%8):
         textff=textff+"#"

 for i in range(0,8):
     p2.append(pas[i])
 pa2=''.join(p2)
 key=pa2
 key = key.encode('utf-8')
 d = des(key)
 ciphertexta2 = d.encrypt(textff)
 print("Encrypted with DES algorithm")
 final_encrypt.append(ciphertexta2)
 print(ciphertexta2,"\n")
 
#for third part
count3=len(textfff)
if x3==0:
 plaintext =textfff
 key=password
 key = key.encode('utf-8')
 aes = pyaes.AESModeOfOperationCTR(key)
 ciphertextfff = aes.encrypt(plaintext)
 final_encrypt.append(ciphertextfff)
 print("Encrypted with AES algorithm")
 print(ciphertextfff,"\n")

elif x3==1:
 key= bytes(password, 'utf-8')
 cipher = blowfish.Cipher(key)
 if len(textfff)%8!=0:
     for i in range(0,8-len(textfff)%8):
         textfff=textfff+"#"
 plaintext =bytes(textfff, 'utf-8')
 encrypted_data3 = b"".join(cipher.encrypt_ecb(plaintext))
 final_encrypt.append(encrypted_data3)
 print("Encrypted with Blowfish algorithm")
 print(encrypted_data3,"\n")
 
elif x3==2:
 p3=[]
 if len(textfff)%8!=0:
     for i in range(0,8-len(textfff)%8):
         textfff=textfff+"#"

 for i in range(0,8):
     p3.append(pas[i])
 pa3=''.join(p3)
 key=pa3
 key = key.encode('utf-8')
 d = des(key)
 ciphertexta3 = d.encrypt(textfff)
 print("Encrypted with DES algorithm")
 final_encrypt.append(ciphertexta3)
 print(ciphertexta3,"\n")
print("\n\n\n")


print("The final array containing encrypted data")
print(final_encrypt)
print("\n\n\n")
#--------------------for decryption-----------------------
choice="yes"
final_decrypt = "";
if choice=="yes":
 if x1==0:
     aes = pyaes.AESModeOfOperationCTR(key)
     decryptedf = aes.decrypt(ciphertextf)
     print("Decrypted with AES algorithm")
     final_decrypt = final_decrypt + str(decryptedf.decode('utf-8'))
     print(decryptedf.decode('utf-8'),"\n")
 elif x1==1:
     print("Decrypted with Blowfish algorithm")
     dec1 = (b"".join(cipher.decrypt_ecb(encrypted_data1)))
     final_decrypt = final_decrypt + dec1.decode('utf-8')
     print(dec1[0:count1].decode('utf-8'),"\n")
 elif x1==2:
     decrypted1 = d.decrypt(ciphertexta1)
     print("Decrypted with DES algorithm")
     final_decrypt = final_decrypt + str(decrypted1.decode('utf-8'))
     print(decrypted1[0:count1].decode('utf-8'),"\n")

 if x2==0:
     aes = pyaes.AESModeOfOperationCTR(key)
     decryptedff = aes.decrypt(ciphertextff)
     print("Decrypted with AES algorithm")
     final_decrypt = final_decrypt + str(decryptedff.decode('utf-8'))
     print(decryptedff.decode('utf-8'),"\n")
 elif x2==1:
     print("Decrypted with Blowfish algorithm")
     dec2 = (b"".join(cipher.decrypt_ecb(encrypted_data2)))
     final_decrypt = final_decrypt + str(dec2.decode('utf-8'))
     print(dec2[0:count2].decode('utf-8'),"\n")
 elif x2==2:
     decrypted2 = d.decrypt(ciphertexta2)
     print("Decrypted with DES algorithm")
     final_decrypt = final_decrypt + str(decrypted2.decode('utf-8'))
     print(decrypted2[0:count2].decode('utf-8'),"\n")

 if x3==0:
     aes = pyaes.AESModeOfOperationCTR(key)
     decryptedfff = aes.decrypt(ciphertextfff)
     print("Decrypted with AES algorithm")
     final_decrypt = final_decrypt + str(decryptedfff.decode('utf-8'))
     print(decryptedfff.decode('utf-8'),"\n")
 elif x3==1:
     print("Decrypted with Blowfish algorithm")
     dec3 = (b"".join(cipher.decrypt_ecb(encrypted_data3)))
     final_decrypt = final_decrypt + str(dec3.decode('utf-8'))
     print(dec3[0:count3].decode('utf-8'),"\n")
 elif x3==2:
     decrypted3 = d.decrypt(ciphertexta3)
     final_decrypt = final_decrypt + str(decrypted3.decode('utf-8'))
     print("Decrypted with DES algorithm")
     print(decrypted3[0:count3].decode('utf-8'),"\n")

s.send(bytes("Thankyou we securely recieved and encrypted your message",'utf-8'))
s.close()





