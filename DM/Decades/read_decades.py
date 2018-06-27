import numpy as np
import csv
import os

DIRECTORIES = ["/flat/", "/0/", "/10/", "/20/", "/30/","/40/", "/50/", "/60/" "/70/", "/80/", "/90/"]
FILES = ["1", "2", "3"]

if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path

    for directory in DIRECTORIES:
        for data_file in FILES:
            wavefront_array = np.loadtxt(directory_path + directory + data_file + '.txt')
            z_coefficients = np.loadtxt(directory_path + directory + data_file + 'zc.txt')
            np.savez(directory_path + directory + data_file + '_numpy_array.npz', wavefront_array=wavefront_array)
            np.savez(directory_path + directory + data_file + 'zc_numpy_array.npz', z_coef=z_coefficients[:,0])

