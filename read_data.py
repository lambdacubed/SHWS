import numpy as np
import csv
import os

DIRECTORY = "/Act15Test/12p4/not_same/ccd-to-mask_4p1/60/"

#def read_wavefront_grid(data_file):
#    wavefront_array = np.empty(0,'float')
#    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path
#    with open(directory_path + DIRECTORY + data_file, 'r') as filein:    # open the file to be read from
#        tsvreader = csv.reader(filein, delimiter = " ")    # make the values space separated
#        line_number = 1	# keep track of the line 
#        for row in tsvreader:		# go through each row in the file
#            if line_number == 1:
#                wavefront_array = row
#            else:
#                wavefront_array = np.vstack((wavefront_array,row))
#            line_number += 1	# increment the line_number
#    return wavefront_array

if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path
    print("\nLooking in directory ", directory_path + DIRECTORY)
    print("Which file would you like to read from? (for '1.txt', input '1')")
    data_file = input()
    wavefront_array = np.loadtxt(directory_path + DIRECTORY + data_file+'.txt')
    np.savez(directory_path + DIRECTORY + data_file + '_numpy_array.npz', wavefront_array=wavefront_array)
