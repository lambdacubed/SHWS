import numpy as np
import os

DIRECTORY = "/Flat40/"

if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path
    print("\nLooking in directory ", directory_path + DIRECTORY)
    print("Which file would you like to read from? (for '1_numpy_array.npz', input '1')")
    data_file = input()
    wavefront_array_file = np.load(directory_path + DIRECTORY + data_file + '_numpy_array.npz')
    wavefront_array = wavefront_array_file['wavefront_array'] 
    print(wavefront_array[48,24])
    
