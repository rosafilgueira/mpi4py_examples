#Divides the matrix row-wise. It uses SEND and RECV directives. 
#Programmers have to compute the distribution of data among processes. 
#A process can compute several rows. 
#Each process receives the data in a matrix shape of 2Dimensions.

#mpiexec -n 10 python split1.py > output_1

#In this example, each process gets 100 rows. 
#Later, all the processes (in this example: 10 processes) computes in parallel the sum of their 100 rows. 
#Each row has 4801 elements.

from mpi4py import MPI
import numpy
from numpy import random

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

if(rank==0):
    v=random.random((1000,4801))
    if size>=len(v):
        size=len(v)
    slice_size=int(numpy.ceil(float(len(v))/float(size)))
    slice_for_last_node=len(v)-(size-1)*slice_size      
    #xtra_slices=len(v)%size

    rows=len(v)
    print "slice_size:",slice_size
    print "slice_for_last_node:",slice_for_last_node
else:
    slice_size=slice_for_last_node=rows=None

size=comm.bcast(size,root=0)
slice_size=comm.bcast(slice_size,root=0)
slice_for_last_node=comm.bcast(slice_for_last_node,root=0)
rows=comm.bcast(rows,root=0)

def doSum(x):
        return numpy.sum(x)

if rank==0:

        print 'thats v_random:\n', v

    	count=1
    	cur_dest=0

        for i in range(len(v)): 
        	if(count>slice_size and cur_dest<size-1):
            		cur_dest+=1
            		count=1
        	if(cur_dest>=size-1):
            		cur_dest=size-1

            	comm.send(v[i],dest=cur_dest)
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
