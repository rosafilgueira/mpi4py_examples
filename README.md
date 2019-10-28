# mpi4py_examples
This repository is dedicated to show different ways ( by creating 6 programs: split1.py, spit2.py, split3,py, split4.py , split,py and split6.py) to distribute a matrix of 1000x4801 elements, which has been generated randomly, among several processes by using different strategies. As soon as each process has each own chunk of the matrix, they compute the sum of their chunk

## split1.py

Divides the matrix row-wise. It uses SEND and RECV directives. Programmers have to compute the distribution of data among processes. A process can compute several rows. Each process receives the data in a matrix shape of 2Dimensions.

	mpiexec -n 10 python split1.py > output_1

In this example, each process gets 100 rows. Later, all the processes (in this example: 10 processes) computes in parallel the sum of their 100 rows. Each row has 4801 elements.

## split2.py

Divides the matrix column-wise. It uses SEND and RECV directives. Programmers have to compute the distribution of data among processes. A process can compute several columns. Each process receives the data in a matrix shape of 2Dimensions.
	 
	mpiexec -n 10 python split2.py > output_2

In this example, each process gets 480 columns (except the last process, which gets 481). Later, all the processes (in this example: 10 processes) computes in parallel the sum of their 480 colums. Each column has 1000 elements.

## split3.py   

Divides the matrix row-wise. Uses SCATTER. The distribution is made automatically by the SCATTER directive. No freedom for choosing the  distribution. One process has only one row. Each process receives the data (row) in a array of 1DIMENSION.
              
	mpiexec -n 10 python split3.py > output_3


## split4.py   

Divides the matrix column-wise. Uses SCATTER. The distribution is made AUTOMATICALLY by SCATTER directive. No freedom for choosing the  distribution. One process has only one column. Each process receives the data (column) in a array of 1DIMENSION
	
	mpiexec -n 3 python split4.py > output_4


## split5.py 

Divides the matrix row-wise. Uses SCATTERV. The programmers have to compute the distribution of data. One process can have several rows. One process can have more rows than others. The data can have gaps (if the programmer desires that). Each process receives the data (several rows) in a array of 1DIMENSION.

	mpiexec -n 10 python split5.py > output_5

## split6.py 

Divides the matrix row-wise. Uses SCATTERV. The programmers have to compute the distribution of data. One process can have several columns. One process can have more columns than others. The data can have gaps (if the programmer desires that). Each process receives the data (several columns) in a array (1DIMENSION).

	mpiexec -n 10 python split6.py > output_6
