def main():
    from time import time
    import argparse
    import subprocess
    import os
    

    # Read command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-nt', type=int, default=100, help='Number of iterations')
    parser.add_argument('-nx', type=int, default=1024, help='Number of gridpoints in x-direction')
    parser.add_argument('-ny', type=int, default=4096, help='Number of gridpoints in y-direction')
    parser.add_argument('-nc', type=int, default=1, help='Number of processors')

    args = parser.parse_args()
    N = args.nc
    X = args.nx
    Y = args.ny
    T = args.nt
    
    b = "rm scale.out"
    c = 'make'
    a = "mpiexec -np " + str(N) + " ./scale.out -nx " + str(X) + " -ny " + str(Y) + " -nt " + str(T) + " >>strong_input.dat"
    os.system(b)
    os.system(c)
    os.system(a)
    #temp = subprocess.Popen([a], stdout = subprocess.PIPE)
    #output = str(temp.communicate())

#############################
if (__name__ == "__main__"):
    main()