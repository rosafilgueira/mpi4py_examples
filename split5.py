#Divides the matrix row-wise. 
#Uses SCATTERV. 
#The programmers have to compute the distribution of data. 
#One process can have several rows. 
#One process can have more rows than others. 
#The data can have gaps (if the programmer desires that). Each process receives the data (several rows) in a array of 1DIMENSION.

#mpiexec -n 10 python split5.py > output_5

from mpi4py import MPI
import numpy
from numpy import random

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
sendbuf=[]
data=[]
if(rank==0):
    v=random.random((1000,4801))
    sendbuf=v	
    print 'thats v_random:\n', v
    if size>=len(v):
	size=len(v)
    slice_size=int(numpy.ceil(float(len(v))/float(size)))
    slice_for_last_node=len(v)-(size-1)*slice_size   
    rows=len(v)
    cols=len(v[0])
    tup_elem =[]
    tup_disp =[]
    disp=0
    for i in range(size-1):
	tup_elem.append(slice_size*cols)
	tup_disp.append(disp)
	disp = disp + slice_size*cols 

    tup_elem.append(slice_for_last_node*cols)
    tup_disp.append(disp)

else:
    slice_size=slice_for_last_node=rows=cols=tup_elem=tup_disp=None

def doSum(x):
        return numpy.sum(x)


#############################
size=comm.bcast(size,root=0)
slice_size=comm.bcast(slice_size,root=0)
slice_for_last_node=comm.bcast(slice_for_last_node,root=0)
cols=comm.bcast(cols,root=0)
tup_elem=comm.bcast(tup_elem,root=0)
tup_disp=comm.bcast(tup_disp,root=0)

if rank<size-1:
	data=numpy.zeros(slice_size*cols)
else:
	data=numpy.zeros(slice_for_last_node*cols)
    
tup_elem= tuple(tup_elem)
tup_disp = tuple(tup_disp)

	
#############################
comm.Scatterv([sendbuf,tup_elem,tup_disp,MPI.DOUBLE],data)

comm.Barrier()

print 'my rank is {0} and my output is {1}\n'.format(rank,doSum(data))

