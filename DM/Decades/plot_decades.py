import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

DIRECTORIES = ["/flat/", "/0/", "/10/", "/20/", "/30/","/40/", "/50/", "/60/" "/70/", "/80/", "/90/",]
FILES = ["1", "2", "3"]

if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path


    for directory in DIRECTORIES:
        wave_array_list = []

        zc_array_list = []

        for data_file in FILES:
            wavefront_array_file = np.load(directory_path + directory + data_file + '_numpy_array.npz')
            wavefront_array = wavefront_array_file['wavefront_array'] 
            wave_array_list.append(wavefront_array)

            zc_file = np.load(directory_path + directory + data_file + '_numpy_array.npz')
            zc_array = zc_file['z_coef'] 
            zc_array_list.append(zc_array)


        wave_array_list = np.array(wave_array_list)
        wavefront_values = wave_array_list.mean()

        x = np.linspace(-2,2,wavefront_array.shape[0])
        y = np.linspace(-2,2,wavefront_array.shape[0])
        X, Y = np.meshgrid(x,y)

        y = np.array(wavefront_values)

        fig = plt.figure(dpi=100)
        ax = fig.add_subplot(111, projection='3d')

        ax.plot_surface(X, Y, wavefront_values, cmap='inferno')
        ax.savefig('Decade wavefront ' + directory + '.png', bbox_inches='tight')
        fig = plt.figure(dpi = 300)



        zc_array_list = np.array(zc_array_list)
        zc_values = zc_array_list.mean()
        zc_error = zc_array_list.std()

        x = np.array(np.range(zc_values.size)) + 1
        ax = fig.add_subplot(111)

        ax.grid()
        ax.errorbar(x, zc_values, yerr=zc_error, fmt='.')
        
        ax.set_title('Voltage at ' + directory)
        ax.set_ylabel('Zernike coefficent')
        ax.set_xlabel('Zernike polynomial')

        plt.savefig('Z coef at ' + directory + '.png', bbox_inches='tight')
