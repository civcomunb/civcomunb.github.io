from matplotlib import pyplot as plt
import numpy as np

# Esse programa irá plotar os digramas de momento fletor e deformação de uma viga biengastada
# com carga concentrada no centro ou distribuída.
# Utilizaremos as equações tabeladas para isso.


def plot_m_diagram(load_type, L, q):
    s = 200
    moment = np.zeros(s+1)
    x = np.linspace(0, L, s+1)

    if load_type == 'Uniforme':
        for i in range(s + 1):
            moment[i] = -(-q*L*L/12 + q*L*x[i]/2 - q*x[i]*x[i]/2)

        plt.title('Moment Diagram')
        plt.xlabel('x (m)')
        plt.ylabel('M (kN.m)')
        plt.fill_between(x, 0, moment, color='blue', alpha=0.2)
        plt.plot(x, moment, color='blue', marker='')
        plt.show()
    else:
        print('Não implementado ainda.')


if __name__ == '__main__':
    plot_m_diagram('Uniforme', 1, 3)
