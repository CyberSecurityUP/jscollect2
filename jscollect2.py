#coding: latin-1
import socket
import os
import sys
from googlesearch import search
import vulners
import json
import time
import requests
import base64

def main():
	os.system("clear")
	print("""
  ____      _  _             ____ ___      _ _____ 
 / ___|_ __| || | _____   _ / ___/ _ \  __| |___ / 
| |   | '__| || ||_  / | | | |  | | | |/ _` | |_ \ 
| |___| |  |__   _/ /| |_| | |__| |_| | (_| |___) |
 \____|_|     |_|/___|\__, |\____\___/ \__,_|____/ 
                      |___/ Joas Antonio dos Santos
Equipe Cyber Security UP
			""")

main()

def dork():
	code = str(input("[!] Digite a dork: "))
	time.sleep(2)
	print("Efetuando a busca...")
	time.sleep(2)
	for a in search(code,stop=20):
		print("> {}", form(x))

def vuln():
	code = str(input("Digite o que deseja buscar: "))
	api = vulners.Vulners()
	print("Efetuando a busca...")
	pesquisa = api.search(code,limit=10)
	for a in pesquisa:
		time.sleep(1)
		print("\n[*] Title: {}".format(a['title']))
		print("[*] ID: {}".format(a['id']))
		print("[*] Href: {}".format(a['href']))

def ba64deco():
	code = str(input("[!] Entre com o codigo: "))
	var_base64 = base64.ba64decode(code.encode("utf-8"))
	print("[+] Decrypt: {}".format(var_base64.decode("utf-8")))

def ba64enco():
	code = str(input("[!] Entre com o texto que deseja encodar"))
	var_base64 = base64.ba64encode(code.encode("utf-8"))
	print("[+] Encrypt: {}".format(var_base64.decode("utf-8")))

def extract():
	code = str(input("[!] Digite o site: "))
	var_ok = requests.get(code)
	if(var_ok.status_code==200):
		r = requests.get("https://api.hackertarget.com/pagelinks/?q={}".format(code))
		time.sleep(1)
		print("Pesquisando...")
		print(r.text)
	else:
		print("[*] Site invalido.")

def dns():
	code = str(input("[!] Digite o site desejado: "))
	r = requests.get("https://api.hackertarget.com/dnslookup?q={}".format(code))
	print(r.text)

def whois():
	s = socket.socket(scoket.AF_INET, socket.SOCK_STREAM)
	s.connect(("200.160.2.3",43))
	s.send(sys.argv[1]+'\r\n')
	resp = s.recv(1024)
	print(resp)

menu = """
1 - Dork Scan
2 - Search Exploit
3 - Base64 decode
4 - Base64 encode
5 - Extract website links
6 - DNS lookup
7 - Whois
"""

print(menu)
code2 = int(input("<jsconsole>"))
if(code2==1):
	dork()
if(code2==2):
       vuln()
if(code2==3):
	ba64deco()
if(code2==4):
	ba64enco()
if(code2==5):
	extract()
if(code2==6):
	dns()
if(code2==7):
	whois()
