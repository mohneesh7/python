# A Pig Latin Converter Code
# Interesting ? Of_Course_Not
# mohneesh7

# Author : Mohneesh S
# Date   : Tue Sep 19, 13:59
# Program: Pig Latin Converter
#		   Using Functional Programming		   

# Description : Enter any Sentence and press [ENTER], 
#				the following output will give you the [ig-pay atin-lay] version of pig latin.


def pig_latiner(a):
	temp_list=[]
	for i in a:
		count=0
		temp=''
		if(i[count] not in ['a','e','i','o','u']):
			temp=temp+i[count]
			i=i[count+1:]
		count+=1
		i=i+'-'+temp+"ay"
		temp_list.append(i)
	return temp_list
def main():	
	r=[x for x in raw_input("Enter a senternce :\n").split()]
	l=pig_latiner(r)
	print ' '.join(l)

main()
