import math
import numpy as np
from datetime import datetime
def sqrt(x):
	return math.sqrt(x)

np.set_printoptions(threshold=np.nan)


allpoints = np.array([[0.,0.],[0, sqrt(3)], [-0.5, sqrt(3)/2], [0, sqrt(3)], [0.5, sqrt(3)/2], [1.5, sqrt(3)/2], [1.0, 0], [1.5, sqrt(3)/2], [0.5, sqrt(3)/2], [1.5, -sqrt(3)/2], [1.0, 0], [1.5, -sqrt(3)/2], [0.5, -sqrt(3)/2], [0, -sqrt(3)], [-0.5, -sqrt(3)/2], [0, -sqrt(3)], [0.5, -sqrt(3)/2], [-1.5, -sqrt(3)/2], [-1.0, 0], [-1.5, -sqrt(3)/2], [-0.5, -sqrt(3)/2], [-1.5, sqrt(3)/2], [-1.0, 0], [-1.5, sqrt(3)/2], [-0.5, sqrt(3)/2]])


def nthuniquevertices(n):
	for x in xrange(0,n):
		if x==0:
			alledges = allpoints.copy()
		alledges = np.unique(alledges,axis=0)
		alledges *= 1./3.
		shift1 = np.append(np.vstack(alledges[:,0]+1.),np.vstack(alledges[:,1]+sqrt(3)/3.),axis=1)
		shift2 = np.append(np.vstack(alledges[:,0]),np.vstack(alledges[:,1]+2.*sqrt(3)/3.),axis=1)
		shift3 = np.append(np.vstack(alledges[:,0]),np.vstack(alledges[:,1]+sqrt(3)/3.),axis=1)
		shift4 = np.append(np.vstack(alledges[:,0]+2./3.),np.vstack(alledges[:,1]),axis=1)
		shift5 =np.append(np.vstack(alledges[:,0]+1./3.),np.vstack(alledges[:,1]+sqrt(3)/3.),axis=1)
		alledges = np.append(alledges,shift1,axis=0)
		alledges = np.append(alledges,shift2,axis=0)
		alledges = np.append(alledges,shift3,axis=0)
		alledges = np.append(alledges,shift4,axis=0)
		alledges = np.append(alledges,shift5,axis=0)
		flipx = np.append(np.vstack(-1.*alledges[:,0]),np.vstack(alledges[:,1]),axis=1)
		alledges = np.append(alledges,flipx,axis=0)
		flipy = np.append(np.vstack(alledges[:,0]),np.vstack(-1.*alledges[:,1]),axis=1)
		alledges = np.append(alledges,flipy,axis=0)
		alledges = np.unique(np.around(alledges,decimals=7),axis=0)
		pass
	pass
	return alledges


for x in xrange(4,5):
	start_time = datetime.now()
	a = nthuniquevertices(x)
	end_time = datetime.now()
	filename = 'vertices/all_vertices_it_' + str(x+1)
	np.save(filename,a)
	np.savetxt(filename,a,delimiter=",")
	print('Duration: {}'.format(end_time-start_time))
