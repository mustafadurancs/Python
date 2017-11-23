__author__ = 'mustafaduran'
import matplotlib.pyplot as plt
import ptw
import file_read
import numpy as np
from numpy import array
from numpy import matrix

sample,target=file_read.TSV_Read("data.tsv")

#sample=array(sample)
#target=array(target)
sample=sample[0:20]
target=target[0:20]
a=array ([0,1,0])
a=array([a]).T
#print sample
b,xx=ptw.myptw(a,sample,target)
plt.plot(xx)
plt.show()
#plt.plot(xx)
