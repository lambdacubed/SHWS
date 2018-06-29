import os
import numpy as np
import file_functions as file_f


def voltage_to_zernike(filename):
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path

    influence_matrix = np.load(directory_path + '/interaction_matrix.npz')

    voltages = file_f.read_adf(filename)

    zernike_coefficients = np.matmul(influence_matrix, voltages)

    return zernike_coefficients
    
if __name__ == "__main__":
    voltage_to_zernike("10.adf")


