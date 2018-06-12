import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

DIRECTORY = "/Act15Test/50/"

def plot_data(wavefront_array):
    x = np.linspace(-2,2,wavefront_array.shape[0])
    y = np.linspace(-2,2,wavefront_array.shape[0])
    X, Y = np.meshgrid(x,y)
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, -wavefront_array, cmap='inferno')
    plt.show()

if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path
    print("\nLooking in directory ", directory_path + DIRECTORY)
    print("Which file would you like to read from? (for '1_numpy_array.npz', input '1')")
    data_file = input()
    wavefront_array_file = np.load(directory_path + DIRECTORY + data_file + '_numpy_array.npz')
    wavefront_array = wavefront_array_file['wavefront_array'] 
    plot_data(wavefront_array_file['wavefront_array'])

