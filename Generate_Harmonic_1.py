import math
import numpy as np
import scipy
from scipy import spatial
from datetime import datetime
np.set_printoptions(threshold=np.nan)
def sqrt(x):
	return math.sqrt(x)
def nthmatrix(n):
	allpoints = np.load('vertices/all_vertices_it_' + str(n) + '.npy')
	allpointstree = scipy.spatial.cKDTree(allpoints, compact_nodes=True, copy_data=False, balanced_tree=True)
	length = len(allpoints)
	c = (4**(n))
	boundmeasure = ((1./4.)**(-n))
	intmeasure = ((1./9.)**(-n))/boundmeasure
	matrix = np.zeros((length, length))
	for i in xrange(0,length):
		a = allpointstree.query_ball_point(allpoints[i],1.1*(1./3.**(n-1)))
		for x in xrange(0,len(a)):
			matrix[i,a[x]] = -1.
			pass
	for i in xrange(0,length):
		matrix[i,i]=0
		if np.sum(matrix[i,:])== -2.:
			matrix[i,:] *= c
			matrix[:,i] *= c
		if (np.sum(matrix[i,:])== -6.):
			matrix[i,:] *= intmeasure
	for i in xrange(0,length):
		if np.sum(matrix[i,:]) == -5.:
			neighbors = np.array(allpointstree.query_ball_point(allpoints[i],1.1*(1./3.**(n-1))))
			mask = np.isin(neighbors,allpoints[i],invert=True)
			neighbors = neighbors[mask]
			for x in xrange(0,len(neighbors)):
				if len(np.array(allpointstree.query_ball_point(allpoints[neighbors[x]],1.1*(1./3.**(n-1))))) == 6:
					matrix[i,neighbors[x]] *= c
					matrix[neighbors[x],i] *= c
	for i in xrange(0,length):
		matrix[i,i] = -1.*np.sum(matrix[i,:])
	uppertree = scipy.spatial.cKDTree(np.load('vertices/upperhalf_vertices_it_' + str(n)+'.npy'), compact_nodes=True, copy_data=False, balanced_tree=True)
	removeindex = np.array([0])
	for i in xrange(0,len(allpoints)):
		aboveaxis = len(uppertree.query_ball_point(allpoints[i],.1*(1./3.**(n-1))))
		if aboveaxis == 0:
			removeindex = np.append(removeindex,i)
		pass
	matrix = np.delete(matrix,removeindex,0)
	matrix = np.delete(matrix,removeindex,1)
	allpoints = np.delete(allpoints,removeindex,0)
	h1step1 = np.zeros(len(allpoints))
	h1step2 = np.array([])
	boundpart = np.array([])
	uppertree = scipy.spatial.cKDTree(np.load('vertices/upperhalf_vertices_no_x_axis_it_' + str(n)+'.npy'), compact_nodes=True, copy_data=False, balanced_tree=True)
	for x in xrange(0,len(allpoints)):
		if allpoints[x][1] <= .000001:
			if allpoints[x][0] < 0:
			    h1step1[x] = -1
			elif allpoints[x][0] > 0:
			    h1step1[x] = 1
			elif allpoints[x][0] == 0:
			    origin = x
			h1step2 = np.append(h1step2,int(x))
	matrix = matrix*2.*boundmeasure
	h1step2 = h1step2.astype(int)
	matrix = np.delete(matrix,h1step2,axis=0)
	truncatedmat = np.delete(matrix,h1step2,axis=1)
	return matrix, allpoints, h1step1, truncatedmat, origin, h1step2

def harmonic1(n):
	matrix, xy, h1step1, truncatedmat, origin, h1step2 = nthmatrix(n)
	y = -1.*np.dot(matrix,h1step1)
	h1form = np.linalg.solve(truncatedmat,y)
	xyz = np.around(np.real(np.append(xy,np.vstack(np.empty(len(xy))),axis=1)),decimals=6)
	k=0
	for x in xrange(0,len(xy)):
		if xyz[x][1] <= .000001:
			print x
			xyz[x][2] = h1step1[x]
		else:
			xyz[x][2] = h1form[k]
			k += 1
	return xyz
for x in xrange(2,6):
    tosave = harmonic1(x)
    np.savetxt("Harmonic_1/Harmonic_it_" + str(x),np.real(np.around(tosave,decimals=6)),delimiter=",")
    np.save("Harmonic_1/Harmonic_it_" + str(x),tosave)
