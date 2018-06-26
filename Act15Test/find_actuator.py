import numpy as np
import os

DIRECTORY = "/Act15Test/12p4/not_same/ccd-to-mask_4p06cal/50/"

THRESHOLD = -.8

if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path
    print("\nLooking in directory ", directory_path + DIRECTORY)
    print("Which file would you like to read from? (for '1_numpy_array.npz', input '1')")
    data_file = input()
    wavefront_array_file = np.load(directory_path + DIRECTORY + data_file + '_numpy_array.npz')
    wavefront_array = wavefront_array_file['wavefront_array'] 
    indices = np.argwhere(wavefront_array < THRESHOLD)
    print(indices)
    for index in indices:
        print(wavefront_array[tuple(index)])
    
