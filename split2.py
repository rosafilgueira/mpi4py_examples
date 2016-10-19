from mpi4py import MPI
import numpy
from numpy import random

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

if(rank==0):
    v=random.random((1000,4801))
    print "The size of v is:", len(v)	
    if size>=len(v[0]):
        size=len(v[0])
    slice_size=int(numpy.ceil(float(len(v[0]))/float(size)))
    slice_for_last_node=len(v[0])-(size-1)*slice_size      
    #xtra_slices=len(v[0])%size

    cols=len(v[0])
    print "slice_size:",slice_size
    print "slice_for_last_node:",slice_for_last_node
else:
    slice_size=slice_for_last_node=cols=None

size=comm.bcast(size,root=0)
slice_size=comm.bcast(slice_size,root=0)
slice_for_last_node=comm.bcast(slice_for_last_node,root=0)
cols=comm.bcast(cols,root=0)

def doSum(x):
        return numpy.sum(x)

if rank==0:

        print 'thats v_random:\n', v

    	count=1
    	cur_dest=0

        for i in range(len(v[0])): 
        	if(count>slice_size and cur_dest<size-1):
            		cur_dest+=1
            		count=1
        	if(cur_dest>=size-1):
            		cur_dest=size-1

            	comm.send(v[:,i],dest=cur_dest)
        	count+=1

if rank<size-1:
    count=1
    while count<=slice_size: #slices per proc
        data=comm.recv(source=0)
        count+=1
        print 'my rank is {0} and my output is {1}\n'.format(rank,doSum(data))


elif rank==size-1:
    count=1
    while count<=slice_for_last_node:
    	data=comm.recv(source=0)
        count+=1
        print 'my rank is {0} and my output is {1}\n'.format(rank,doSum(data))
