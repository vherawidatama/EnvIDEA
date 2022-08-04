import socket
import tqdm
import os
import threading
import hashlib
import itertools
import sys
import timeit
from datetime import datetime
from Crypto import Random
from Crypto.PublicKey import RSA
from CryptoPlus.Cipher import IDEA

def decrypt(filename):
    file_path = "dec"+filename[3:]
    key = 'test123456789012'
    with open(filename, 'rb') as input_file:
        newmess = input_file.read()
        decoded = newmess.decode("hex")
        ideaDecrypt = IDEA.new(key, IDEA.MODE_CTR, counter=lambda: key)
        dMsg = ideaDecrypt.decrypt(decoded)
        with open("file/"+file_path, 'wb') as output_file:
            output_file.write(dMsg)

# device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# create the server socket
# TCP socket
s = socket.socket()

# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))

# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(5)
print("[*] Listening as {}:{}".format(SERVER_HOST, SERVER_PORT))
#print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# accept connection if there is any
client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
#print(f"[+] {address} is connected.")
print("[+] {} is connected.".format(address))

# receive the file infos
# receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
# remove absolute path if there is
filename = os.path.basename(filename)
# convert to integer
filesize = int(filesize)

# start receiving the file from the socket
# and writing to the file stream
progress = tqdm.tqdm(range(filesize), "Receiving {}".format(filename), unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))

# close the client socket
client_socket.close()
# close the server socket
s.close()


#startting time
now = datetime.now()
current_time = now.strftime("%d/%m/%y %H:%M")

print("\n")
print("Decrypting File ......")
print("Current Time =", current_time)

t1_start = timeit.default_timer()
decrypt('encpublic.txt')
t1_stop = timeit.default_timer()
print("Elapsed time in seconds:", t1_stop-t1_start)
print("File Decrypted")
print("\n")


os.remove("encpublic.txt")
