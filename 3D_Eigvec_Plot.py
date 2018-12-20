from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
def plotiteig(n,m,w):
    itnumber = n

    eignumber = m

    orderedpoints = np.load('eigenvectors/full_it_' + str(n) + '_weight_' + str(w) + '_vector_' + str(m)  +'.npy')
    eigs = np.load('eigenvalues/full_eigvals_it_' + str(n) + '_weight_' + str(w) +'.npy')
    X = orderedpoints[:,0]
    Y = orderedpoints[:,1]
    Z = orderedpoints[:,2]
    ax.scatter(X,Y,Z, c='r',marker='.')
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')
    plt.title("Iteration: " + str(n) + " Eigenvector: " + str(m) + " Weight: "+ str(w) + " Eigenvalue: " + str(np.real(eigs[len(eigs)-m-1])))
    print str(np.real(eigs[len(eigs)-m-1]))
    plt.show()
    return

it = 2
weight = (4**it)

vec = 66

plotiteig(it,vec,weight)