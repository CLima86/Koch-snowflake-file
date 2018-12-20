import math
import numpy as np
def sqrt(x):
	return math.sqrt(x)

# np.set_printoptions makes it so it outputs entire arrays intsead of short hand, so it can mathematica or other visualization softwear

np.set_printoptions(threshold=np.nan)

allboundarypoints = np.array([[0, sqrt(3)], [-0.5, sqrt(3)/2], [0, sqrt(3)], [0.5, sqrt(3)/2], [1.5, sqrt(3)/2], [1.0, 0], [1.5, sqrt(3)/2], [0.5, sqrt(3)/2], [1.5, -sqrt(3)/2], [1.0, 0], [1.5, -sqrt(3)/2], [0.5, -sqrt(3)/2], [0, -sqrt(3)], [-0.5, -sqrt(3)/2], [0, -sqrt(3)], [0.5, -sqrt(3)/2], [-1.5, -sqrt(3)/2], [-1.0, 0], [-1.5, -sqrt(3)/2], [-0.5, -sqrt(3)/2], [-1.5, sqrt(3)/2], [-1.0, 0], [-1.5, sqrt(3)/2], [-0.5, sqrt(3)/2]])

#nthboundaryforedges takes as an input a set of points (in this code those points will be boundaryedges1 or boundaryedges2). It scales the coordinates by a third towards the origin and translates them as necessary to generate the next boundary from a given boundary. NOTE: This function doesn't generate the exact boundary, it will have interior points included that are removed in a later function.

def nthboundaryforedges(inputpoints1):
	boundarypoints = inputpoints1.copy()
	boundarypoints *= 1./3.
	scaledboundary = np.vstack(boundarypoints)
	shift1 = np.append(np.vstack(boundarypoints[:,0]+1.),np.vstack(boundarypoints[:,1]+sqrt(3)/3.),axis=1)
	shift2 = np.append(np.vstack(boundarypoints[:,0]),np.vstack(boundarypoints[:,1]+2.*sqrt(3)/3.),axis=1)
	boundarypoints = np.append(boundarypoints,shift1,axis=0)
	boundarypoints = np.append(boundarypoints,shift2,axis=0)
	flipx = np.append(np.vstack(-1.*boundarypoints[:,0]),np.vstack(boundarypoints[:,1]),axis=1)
	boundarypoints = np.append(boundarypoints,flipx,axis=0)
	flipy = np.append(np.vstack(boundarypoints[:,0]),np.vstack(-1.*boundarypoints[:,1]),axis=1)
	boundarypoints = np.append(boundarypoints,flipy,axis=0)
	return boundarypoints

#nthinteriorforedges scales down the inputed points and translates them. In this case they are translated to all of the neccesary locations to get all of the points on the snowlfake, interior and boundary
#make comment about vstack


def nthboundaryedges(n):

	for x in xrange(0,n):

		if x == 0:
			set1 = np.array([[0, sqrt(3)], [-0.5, sqrt(3)/2], [0, sqrt(3)], [0.5, sqrt(3)/2], [1.5, sqrt(3)/2], [1.0, 0], [1.5, sqrt(3)/2], [0.5, sqrt(3)/2], [1.5, -sqrt(3)/2], [1.0, 0], [1.5, -sqrt(3)/2], [0.5, -sqrt(3)/2], [0, -sqrt(3)], [-0.5, -sqrt(3)/2], [0, -sqrt(3)], [0.5, -sqrt(3)/2], [-1.5, -sqrt(3)/2], [-1.0, 0], [-1.5, -sqrt(3)/2], [-0.5, -sqrt(3)/2], [-1.5, sqrt(3)/2], [-1.0, 0], [-1.5, sqrt(3)/2], [-0.5, sqrt(3)/2]])
		set1 = nthboundaryforedges(set1).copy()
		removeindex = np.array([0])

		for x in xrange(0,len(set1)):
			dist1 = sqrt((set1[x,0])**2+(set1[x,1])**2)
			if dist1 <= .9999:
				removeindex = np.append(removeindex,x)
			pass
		set1 = np.delete(set1,removeindex,0)
		pass

	set1 = np.unique(np.around(set1,decimals=7),axis=0)
	return set1
for x in xrange(1,5):
	print x
	filename = 'vertices/boundary_it_' +str(x+1)
	np.save(filename,nthboundaryedges(x))
