import math
import numpy as np
import scipy
from scipy import spatial
from datetime import datetime

def vertices(n):
    allpoints = np.load('vertices/all_vertices_it_' + str(n) + '.npy')
    boundarypoints = np.load('vertices/boundary_it_' + str(n) + '.npy')
    return allpoints, boundarypoints
def locations(n,buffer):
    allpoints, boundarypoints = vertices(n)
    fulltree = spatial.cKDTree(allpoints, compact_nodes=True, copy_data=False, balanced_tree=True)
    boundlocations = np.array([])
    for x in xrange(0,len(boundarypoints)):
        boundlocations = np.append(boundlocations,fulltree.query_ball_point(boundarypoints[x],(buffer*(1./3.**(n-1)))+.00001))
    print len(boundlocations)
    boundlocations = np.unique(boundlocations.astype(int))
    return allpoints, boundlocations
def maxvals(n,buffer,weight):
    allpoints, boundlocations = locations(n,buffer)
    intmaxs = np.empty([len(allpoints),2])
    boundmaxs = np.empty([len(allpoints),2])
    maxprop = np.empty([len(allpoints),2])
    intsum = np.empty([len(allpoints),2])
    boundsum = np.empty([len(allpoints),2])
    sumprop = np.empty([len(allpoints),2])
    l2intsum = np.empty([len(allpoints),2])
    l2boundsum = np.empty([len(allpoints),2])
    for x in xrange(0,len(allpoints)):
        eigvec = np.absolute(np.load('eigenvectors/full_it_' + str(n) + '_weight_' + str(weight*(4**n))+ '_vector_' + str(x) + '.npy')[:,2])
        totsum = np.sum(eigvec)
        eigvecbound = eigvec[boundlocations]
        eigvecint = np.delete(eigvec,boundlocations)
        boundmaxs[x][0] = x
        intmaxs[x][0] = x
        maxprop[x][0] = x
        boundmaxs[x][1] = np.amax(eigvecbound)
        intmaxs[x][1] = np.amax(eigvecint)
        maxprop[x][1] = boundmaxs[x][1]/intmaxs[x][1]

        boundsum[x][0] = x
        intsum[x][0] = x
        sumprop[x][0] = x
        boundsum[x][1] = np.sum(eigvecbound)
        intsum[x][1] = np.sum(eigvecint)
        sumprop[x][1] = boundsum[x][1]/intsum[x][1]

	l2boundsum[x][0] = x
        l2intsum[x][0] = x
        l2boundsum[x][1] = np.sum(eigvecbound**2)
        l2intsum[x][1] = np.sum(eigvecint**2)
    weight = weight*(4**n)
    np.save("norms/infinity_boundary_it_" + str(n) + "_weight_" + str(weight)+ "_buffer_"+str(buffer),boundmaxs)
    boundmaxs.astype('float32').tofile("norms/infinity_boundary_it_" + str(n) + "_weight_" + str(weight)+ "_buffer_"+str(buffer) +  ".dat")
    np.save("norms/infinity_interior_it_" + str(n) + "_weight_" + str(weight)+ "_buffer_"+str(buffer),intmaxs)
    intmaxs.astype('float32').tofile("norms/infinity_interior_it_" + str(n) + "_weight_" + str(weight)+ "_buffer_"+str(buffer) +  ".dat")
    np.save("norms/infinity_ratio_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer),maxprop)
    maxprop.astype('float32').tofile("norms/infinity_ratio_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer) +  ".dat")
    np.save("norms/L1_boundary_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer),boundsum)
    boundsum.astype('float32').tofile("norms/L1_boundary_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer) +  ".dat")
    np.save("norms/L1_interior_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer),intsum)
    intsum.astype('float32').tofile("norms/L1_interior_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer) +  ".dat")
    np.save("norms/L1_ratio_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer),sumprop)
    sumprop.astype('float32').tofile("norms/L1_ratio_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer) +  ".dat")
    np.save("norms/L2_boundary_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer),l2boundsum)
    l2boundsum.astype('float32').tofile("norms/L2_boundary_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer) +  ".dat")
    np.save("norms/L2_boundary_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer),l2intsum)
    l2intsum.astype('float32').tofile("norms/L2_interior_it_" + str(n) + "_weight_" + str(weight)+"_buffer_"+str(buffer) +  ".dat")
    return

for i in xrange(4,5):
    print i
    for x in xrange(0,1):
	print x, x
        for y in xrange(1,2):
	    print y,y,y
            maxvals(i,x,y)
