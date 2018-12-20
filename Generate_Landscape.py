import math
import numpy as np
import scipy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy import spatial
from datetime import datetime
np.set_printoptions(threshold=np.nan)
def sqrt(x):
	return math.sqrt(x)
def lands(it, weight):
	laplace = np.load('laplacians/it_' + str(it) + '_weight_' + str(weight) + '.npy')

	lap1 = np.absolute(laplace)
	landvec2 = np.sum(lap1,axis=1)
	xy = np.load('vertices/all_vertices_it_' + str(it) + '.npy')
	print np.min(landvec2)
	landvec2 = np.append(xy,np.vstack(landvec2),axis=1)
	np.save("landscape/landscape_it_" + str(it) + "_weight_" + str(weight),landvec2)
	landvec2.astype('float32').tofile("landscape/landscape_it_" + str(it) + "_weight_" + str(weight) +  ".dat")
	return 

for x in xrange(2,5):
	lands(x,4**x)
