#######################################
"""
	   Coded By Z3US
     Hehe ;)
"""
#######################################
#import module
import sys
import requests
import time
import random
import os

# Warna ! Color
B = '\033[1;34m'  #Blue   ! Blue
R = '\033[31m'    #Red    ! Red
G = '\033[32m'    #Green  ! Green
W = '\033[0m'     #White  ! White
Y = '\033[33;5m'  #Yellow ! Yellow
P = '\033[95m'    #Purple ! Purple
C = '\033[36;1m'  #Cyan   !

lo = " Enter Target"+R+" ["+B+" Without https / http"+R+" ]\n "+B+"Example:"+G+" github.com"+C
target = R+"["+C+"Target"+R+"]"+G+" => "+C

def type(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

def banner():
	os.system("clear")
	print Y+"""
	           0000000
        	 00       00
	        0"""+R+"""  ()  () """+Y+"""  0
	       0             0
	        0 """+R+"""  @@@@ """+Y+"""   0
	       0 00       00 0
	     0     0     0     00
	    0 ------------------- 0
	     0 """+G+""" Coded By Z3US"""+Y+"""  0
	      \  """+G+"""Hehe """+Y+"""/
	     """+P+""" -------------------
	     | """+C+"""   Admin Finder """+P+"""  |
              ~~~~~~~~~~~~~~~~~~~
	"""+B

def go():
	banner()
	type(lo)
	target = raw_input(target)
	print
	time.sleep(1.5)
	asu="wordlist.txt"
	f=open(asu,'r')
	content=f.read()
	x=kontent.split("\n")
	for i in x:
	      #cek(url+"/"+i)
	      url=target+"/"+i
	      ree=requests.get("http://"+str(url)).status_code
	      if ree == 200:
	              print G+"[+] Found | url : "+url+" | code :",ree
	              #raw_input("Press Any Key To Countinue.")
	      else:
	              print R+"[-] Not Found | url : http://"+url

try:
   go()
except KeyboardInterrupt:
   print ("      "+W+"("+R+" Ctrl + C "+W+")"+R+" Detected"+W+"")
   exit()
except EOFError:
   print ("\n      "+W+"("+R+" Ctrl + D "+W+")"+R+" Detected"+W+"")
except requests.exceptions.ConnectionError:
  print ("\n      "+W+"("+R+" No "+W+")"+R+" Conection"+W+"")
except requests.exceptions.InvalidURL:
  print ("\n      "+W+"("+R+" No "+W+")"+R+" Url"+W+"")
