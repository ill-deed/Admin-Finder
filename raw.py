# Hehe ;)
# Copyright @s1_z3us
# coded lovingly by Z3US


#Import Module
import os
import requests


banner = """
 Welcome To My Tools
  Admin Finder
 Coded By Z3US
"""
os.system('clear')
print banner

#input target
target = raw_input('[Target]> ')

#open wordlist
f=open('wordlist.txt','r')
content=f.read()
x=content.split('\n')

for i in x:
     url=target+"/"+i
     code=requests.get(str(url)).status_code
     if code == 200:
             print "[+]Success | url : "+url
     else:
             print "[-] Fail | url:" + url
