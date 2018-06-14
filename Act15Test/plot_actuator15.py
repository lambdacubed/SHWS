import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os


if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path


    data_3p5 = np.load(directory_path + '/10p8/3p5_vectors.npz')
    x_3p5 = data_3p5['x']
    y_3p5 = data_3p5['y']
    y_err_3p5 = data_3p5['y_err']

    data_4p1 = np.load(directory_path + '/12p4/not_same/ccd-to-mask_4p1/4p1_vectors.npz')
    x_4p1 = data_4p1['x']
    y_4p1 = data_4p1['y']
    y_err_4p1 = data_4p1['y_err']

    x = np.linspace(40, 65, 100)
    y = 0.066929*(x-40)

    fig = plt.figure(1, dpi = 1200)

    ax = fig.add_subplot(111)

    ax.grid()
    ax.errorbar(x_3p5, y_3p5, yerr=y_err_3p5, fmt='.', label="Lens-to-CMOS = 3.5mm")
    ax.errorbar(x_4p1, y_4p1, yerr=y_err_4p1, fmt='.', label="Lens-to-CMOS = 4.1mm")
    ax.plot(x,y, label="Northrop Grumman")
    ax.plot(x,2*y, label="2x Northrop Grumman")

    ax.legend()

    ax.set_title('Actuator 15 stroke')
    ax.set_ylabel('Actuator movement (microns)')
    ax.set_xlabel('Actuator 15 voltage (everything else at 40V)')

    plt.savefig('Actuator 15 final.png', bbox_inches='tight')

    plt.show()
