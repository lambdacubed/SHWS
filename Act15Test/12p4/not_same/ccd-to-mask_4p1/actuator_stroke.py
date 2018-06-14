import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

DIRECTORIES = ["/45/", "/50/", "/55/", "/60/"]
X_VALUES = [45, 50, 55, 60]
FILES = ["1", "2", "3"]
INDEX = [52,21]

if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path

    x = np.asarray(X_VALUES)
    y_values = []
    y_error = []
    for directory in DIRECTORIES:
        actuator_deformation_list = []
        for data_file in FILES:
            wavefront_array_file = np.load(directory_path + directory + data_file + '_numpy_array.npz')
            wavefront_array = wavefront_array_file['wavefront_array'] 
            actuator_value = wavefront_array[tuple(INDEX)]
            actuator_deformation_list.append(actuator_value)
            print(actuator_value)
        act_def = np.array(actuator_deformation_list)
        y_values.append(act_def.mean())
        y_error.append(np.std(act_def))

    y = np.array(y_values)
    y_err = np.array(y_error)

    fig = plt.figure(dpi = 300)

    plt.grid()
    plt.errorbar(x,-y,yerr=y_err, fmt='.')
    plt.xlim(39, 61)
    plt.ylim(-.1, 2.2)
    plt.xlabel('Actuator 15 voltage with others at 40V')
    plt.ylabel('Actuator stroke (microns)')
    plt.title('Actuator 15 stroke')
    plt.savefig('Actuator 15.png', bbox_inches='tight')
    plt.show()
    np.savez('4p1_vectors.npz', x=x, y=-y, y_err=y_err)