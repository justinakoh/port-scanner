import socket
import subprocess
import sys
import array
from datetime import datetime

subprocess.call('clear', shell=True)
array = []

#asking for input
remote_host = input("Enter a remote host to scan. This can be a website or an IPv4 address: ")
IP_address = socket.gethostbyname(remote_host)

#Starting scanning banner
print( "-" * 90)
print( "Scanning the remote host.", IP_address, " Please wait, this takes a while!")
print( "-" * 90)
#checktime the scan started
t1 = datetime.now()

#Searching ports from 1 - 1025
try:
    for port in range(1, 1025):
        print("Checking port: ", port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((IP_address, port))
        if result == 0:
            array.append(port)
        sock.close()


#Checking for exceptions
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Could not connect to server")
    sys.exit()

t2 = datetime.now()

#printing out all the open ports in second banner
print( "-" * 30, "THE FOLLOWING PORTS ARE OPEN ", "-" * 30)
for open_port in array:
    print( "Port ", open_port, " is open")
print("Scanning completed in ", t2 - t1)
print( "-" * 90)
