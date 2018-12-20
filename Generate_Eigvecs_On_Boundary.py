import math
import numpy as np
import scipy
from scipy import spatial
from datetime import datetime

def boundorder(n):
    bpoints = np.load('vertices/boundary_it_' + str(n) + '.npy')
    boundtree = spatial.cKDTree(bpoints, compact_nodes=True, copy_data=False, balanced_tree=True)
    bound_order = np.array(boundtree.query_ball_point([-1.,0.],1.1*(1./3.**(n-1))))
    current_point = bpoints[bound_order[0]]
    for x in xrange(0,len(bpoints)):
        neighbors = np.array(boundtree.query_ball_point(current_point,1.1*(1./3.**(n-1))))
        mask = np.isin(neighbors,bound_order,invert=True)
        neighbors = neighbors[mask]
        if x == 0:
            for i in xrange(0,len(neighbors)):
                if (len(np.array(boundtree.query_ball_point(bpoints[neighbors[i]],1.1*(1./3.**(n-1)))))== 3):
                    current_point = bpoints[neighbors[i]]
                    bound_order = np.append(bound_order,neighbors[i])
        elif len(neighbors) == 1:
            current_point = bpoints[neighbors[0]]
            bound_order = np.append(bound_order,neighbors[0])
        elif len(neighbors) == 2:
            if (len(np.array(boundtree.query_ball_point(bpoints[neighbors[0]],1.1*(1./3.**(n-1))))) == 5) or (len(np.array(boundtree.query_ball_point(bpoints[neighbors[0]],1.1*(1./3.**(n-1))))) == 4):
                current_point = bpoints[neighbors[1]]
                bound_order = np.append(bound_order,neighbors[1])
            else:
                current_point = bpoints[neighbors[0]]
                bound_order = np.append(bound_order,neighbors[0])
    return bound_order
def bound_local(n):
    bpoints = np.load('vertices/boundary_it_' + str(n) + '.npy')
    indexbound = boundorder(n)
    upperhalf = np.array(np.load('vertices/all_vertices_it_' + str(n) + '.npy'))
    upperhalftree = spatial.cKDTree(upperhalf, compact_nodes=True, copy_data=False, balanced_tree=True)
    final_index = np.array([])
    for x in xrange(0,len(bpoints)):
        allpointsindex = np.array(upperhalftree.query_ball_point(bpoints[indexbound[x]],.000001))
        final_index = np.append(final_index,allpointsindex[0])
    return final_index

def boundvals(it,weight):
    index = bound_local(it)
    eigvecs = np.load('eigenvectors/all_vecs_it_' + str(it) + '_weight_' + str(weight) + '.npy')
    for i in xrange(0,len(eigvecs)):
        vector = np.array([[0,0]])
        for x in xrange(0,len(index)-1):
            vector = np.append(vector,np.array([[x,eigvecs[int(index[x]),i]]]),axis=0)
        vector = np.delete(vector,0,0)
        print str(weight) + "  " + str(i)
        np.save("boundary_vectors/boundary_it_" + str(it) + "_weight_" + str(weight) + "_vector_" + str(len(eigvecs)-i-1),vector)
	np.savetxt("boundary_vectors/boundary_it_" + str(it) + "_weight_" + str(weight) + "_vector_" + str(len(eigvecs)-i-1),np.real(np.around(vector,decimals=6)),delimiter=",")
    return vector
for it in xrange(2,5):
    boundvals(it,4**it)
