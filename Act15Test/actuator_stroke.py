import numpy as np
import matplotlib
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data40 = np.array([-.063296, -.071984, -.072457, -.093994, -.080089])
    data45 = np.array([-.471318, -.550925, -.533524, -.488437, -.508567])
    data50 = np.array([-.99765, -1.028987, -1.060487, -1.125882, -1.104944])
    data55 = np.array([-1.578908, -1.59371, -1.548129, -1.64831, -1.573344])
    data60 = np.array([-2.212899, -2.096609, -2.158838, -2.142277, -2.183286])
    error_40 = np.array([data40.max(), data40.min()])
    error_45 = np.array([data45.max(), data45.min()])
    error_50 = np.array([data50.max(), data50.min()])
    error_55 = np.array([data55.max(), data55.min()])
    error_60 = np.array([data60.max(), data60.min()])
    error_bars_t = -np.array([error_40, error_45, error_50, error_55, error_60])
    error_bars_coordinates = np.transpose(error_bars_t)
    x = np.asarray([40, 45, 50, 55, 60])
    y = -np.array([data40.mean(), data45.mean(), data50.mean(), data55.mean(), data60.mean()])
    error_bars = [y - error_bars_coordinates[0], error_bars_coordinates[1] - y]
    fig = plt.figure(dpi = 300)

    plt.grid()
    plt.errorbar(x,y,yerr=error_bars)
    plt.xlabel('Actuator 15 voltage with others at 40V')
    plt.ylabel('Actuator stroke (microns)')
    plt.title('Actuator 15 stroke')
    plt.savefig('Actuator 15.png', bbox_inches='tight')
    plt.show()