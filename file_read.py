__author__ = 'mustafaduran'
import numpy
def TSV_Read(Input_File):
    dosya=open(Input_File,"r")
    indis=0
    target=list()
    sample=list()
    for line in dosya:
        satir= line.split()
        target.append(satir[0])
        sample.append(satir[1])
        indis=indis+1
   # print Dosya.read()
    return (sample,target)

TSV_Read("data.tsv")

