#!/usr/bin/python3
from subprocess import call
from collections import Counter
import MySQLdb
import MySQLdb as db
import subprocess as sp

import subprocess
import os
import os.path


import hashlib

import signal
import random
import httplib
import sys
import datetime
import time
import traceback
import base64
import urllib
from pprint import pprint
import socket
import platform
import tempfile
# catch stderr
from subprocess import PIPE as pipe


#doraemon
class StrTestInPython:
  strVal = "This is a python"
  

  def capitalizeWord(self):
	call(["clear", ""])
	sentence = raw_input("Enter a sentence, I will capitalize each word of the given sentence = : ")
	print "sentence = : %s, Length = : %d "%(sentence, len(sentence))
	sentence = sentence.lower()
	words = ""
	wordCntr = 0
	for i in range(0, len(sentence)):
		val = sentence[i:i+1]
		if(val == ' '):
			wordCntr = 0

		else:
			if(wordCntr ==0):
				val = val.upper();
				wordCntr += 1

		words = words + val 
	#print "val = : %s " %(val)
	print "See result using logic = : %s"%(words)   

	val2 = sentence.capitalize();
	print "See result using inbuilt method capitalize() = : ",val2




  def countOccurences(self):
	sentence = raw_input("Enter a sentence = : ")
	search = raw_input("Enter the word to search = : ")
	sentence = sentence.lower();
	search = search.lower();
	words = ""
	occurences = 0
	search = search.strip(' ')
	sentence = sentence.strip(' ')
	searchLen = len(search)
	
	for i in range(len(sentence)):
		words = sentence[i:i+len(search)];
		if(words == search):
			occurences += 1
		
	print "\nOccurences of %s in the sentence \'%s\' is %d "%(search,sentence,occurences)       
  




  def letterFreqTest(self):
	sentence = raw_input("Enter a sentence = : ")
	sentence = sentence.lower()
	print "Sentence = : %s"%(sentence)
	map = {}
	for i in range(len(sentence)):
		letter = sentence[i:i+1];
		freq = map.get(letter, 0)
		map[letter] = freq + 1;

	
	descSortedValues = sorted(map, key=map.get, reverse=True)
	print "See below data descending sort on values\n---------------------"
	for i in range(len(descSortedValues)):
		print "Letter = : %s >> Freq = : %d "%(descSortedValues[i], map[descSortedValues[i]])

	

  def reverseWord(self):

	word = raw_input("Enter a sentence = : ")
	cntr = (len(word))-1;
	reverse = ""
	for i in range(0, len(word)):
		letter = word[cntr];
		cntr = cntr - 1;
		#print "Letter from last = : %s"%(letter)
		reverse = reverse + letter;
	print "Reverse is = : %s "%(reverse)    



  def useradd(self,name, username, preferred_shell):
	#http://linoxide.com/linux-how-to/solution-linux-useradd-error-cannot-lock-etcpasswd-try-again-later/
	
	removed_dir = "/home/deleted:" + username
	home_dir = "/home/" + username
	useradd_suffix = "-m -d"

	#print "home_dir = : ",home_dir    
	#print "removed_dir = : ",removed_dir    

	# restore removed home directory
	if not os.path.isdir(home_dir) and os.path.isdir(removed_dir):
		print "Condition Matched"

		qexec(["/bin/mv", removed_dir, home_dir])
	
	if os.path.isdir(home_dir):
		useradd_suffix = ""
	

	#print "useradd_suffix = : ",useradd_suffix   
	cmd = ["sudo /usr/sbin/useradd ", useradd_suffix,
		
		" -c ", "varmaa-" + name,
		" -s ", preferred_shell if preferred_shell else "/bin/bash",
		" -g ", username]

	
#userName = "rajeevSir"
#prefereedShell = "/bin/bash"

	#newCommand2 = "sudo /usr/sbin/useradd rajeevSir -m -d /home/rajeevSir -c varmaa-rajeevSir -s /bin/bash "
	newCommand = "sudo /usr/sbin/useradd "+name+" -m -d "+home_dir +" -c varmaa-"+name +" -s "+preferred_shell + " -g "+name
	#print "newCommand = : ",newCommand


	commd = ""
	for i in cmd:
		#print i
		commd = commd + i

	
	
	newCommand2 = "sudo /usr/sbin/useradd rajeevSir2"
	#sp.check_output([i for i in newCommand2 if i])
	os.system(newCommand2)
	


  
  def qexec(cmd):
	print ("[varmaa] exec: \"" + " ".join(cmd) + '"')
	try:
		subprocess.check_call(cmd)
		print "Task completed..." 
	except Exception, e:
		print ("ERROR executing %s" % " ".join(cmd))
		print (e)
		print ("Retrying.. (varmaa.sh)")
	

call(["clear", ""])     
obj = StrTestInPython()


userName = "rajeevSir"
prefereedShell = "/bin/bash"
#obj.useradd(userName, userName, prefereedShell)

obj.capitalizeWord()
#obj.letterFreqTest()
#obj.reverseWord()
#obj.create_DbTable()
#obj.creatDataBase()
#obj.countOccurences()







