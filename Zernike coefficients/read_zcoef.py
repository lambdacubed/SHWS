
import os
import numpy as np


DIRECTORY = ""

def read_z_coef(filename):
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path
    wavefront_array = np.loadtxt(directory_path + "/" + filename + '.txt')
    if wavefront_array.shape[0] == 200:
        print(wavefront_array[:,0])
    else:
        print("There aren't 200 coefficients")


if __name__ == "__main__":
    read_z_coef("test_w_reference")
