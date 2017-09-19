# A simple text editor using simple file operations.

# Author      : Mohneesh S
# Date		  : Tue Sep 19, 22:54
# Program     : Text Editor using file read(), write() operations.
# Description : Follow on-console instructions to get to know the program better,
#				for,now only writing once is permitted, will improve it, feel free
#				fork.



import time,os
# Function for creating a file. Takes file name as input.
def create_new(file_name):
	f = open(file_name,'a+')
	write_file(file_name)
	f.close()

# Shows the contents of the file . Takes the file name as input.
def read_only(file_name):
	f = open(file_name,'r')
	f1 = f.read()
	return f1
	f.close()

# Writes the content inputted through console to the file_name provided
def write_file(file_name):
	f = open(file_name,'a+')
	while(True):
		s = raw_input()
		if(s):
			f.write('\n'+s)
		else:
			break
	f.close()

def main():
	choice =5
	while(choice!=0):
		print """ ********************************************************************
					 not-so-interactive-TEXT EDITOR v 1.0
	 ******************************************************************** 
	 \t 1] create a new file and add content
	 \t 2] read the content from the file 
	 Now please enter [1/2] \n"""
	 	choice = input(":")
	 	if(choice==1):
	 		file_name = raw_input("\tEnter file name with extension [abc.txt] :\n\t")
	 		create_new(file_name)
	 	if(choice==2):
	 		file_name = raw_input("\tEnter file name with extension [abc.txt] :\n\t")
	 		content=read_only(file_name)
	 		print content

main()