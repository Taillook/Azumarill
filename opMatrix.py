# coding: utf-8
import sys


class OpMatrix(object):

    def __init__(self, values):
        self.mtr = values

    def __add__(self, value):
        print "__add__"
        return OpMatrix([[self.mtr[j][i] + value.mtr[j][i] for i in range(len(self.mtr))] for j in range(len(self.mtr))])

    def __sub__(self, value):
        print "__sub__"
        return OpMatrix([[self.mtr[j][i] - value.mtr[j][i] for i in range(len(self.mtr))] for j in range(len(self.mtr))])

    def __str__(self):
        # オブジェクトを参照された際に文字列化した行列を返す
        return self.strMatrix()

    def copy(self):
        return OpMatrix(self.mtr)

    def strMatrix(self):
        # 行列を文字列として表現するための変数
        smtr = ""
        # smtr内の文字列生成
        for i in xrange(len(self.mtr)):
            # 行列内の最大値を取得し、フォーマット用文字列を生成
            formatStr = "{0:" + str(len(str(max(max(self.mtr))))) + "d}"
            # 行列内の数の桁数が最大の桁数に合うように文字列を生成
            munStr = [formatStr.format(self.mtr[i][j]) for j in range(len(self.mtr[i]))]
            # 改行の有無を指定
            isEnter = "\n" if i != len(self.mtr) - 1 else ""
            # smtrに行ごとの文字列を追加
            smtr += ("|" + " ".join(munStr) + "|" + isEnter)
        return smtr

    def printMatrix(self):
        print self.strMatrix()

    def findDet(self):
        #文字列化した数値の長さ
        lenNumStr = len(str(max(max(self.mtr))))

        # 行列内の最大値を取得し、フォーマット用文字列を生成
        formatStr = "{0:" + str(lenNumStr) + "d}"

        self.printMatrix()

        if len(self.mtr[0]) == 2:
            det = (self.mtr[0][0] * self.mtr[1][1]) - \
                (self.mtr[0][1] * self.mtr[1][0])
            print "det=(" + str(self.mtr[0][0]) + "x" + str(self.mtr[1][1]) + ")-" + \
                "(" + str(self.mtr[0][1]) + "x" + str(self.mtr[1][0]) + ")\n" + \
                "   =" + str(det)
            return det
        elif len(self.mtr[0]) == 3:
            sp1 = self.mtr[0][0] * self.mtr[1][1] * self.mtr[2][2]
            sp2 = self.mtr[0][1] * self.mtr[1][2] * self.mtr[2][0]
            sp3 = self.mtr[0][2] * self.mtr[1][0] * self.mtr[2][1]
            sm1 = self.mtr[0][0] * self.mtr[1][2] * self.mtr[2][1]
            sm2 = self.mtr[0][1] * self.mtr[1][0] * self.mtr[2][2]
            sm3 = self.mtr[0][2] * self.mtr[1][1] * self.mtr[2][0]

            det = sp1 + sp2 + sp3 - sm1 - sm2 - sm3

            lenUnderBar = lenNumStr * 9 + 2 + len(str(det))

            print "+|" + formatStr.format(self.mtr[0][0]) + " x " + formatStr.format(self.mtr[1][1]) + " x " + formatStr.format(self.mtr[2][2]) \
                  + " = " + str(sp1) + "\n" \
                  + "+|" + formatStr.format(self.mtr[0][1]) + " x " + formatStr.format(self.mtr[1][2]) + " x " + formatStr.format(self.mtr[2][0]) \
                  + " = " + str(sp2) + "\n" \
                  + "+|" + formatStr.format(self.mtr[0][2]) + " x " + formatStr.format(self.mtr[1][0]) + " x " + formatStr.format(self.mtr[2][1]) \
                  + " = " + str(sp3) + "\n" \
                  + "-|" + formatStr.format(self.mtr[0][0]) + " x " + formatStr.format(self.mtr[1][2]) + " x " + formatStr.format(self.mtr[2][1]) \
                  + " = " + str(sm1) + "\n" \
                  + "-|" + formatStr.format(self.mtr[0][1]) + " x " + formatStr.format(self.mtr[1][0]) + " x " + formatStr.format(self.mtr[2][2]) \
                  + " = " + str(sm2) + "\n" \
                  + "-|" + formatStr.format(self.mtr[0][2]) + " x " + formatStr.format(self.mtr[1][1]) + " x " + formatStr.format(self.mtr[2][0]) \
                  + " = " + str(sm3)

            for i in xrange(lenUnderBar):
                if i == 0:
                    sys.stdout.write(" ")
                elif i == lenUnderBar - 1:
                    print ""
                else:
                    sys.stdout.write("-")

            print " =" + str(det)

            return det

if __name__ == '__main__':
    print "Please enter the dimension number of the matrix and matrix."
    print "ex:\n2\n1 2\n3 4\n"

    dimensionNum = raw_input()

    if dimensionNum.isdigit():
        dimensionNum = int(dimensionNum)
    else:
        print "Error"
        exit()

    if dimensionNum != 2 and dimensionNum != 3:
        print "Error"
        exit()

    mtr = OpMatrix([[int(j) for j in raw_input().split()] for i in xrange(dimensionNum)])
    mtr2 = mtr.copy()
    print mtr is mtr2
    print (mtr + mtr2).findDet()
