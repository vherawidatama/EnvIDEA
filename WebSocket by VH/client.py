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


def encrypt(filename):
    with open(filename, 'rb') as input_file:
        file_path = "enc"+filename
        mess = input_file.read()
        key = 'test123456789012'
        ideaEncrypt = IDEA.new(key, IDEA.MODE_CTR, counter=lambda :key)
        eMsg = ideaEncrypt.encrypt(mess)
        eMsg = eMsg.encode("hex").upper()
        with open("file/"+file_path, 'wb') as output_file:
            output_file.write(eMsg)

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "192.168.100.32"
# the port, let's use 5001
port = 5001
# the name of file we want to send, make surse it exists

# print(filename_ori)

print("Encrypting File ......")
now = datetime.now()
current_time = now.strftime("%d/%m/%y %H:%M")
print("Current Time =", current_time)
t1_start = timeit.default_timer()

#key
encrypt('public.txt')

t1_stop = timeit.default_timer()
print("Elapsed time in seconds:", t1_stop-t1_start) 
print("File Encrypted")
print("\n")
# send data
filename = "file/encpublic.txt"

# get the file size
filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

s.connect((host, port))

# send the filename and filesize
s.send("{}{}{}".format(filename, SEPARATOR, filesize).encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), "Sending {}".format(filename), unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()
