#!/usr/bin/env python3

import requests
import time
import random
import os
import sys

# ANSI Color Codes
BLUE = '\033[1;34m'
RED = '\033[31m'
GREEN = '\033[32m'
WHITE = '\033[0m'
YELLOW = '\033[33;5m'
PURPLE = '\033[95m'
CYAN = '\033[36;1m'

def typewriter(text):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.005, 0.02))

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(YELLOW + r"""
	           0000000
        	 00       00
	        0""" + RED + """  ()  () """ + YELLOW + """  0
	       0             0
	        0 """ + RED + """  @@@@ """ + YELLOW + """   0
	       0 00       00 0
	     0     0     0     00
	    0 ------------------- 0
	     0 """ + GREEN + """ Coded Cleanly """ + YELLOW + """  0
	      \  """ + GREEN + """Hehe""" + YELLOW + """  /
	     """ + PURPLE + """ -------------------
	     | """ + CYAN + """   Admin Finder """ + PURPLE + """  |
              ~~~~~~~~~~~~~~~~~~~
    """ + BLUE)

def find_admin_panels():
    banner()
    prompt = (
        f" Enter Target {RED}[{BLUE} Without https:// or http:// {RED}]\n"
        f"{BLUE} Example:{GREEN} github.com\n\n"
        f"{RED}[{CYAN}Target{RED}]{GREEN} => {CYAN}"
    )
    typewriter(prompt)
    
    try:
        target = input().strip()
        wordlist_path = "wordlist.txt"

        if not os.path.exists(wordlist_path):
            print(f"{RED}[-] Wordlist not found: {wordlist_path}{WHITE}")
            return

        with open(wordlist_path, 'r') as file:
            paths = [line.strip() for line in file if line.strip()]

        print(f"\n{CYAN}[!] Scanning {len(paths)} paths on {target}...\n{WHITE}")
        time.sleep(1.5)

        for path in paths:
            url = f"http://{target}/{path}"
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"{GREEN}[+] Found: {url} | Code: 200{WHITE}")
                else:
                    print(f"{RED}[-] Not Found: {url}{WHITE}")
            except requests.exceptions.RequestException as e:
                print(f"{RED}[-] Error accessing {url} | {e}{WHITE}")
    except KeyboardInterrupt:
        print(f"\n{WHITE}({RED}Ctrl + C{WHITE}) {RED}Interrupted{WHITE}")
    except EOFError:
        print(f"\n{WHITE}({RED}Ctrl + D{WHITE}) {RED}Input Closed{WHITE}")

if __name__ == "__main__":
    find_admin_panels()
