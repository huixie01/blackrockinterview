def minMax(oplist, datalist) :

  returnlist=[]
  newlist=[]
  count=len(oplist)
  n=0

  while ( n < count) :
	print("n:"+str(n))
	data = datalist[n]
	op = oplist[n]
	print("data:"+str(data))

	if ( op == 'push' ):
		newlist.append(data)
	if ( op == 'pop' ):
		newlist.remove(data)
	
	print(newlist)
	if (len(newlist)>0 ):
		mn = min(newlist)
		mx = max(newlist)
		p = mn*mx
	else: 
		p=0
	returnlist.append(p)
	n += 1
  return returnlist

oplist=['push','pop','push','push','pop']
datalist=[3,3,1,4,1]

rl=minMax(oplist,datalist)
print(rl)
	
