import math
import numpy as np
import scipy
from scipy import spatial
from datetime import datetime

def upperhalf(n):
    removeindex = np.array([0])
    set1 = np.load('vertices/all_vertices_it_' + str(n) +'.npy')
    for x in xrange(0,len(set1)):
        if set1[x,1] <= -.00001:
            removeindex = np.append(removeindex,x)
    for x in xrange(0,len(removeindex)-1):
        set1 = np.delete(set1,removeindex[len(removeindex)-1],0)
        removeindex  = np.delete(removeindex,len(removeindex)-1,0)
    set1 = np.unique(np.around(set1,decimals=7),axis=0)
    return set1
for x in xrange(5,6):
    filename = 'vertices/upperhalf_vertices_it_' + str(x)+ '.npy'
    np.save(filename,upperhalf(x))