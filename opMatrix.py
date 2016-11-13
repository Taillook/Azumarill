class OpMatrix:
	def __init__(self):
		self.mtr=[]

	def append(self,lst):
		self.mtr.append(lst)

	def __str__(self):
		smtr = ""
		for i in xrange(len(self.mtr)):
			smtr+=("|"+" ".join(map(str,self.mtr[i]))+"|")
			if i!=len(self.mtr)-1: smtr+="\n"
		return smtr

def finDet2(a,b,c,d):
	print "|"+str(a)+" "+str(b)+"|"
	print "|"+str(c)+" "+str(d)+"|\n"
	print "det=("+str(a)+"x"+str(d)+")-"+"("+str(b)+"x"+str(c)+")\n   ="+str((a*d)-(b*c))

def findDet3(a,b,c,d,e,f,g,h,i):
	print "|"+str(a)+" "+str(b)+" "+str(c)+"|"
	print "|"+str(d)+" "+str(e)+" "+str(f)+"|"
	print "|"+str(g)+" "+str(h)+" "+str(i)+"|\n"

if __name__ == '__main__':
	mtr = OpMatrix()
	mtr.append(map(int,raw_input().split()))
	mtr.append(map(int,raw_input().split()))
	print mtr
	finDet2(1,2,3,4)