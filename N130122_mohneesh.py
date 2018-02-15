a = "<s> is mohneesh  a good   \
	 <s> boy and punk is  the mohneesh"
# a = a.insert(0,'<s>')
l=[]
a = a.split()
b = a[1:]
c = zip(a,b)
print "Bigrams :\n\t\t("+str(c)+")\n"
for i in range(len(c)):
	print "\tC(",c[i],")/C(",c[i][0],")"
	print "\t",c.count(c[i])/float(a.count(c[i][0])),"\n"
for i in a:
	l.append(a.count(i))
print "Nf Values :\n"
for i in range(max(l)+1):
	print "N",i," value: ",l.count(i)