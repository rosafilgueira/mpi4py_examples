# mpi4py_examples
This repository is dedicated to show different ways (split1.py, spit2.py, split3,py, split4.py , split,py and split6.py) to distribute a matrix (1000x4801 elements, which have been generated randomly) among several processes by using different strategies. As soon as each process has each chunk of the matrix, they compute the sum of their chunk

## split1.py

Divides the matrix row-wise. It uses SEND and RECV directives. The programmer has to compute the distribution among the processes. It gives all the freedom to programmers to choose the distribution of data among processes. A process can have several rows. Each process receives the data in a matrix shape (2Dimensions).

	mpiexec -n 10 python split1.py > output_1

In this example, each process gets 100 rows. And the 10 process computes in parallel the sum of their 100 rows. Each row has 4801 elements.

## split2.py

Divides the matrix column-wise. It uses SEND and RECV directives. The programmer has to compute the distribution among the processes. It gives all the freedom to programmers to choose the distribution of data among processes. A process can have several columns. Each process receives the data in a matrix shape (2Dimensions).
	 
	mpiexec -n 10 python split2.py > output_2

In this example, each process gets 480 columns (except the last process, which gets 481). And the 10 process computes in parallel the sum of their 480 colums. Each column has 1000 elements.

## split3.py   

Divides the matrix row-wise. Uses SCATTER. The distribution is made automatically by the SCATTER directive. No freedom for choosing the better distribution. One process has only one row. Each process receives the data (the row) in a array (1DIMENSION).
              
	mpiexec -n 10 python split3.py > output_3


## split4.py   

Divides the matrix column-wise. Uses SCATTER. The distribution is made AUTOMATICALLY by SCATTER directive.No freedom for choosing the better distribution. One process has only one colum. Each process receives the data (the column) in a array (1DIMENSION)
	
	mpiexec -n 3 python split4.py > output_4


## split5.py 

Divides the matrix row-wise. Uses SCATTERV. The programmer has to compute the distribution among the processes. Gives, all the freedom to the programmer to choose the better distribution. One process can have several rows. One process can have more rows than others. The data can have gaps (if the programmer desires that). Each process receives the data (several rows) in a array (1DIMENSION).

	mpiexec -n 10 python split5.py > output_5

## split6.py 

Divides the matrix row-wise. Uses SCATTERV. The programmer has to compute the distribution among the processes. Gives, all the freedom to the programmer to choose the better distribution. One process can have several columns. One process can have more columns than others. The data can have gaps (if the programmer desires that). Each process receives the data (several columns) in a array (1DIMENSION).

	mpiexec -n 10 python split6.py > output_6
