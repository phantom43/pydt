import json
import os
from test import *

remember = "admin.json"

def login():
	os.system("clear")
	user = input("enter username# ")
	pw = input("enter your password# ")
	if user == "senja" and pw == "1232123":
		talk()
		print("welcome to admin panel", user)
		aflog()
	else:
		os.system("clear")
		print("your username or password is wrong check it!!!")
		print("who are u ? are u admin?")

def aflog():
	options()
	option = input("chose an option# ")
	if option == "1":
#		print("debug!")
		with open('index.json') as f:
			deta = json.load(f)
		for i in deta["data"]:
			print(i)
		input("enter to go back")
		os.system("clear")
	if option == "2":
#		print("debug!")
		with open('index.json') as f:
			deta = json.load(f)
		for i in deta["data"]:
			print(i['nama'])
		input("enter to go back")
		os.system("clear")
	if option == "3":
#		print("debug!")
		with open('index.json') as f:
			deta = json.load(f)
		for i in deta["data"]:
			print(i['nama'], ":")
			print(i['tgl'])
		input("enter to go back")
		os.system("clear")
	if option == "4":
#		print("debug!")
		with open('index.json') as f:
			deta = json.load(f)
		for i in deta["data"]:
			print(i["nama"], ":")
			print(i['email'])
		input("enter to go back")
		os.system("clear")
	aflog()
login()