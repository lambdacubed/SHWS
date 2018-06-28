import numpy as np
import csv
import os
import matplotlib.pyplot as plt

DIRECTORIES = ["/"]
FILES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path

    for directory in DIRECTORIES:
        z_coef_list = []
        for data_file in FILES:
            zernike_coefficients_info = np.loadtxt(directory_path + directory + data_file + '.txt')
            z_coefficients = zernike_coefficients_info[:,0]
            z_coef_list.append(z_coefficients)

        zc_array_list = np.array(z_coef_list)
        zc_noise = zc_array_list.std(axis=0,ddof=1)

        fig = plt.figure(dpi=100)
        ax = fig.add_subplot(111)

        ax.grid()
        ax.plt(zc_noise)

        ax.set_title('Zernike polynomial noise')
        ax.set_ylabel('Standard deviation (waves?)')
        ax.set_xlabel('Zernike polynomial number')

        plt.savefig('Z polynomial noise.png', bbox_inches='tight')



