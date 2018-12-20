import math
import numpy as np
import scipy
from scipy import spatial
from datetime import datetime
np.set_printoptions(threshold=np.nan)
def sqrt(x):
	return math.sqrt(x)
def nthmatrix(n):
	inittime = datetime.now()
	allpoints = np.load('vertices/all_vertices_it_' + str(n) + '.npy')
	allpointstree = scipy.spatial.cKDTree(allpoints, compact_nodes=True, copy_data=False, balanced_tree=True)
	length = len(allpoints)
	c = (4**(n))
	boundmeasure = ((1./4.)**-n)
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
					matrix[i,x] *= c
					matrix[x,i] *= c
	for i in xrange(0,length):
		matrix[i,i] = -1.*np.sum(matrix[i,:])

	boundtree = scipy.spatial.cKDTree(np.load('vertices/boundary_it_' + str(n)+'.npy'), compact_nodes=True, copy_data=False, balanced_tree=True)
	removeindex = np.array([0])
	for i in xrange(0,len(allpoints)):
		aboveaxis = len(boundtree.query_ball_point(allpoints[i],.1*(1./3.**n)))
		if aboveaxis == 1:
			removeindex = np.append(removeindex,i)
		pass
	removeindex = np.delete(removeindex,0)
	matrix = np.delete(matrix,removeindex,0)
	matrix = np.delete(matrix,removeindex,1)
	allpoints = np.delete(allpoints,removeindex,0)
	endtime = datetime.now()
	print "It took " + str(endtime-inittime) + " to generate the matrix for level " + str(n)
	return 2.*boundmeasure*matrix, allpoints
def alleigvecs(n):
	matrix, xy = nthmatrix(n)
	inittime = datetime.now()
	vals, vecs = np.linalg.eig(matrix)
	inittime = datetime.now()
	idx = vals.argsort()[::-1]
	vals = np.real(np.around(vals[idx],decimals=6))
	print vals
	np.save('eigenvalues/dirichlet_eigvals_it_' + str(n), vals)
	np.savetxt('eigenvalues/dirichlet_eigvals_it_' + str(n), vals,delimiter=",")
	vals.astype('float32').tofile('eigenvalues/dirichlet_eigvals_it_' + str(n) +  ".dat")
	vecs = np.real(np.around(vecs[:,idx],decimals=6))
	bound = np.load('vertices/boundary_it_' + str(n) + '.npy')
	zbound = np.append(bound,np.vstack(np.zeros(len(bound))),axis=1)
	vecs.astype('float32').tofile('eigenvectors/all_dirichlet_vecs_it_' + str(n) +  ".dat")
	endtime = datetime.now()
	for i in xrange(0,len(xy)):
		print i
		around = np.append(xy,np.vstack(vecs[:,len(xy)-i-1]),axis=1)
		around = np.real(around)
		around = np.append(around,zbound,axis=0)
		filename = 'eigenvectors/dirichlet_it_' + str(n) + '_vector_' + str(i)
		np.save(filename, around)
		np.savetxt(filename, around,delimiter=",")
	print "It took " + str(endtime-inittime) + " to do the rest of indexing for level " + str(n)
	return around
for x in xrange(2,5):
	print x
	alleigvecs(x)
