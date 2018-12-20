from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pylab

def maxsplt(iteration, weight, vector):
    fig = plt.figure()
    
    input = np.load("Boundary_vectors/boundary_it_"+str(iteration)+"_weight_"+str(weight)+"_vector_"+ str(vector) + ".npy")
    
    length = len(input)
    X = input[:,0]
    Y = input[:,1]

    plt.figure(1)
    plt.plot(X,Y,'k',X,Y,'.')
    plt.show()




iteration = 2

weight = 4**iteration

vector = 66

maxsplt(iteration,weight,vector)
