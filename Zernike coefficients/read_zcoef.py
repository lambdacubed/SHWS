
import os
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

DIRECTORY = ""

ACTUATORS = ['/0/', '/1/']

VOLTAGES = ['4/', '8/']

FILES = ["test", "test_w_reference"]

def read_z_coef(filename):
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path
    wavefront_array = np.loadtxt(directory_path + "/" + filename + '.txt')
    if wavefront_array.shape[0] == 200:
        return wavefront_array[:,0]
    else:
        print("There aren't 200 coefficients")


if __name__ == "__main__":
    # zc_list = [read_z_coef("test_w_reference")]
    # zc_list.append(read_z_coef("test"))
    # zc_array = np.array(zc_list)
    # print(zc_array.mean(axis=0))
    # print(zc_array.std(axis=0,ddof=1))



    x_voltages = np.array([4, 8])
    
    directory_path = os.path.dirname(os.path.abspath(__file__)) # get the current directory's path

    interaction_matrix_list = []
    r_squared_list = []
    std_error_list = []
    for actuator in ACTUATORS:
        zc_per_voltage = []
        std_per_voltage = []
        for voltage in VOLTAGES:
            zc_list = []
            for zc_file in FILES:
                zernike_polynomial_info = np.loadtxt(directory_path + actuator + voltage + zc_file + '.txt')
                if zernike_polynomial_info.shape[0] == 200:
                    zc_list.append(zernike_polynomial_info[:,0])
                else:
                    print("There aren't 200 coefficients in " + actuator + voltage + zc_file)

            zc_array = int(voltage[0])**(int(actuator[1])) * np.array(zc_list)
            zc_array_mean = zc_array.mean(axis=0)
            zc_array_stddev = zc_array.std(axis=0, ddof=1)

            zc_per_voltage.append(zc_array_mean)
            std_per_voltage.append(zc_array_stddev)


        zc_voltage_array = np.array(zc_per_voltage)
        std_voltage_array = np.array(std_per_voltage)

        interaction_matrix_elements = []
        r_s = []
        std_error = []
        for z_coef in range(zc_voltage_array.shape[1]):
            slope, intercept, r_value, p_value, std_err = stats.linregress(x_voltages, zc_voltage_array[:, z_coef])
            interaction_matrix_elements.append(slope)
            r_s.append(r_value)
            std_error.append(std_err)

        interaction_matrix_list.append(interaction_matrix_elements)
        r_squared_list.append(r_s)
        std_error_list.append(std_error)

    interaction_matrix = np.transpose(np.array(interaction_matrix_list))
    r_squared = np.transpose(np.array(r_squared_list))
    std_err = np.transpose(np.array(std_error_list))

    np.savez(directory_path + '/interaction_matrix.npz', interaction_matrix=interaction_matrix)
    np.savez(directory_path + '/error_info.npz', r_squared = r_squared, std_err=std_err)

    fig = plt.figure(dpi=400)

    ax1 = fig.add_subplot(131)
    plot_1 = ax1.imshow(interaction_matrix)
    plt.colorbar(plot_1,ax=ax1)
    ax1.set_title('Interaction matrix')

    ax2 = fig.add_subplot(132)
    plot_2 = ax2.imshow(r_squared)
    plt.colorbar(plot_2,ax=ax2)
    ax2.set_title('R squared')

    ax3 = fig.add_subplot(133)
    plot_3 = ax3.imshow(std_err)
    plt.colorbar(plot_3,ax=ax3)
    ax3.set_title('Standard Error')

    plt.savefig('Interaction Matrix Info.png', bbox_inches='tight')


