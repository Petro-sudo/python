#Question 3.1.2
from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
n_ranks = MPI.COMM_WORLD.Get_size()
size = comm.size
rank = comm.rank
name = MPI.Get_processor_name()

n_ranks = MPI.COMM_WORLD.Get_size()
if n_ranks <= 1:
    print("This example requires two or more ranks")
    sys.exit(1)


rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    message = 'I am process %d of %d on %s.\n' % (rank, size, name)
    MPI.COMM_WORLD.send(message, dest=1, tag=0)

if rank == 1:
    message = MPI.COMM_WORLD.recv(source=0, tag=0)
    print(message)


