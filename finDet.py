def finDet2(a,b,c,d):
	print "|"+str(a)+" "+str(b)+"|"
	print "|"+str(c)+" "+str(d)+"|\n"
	print "det=("+str(a)+"x"+str(d)+")-"+"("+str(b)+"x"+str(c)+")\n   ="+str((a*d)-(b*c))

def findDet3(a,b,c,d,e,f,g,h,i):
	print "|"+str(a)+" "+str(b)+" "+str(c)+"|"
	print "|"+str(d)+" "+str(e)+" "+str(f)+"|"
	print "|"+str(g)+" "+str(h)+" "+str(i)+"|\n"

if __name__ == '__main__':
	finDet2(1,2,3,4)