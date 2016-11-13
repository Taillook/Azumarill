# coding: utf-8
import math
class OpMatrix(object):
	def __init__(self,values):
		self.mtr=values

	def __add__(self,value):
		print "__add__"
		return OpMatrix([[self.mtr[j][i]+value.mtr[j][i] for i in range(len(self.mtr))] for j in range(len(self.mtr))])

	def __sub__(self,value):
		print "__sub__"
		return OpMatrix([[self.mtr[j][i]-value.mtr[j][i] for i in range(len(self.mtr))] for j in range(len(self.mtr))])

	def __str__(self):
		#オブジェクトを参照されたとき用の変数
		smtr = ""
		#smtr内の文字列生成
		for i in xrange(len(self.mtr)):
			#行列内の最大値を取得し、フォーマット用文字列を生成
			formatStr="{0:"+str(len(str(max(max(self.mtr)))))+"d}"
			#行列内の数の桁数が最大の桁数に合うように文字列を生成
			munStr=[formatStr.format(self.mtr[i][j]) for j in range(len(self.mtr[i]))]
			#改行の有無を指定
			isEnter="\n" if i!=len(self.mtr)-1 else ""
			#smtrに行ごとの文字列を追加
			smtr+=("|"+" ".join(munStr)+"|"+isEnter)
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
	mtr = []
	print "Please enter the dimension number of the matrix and matrix."
	print "ex:\n2\n1 2\n3 4\n"
	[mtr.append(map(int,raw_input().split())) for i in xrange(input())]
	mtr = OpMatrix(mtr)
	mtr2 = mtr
	print mtr-mtr2
	#finDet2(1,2,3,4)