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
    if size>=len(v[0]):
        size=len(v[0])
    slice_size=int(numpy.ceil(float(len(v[0]))/float(size)))
    slice_for_last_node=len(v[0])-(size-1)*slice_size      
    rows=len(v)
    cols=len(v[0])
    tup_elem =[]
    tup_disp =[]
    disp=0
    for i in range(size-1):
	tup_elem.append(slice_size*rows)
	tup_disp.append(disp)
	disp = disp + slice_size*rows

    tup_elem.append(slice_for_last_node*rows)
    tup_disp.append(disp)
    print "tup_elem:",tup_elem
    print "tup_disp:",tup_disp
    		
else:
    slice_size=slice_for_last_node=rows=cols=tup_elem=tup_disp=None

def doSum(x):
        return numpy.sum(x)


#############################
size=comm.bcast(size,root=0)
slice_size=comm.bcast(slice_size,root=0)
slice_for_last_node=comm.bcast(slice_for_last_node,root=0)
rows=comm.bcast(rows,root=0)
tup_elem=comm.bcast(tup_elem,root=0)
tup_disp=comm.bcast(tup_disp,root=0)

if rank<size-1:
	data=numpy.zeros(slice_size*rows)
else:
	data=numpy.zeros(slice_for_last_node*rows)
    
tup_elem= tuple(tup_elem)
tup_disp = tuple(tup_disp)

	
#############################
comm.Scatterv([sendbuf,tup_elem,tup_disp,MPI.DOUBLE],data)

comm.Barrier()

print 'my rank is {0} and my output is {1}\n'.format(rank,doSum(data))

