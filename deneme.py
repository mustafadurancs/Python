__author__ = 'mustafaduran'
import math
import numpy as np
from numpy import array
from numpy import matrix
from dtw import dtw
import fastdtw
import file_read
from numpy import linalg as LA

from numpy.linalg import norm
#
# a=array ([0,1,0])
# b=array([a]).T
#
# print a
# print b
# t=range(1,10)
# t=array([t]).T
# print t
#
# m1 = [ [1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0] ]
# m2 = [ [2, 4, 6, 0], [1, 3, 5, 0], [0, -1, -2, 0] ]
# m3= [ 4*[0] for i in range(3) ]
# for i in range(3):
#     for j in range(4):
#         m3[i][j]= m1[i][j]+m2[i][j]
#
# print m3
#
# x=5
# y=6
# a=matrix('np.ones(x);np.zeros(y)')
# print a
x,y=file_read.TSV_Read("data.tsv")
#a1,a2=fastdtw(x, y, radius=1, dist=lambda a, b: abs(a - b))
a=9
#a.__int__()
x1 = np.zeros((a,2))
x1[0,0]=15
x1[0,1]=3
x11=x1[0:3,0]
x12=x1[0:3,1]
x11=x11*x12

print "x11:"
print np.diff(x11,n=1,axis=0)
x2 = np.arange(3.0)
#print np.subtract(x1, x2)