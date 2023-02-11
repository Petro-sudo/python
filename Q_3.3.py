#Question 3.3
import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()


randNum1 = numpy.zeros(1)
randNum2 = numpy.zeros(2)

if rank == 1:
        randNum1 = numpy.random.random_sample(1)
        print("Process", rank, "First number", randNum1)
        
if rank == 0:
        randNum2 = numpy.random.random_sample(1)
        print("Process", rank, "Second number", randNum2)
        max1 = randNum1
        max2 = randNum2
        if max1 > max2:
            print("The highest number is: ", max1)
        elif max2 > max1:
            print("The highest number is: ", max2)
    
       
          
    

        
         
     
     
     
     
  


