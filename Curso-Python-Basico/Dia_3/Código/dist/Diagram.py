from matplotlib import pyplot as plt
import numpy as np

# import PyQt4.QtGui

def viga(q, L):
    # m(x) = - q*L*L/2 + q*L*x/2 - q*x*x/2
    x = np.linspace(0, L, 100)
    m = -(-q*L*L/12 + q*L*x/2 - q*x*x/2)

    plt.plot(x, m, '-b')
    plt.xlabel('x (m)')
    plt.ylabel('M (kN.m)')
    plt.title('Moment Diagram')
    plt.fill_between(x, 0, m, color='blue', alpha=0.2)
    plt.show()

# viga(10, 3)
