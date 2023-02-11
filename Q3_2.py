#Question 3.2
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

print("Hello from process", str(rank), "out of", str(size))
