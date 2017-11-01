__author__ = 'mustafaduran'

import math
import numpy as np
from numpy import array
from numpy import matrix
from numpy import linalg as LA


def myptw (a,sample_profile,target_profile):

    n=len(sample_profile)
    print n
    A_=array([1,1,1])
    dA=array([A_]).T

    while LA.norm(dA)>0.01:

        print LA.norm(dA)
        t=range(1,n+1)
        t=array([t]).T
        print "t:"
        print t
        w=a[0]+a[1]*t+a[2]*t**2
        #print "w:"
        #print w
        for i in range(n-2):

            #deger=w(i)
            alt=np.fix(w[i])
            alt=int(alt)

            if alt<=0:
                alt=1
                #S=S+1000000

            if alt>=n-1:
                alt=n-1
                #S=S+1000000;

            ust=alt+1
            [i, alt, ust]
            #n.__int__()
            xx=np.zeros((n,2))
            #print xx
            #xx=[[0 for deneme in range(n)] for deneme in range(n)]
            xx[i,0]=int(sample_profile[alt])+(int(sample_profile[ust]) - int(sample_profile[alt]))*(w[i]-alt)
            #print "xx["+str(i)+"][0]:"
            #print xx


        dxx=np.diff(xx,n=1,axis=0)
        print "dxx:"
        print dxx.shape
        t=range(1,n-1)
        t=array([t]).T
        target_profile=target_profile[1:n-1]
        #print target_profile
        #print "xx:"
        #print xx
        xx=xx[0:n-2,0]

        xx=array([xx]).T
        print "xx"
        print xx.shape
        target_profile = [int(numeric_string) for numeric_string in target_profile]
        print "target:"
        target_profile=np.array(target_profile)
        print target_profile

        A=np.zeros((3,2))
        #A= [[0 for deneme in range(1)] for deneme in range(3)]
        #t_p=matrix(target_profile)
        #xx_=matrix(xx)
        A0=np.subtract(target_profile,xx)
        print "A0:"
        print A0.shape
        print "dxx:"
        print dxx
        A[0,0]=sum((A0)*dxx)
        A[1,0]=sum((target_profile-xx)*dxx*t)
        A[2,0]=sum((target_profile-xx)*dxx*t**2)

        B={}

        B[0,0]=sum(dxx**2)
        B[0,1]=sum(dxx**2.*t)
        B[0,2]=sum(dxx**2.*t**2)

        B[1,0]=sum(dxx**2.*t)
        B[1,1]=sum(dxx**2.*t**2)
        B[1,2]=sum(dxx**2.*t**3)

        B[2,0]=sum(dxx**2.*t**2)
        B[2,1]=sum(dxx**2.*t**3)
        B[2,2]=sum(dxx**2.*t**4)

        dA=LA.inv(B)*A
        a=a+dA

    return (xx,a)



