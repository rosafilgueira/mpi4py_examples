from mpi4py import MPI
import numpy
from numpy import random

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
sendbuf=[]
if(rank==0):
    v=random.random((10,3))
    sendbuf=v.transpose()	
    print 'thats v_random transposed!:\n', sendbuf

def doSum(x):
        return numpy.sum(x)

data=comm.scatter(sendbuf,0)
print 'my rank is {0} and my output is {1}\n'.format(rank,doSum(data))

for i in range(len(data)):
		data[i]=data[i]+1

gather_matrix=comm.gather(data,0)
if (rank == 0):
	print 'thats gather_matrix\n:', numpy.array(gather_matrix)
