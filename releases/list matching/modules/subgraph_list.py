import requests
import json
import re
from functions import *

class subgraph_list():
	def __init__(self,endpoint,exchange):
		self.endpoint=endpoint
		self.exchange=exchange
		
	def build_list(self):
		print("building " + exchange + " token list "
		endpoint=self.endpoint
		l=[] #dummy list to store token data
		k=["1",""] #list of ID , ID=token address
		while k[-1]!=k[-2]:                          #till last id different from previous last Id
			t_query=query_builder(k[-1])  #build a valid subgraph query to retrieve a token list from the exchange
			temp=query_graph(t_query,endpoint)     #use the previous query to make an api request
			l=l + temp["data"]["tokens"]
			try:
				lastId=temp["data"]["tokens"][-1]["id"] #get Id of the last element of the generated token list
			except IndexError:
				break
			k.append(lastId)                     #add the last Id to the list of ID
		
		f=[i["symbol"].upper() for i in l] + [k[-1]] #extract tickers from the dummy list and add the Id of the last scraped token
		
		with open(self.exchange + "_tickers.txt", 'w') as w:
			w.writelines(s + "\n" for s in f)
		print("Done")
			
			
	def update_list():
		print("ypdating " + exchange + " token list "

		with open(self.exchange + "_tickers.txt", 'r') as w:  ##get old list
			old_list=w.read().splitlines() 
			
	####### build new list starting from the last element of the old list
		endpoint=self.endpoint
		l=[]
		k=["1",old_list[-1]]
		while k[-1]!=k[-2]:                          
			t_query=query_builder(k[-1])
			temp=query_graph(t_query, endpoint)     
			l=l + temp["data"]["tokens"]
			try:
				lastId=temp["data"]["tokens"][-1]["id"] 
			except IndexError:
				break
			k.append(lastId)                     
		
		new_list=[i["symbol"].upper() for i in l]

		f_list=old_list[:-1] + new_list + [k[-1]]  ### merging the old and new lists
		with open(self.exchange + "_tickers.txt", 'w') as w:
			w.writelines(s + "\n" for s in f_list)
		print("Done")			
			
	def __str__(self):
		return "Open the file:"+ self.exchange + "_tickers.txt"+", You must build the list first"
		
		
	def get():
		try:
			with open(self.exchange + "_tickers.txt", 'r') as w:
				temp=w.read().splitlines() 
			return temp
		except FileNotFoundError:
			print("File not found")
