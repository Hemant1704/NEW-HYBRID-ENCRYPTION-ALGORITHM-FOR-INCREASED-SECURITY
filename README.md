# NEW-HYBRID-ENCRYPTION-ALGORITHM-FOR-INCREASED-SECURITY
 A new encryption/decryption algorithm for securing data in storage systems which will provide an extra edge over the rest of the algorithms and will be more secured.
The main aim of this algorithm is to prevent any attacker to get the original message from the encrypted message in the storage.
Thus our algorithm is not based on just one single existing algorithm, it will use 3 algorithms to encrypt a single message. 
Encryption Phase:
It will be done by splitting the input message by the user into 3 parts and then based on the password entered by the user a modulo operation will be done with 3. This will then give us the choice to make for the algorithm to be chosen for that part.
Password – (10 digit password with min 3 digits in it)
(password digit)%3 : 0 :  AES algorithm on that part of text
                                   1 :   Blowfish Algorithm on that part of text
                                   2 :   DES algorithm in that part
  


