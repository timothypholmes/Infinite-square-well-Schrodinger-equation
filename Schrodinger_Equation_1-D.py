#! /usr/bin/env python3

'''
Analytical solution to the Time-Dependent Schrodinger equation
for a particle in an infinite square well

author: Timothy Holmes
email: tpholmes7@gmail.com
website: http://timothypholmes.github.io

'''

######################################################################
#Import libraries
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
Global constants
defined at the bottom
----------------
hbar = 6.58211951*10**-16
x =
L = x[-1]
m = int(938000000)#Mass
num = int(500)
dt = 2000 #Time step
'''

class time_evolution:
    '''
    Class that take an approach at solving the Time-Dependent Schrodinger
    equation for an unbounded particle in an infinite square well and
    generates a gaussian wave function for the psi initial.
    '''
    def __init__(self,hbar,m,quantum_number,total_time,dt,
    L,x,n,a,l):
        self.hbar = hbar
        self.mass = m
        self.quantum_number = quantum_number
        self.total_time = total_time
        self.time_step = dt
        self.length = L
        self.x = x
        self.n = n
        self.a = a

        '''
        Parameters
        ----------
        x : array, float
            length-N array of evenly spaced spatial coordinates
        psi_x0 : array, complex
            Initial wave function at time t0 = 0
        psi_xt : array, complex
            Time-dependent Schrodinger equation
        hbar : scalar, float
            value of planck's constant
        m : scalar, float
            particle mass
        quantum_number : scalar, integer
            values of conserved quantities in a quantum system
        total_time : float
        Time_step : scalar, integer
        '''

    def gaussan_wave_packet(self,x,x0,l,a):
        A = (1/(4*a**2))**(1/4.0)
        self.psi_x0 = A*(np.exp((-(x - x0)**2)
            /(4*a**2))*np.exp(1j*l*x)).reshape(len(x),1)
        #return psi_x0
        print("psi_x0: " + str(self.psi_x0.shape))


    def normalize(self):
        A = ( 1/(np.sqrt(np.trapz((np.conj(self.psi_x0[:,0])
            *self.psi_x0[:,0]), x[:,0]))))
        self.psi_x0_normalized = A*self.psi_x0
        print("Scalar A: " + str(A))
        print("Psi0 Normalized: " + str(self.psi_x0_normalized.shape))


    def phi_n(self):
        self.phi = ( np.sqrt( 2/L ) * np.sin( (n * np.pi * x) /L ) )
        print("Phi: " + str(self.phi.shape))


    def energy_eigenvalues(self):
        self.En = ( ( np.power(n,2))*(np.pi**2)*(hbar**2))/(2*m*L**2)
        print("En: " + str(self.En.shape))


    def C_n(self, quantum_number):
        self.Cn = np.zeros((quantum_number,1),dtype=complex)

        for i in range(0,quantum_number):

            self.Cn[i,0] = np.trapz( (np.conj(self.phi)
                *self.psi_x0_normalized)[:,i], x[:,0] )

        self.Cn = self.Cn.reshape(1,500)
        print("Cn: " + str(self.Cn.shape))


    def schrodinger_equation(self, total_time):

        count = 0

        for j in range(0, total_time, dt):

            time = j
            self.psi_xt = np.zeros((len(x),1),dtype=complex).reshape(len(x),1)

            for k in range(0, quantum_number):

                self.psi_xt[:,0] = self.psi_xt[:,0] + (self.Cn[0,k]
                    * self.phi[:,k] * (np.exp((-1j * self.En[0,k]*time)/hbar)))

                count += 1

######################################################################
# plot

            plt.plot(x, np.real(self.psi_xt),'r',
                label=r'$\mathbb{R} \psi(x,t)$', linewidth = 0.75)
            plt.plot(x, np.imag(self.psi_xt),'b',
                label=r'$\mathbb{C} \psi(x,t)$', linewidth = 0.75)
            plt.plot(x, np.abs(self.psi_xt),'y',
                label=r'$|\psi(x,t)|$', linewidth = 0.75)

            x_min = min(self.x[:,0])
            x_max = max(self.x[:,0])
            psi_min = -A
            psi_max = A
            plt.xlim((x_min, x_max))
            plt.ylim((psi_min, psi_max))

            plt.legend(prop=dict(size=6))
            psi_x_line, = plt.plot([], [], c='r')
            V_x_line, = plt.plot([], [], c='k')
            left_wall_line = plt.axvline(0, c='k', linewidth=2)
            right_well_line = plt.axvline(x[-1], c='k', linewidth=2)

            plt.pause(0.01)
            plt.draw()
            plt.clf()
            plt.cla()

        print('The number of iterations: ' + str(count))

######################################################################
# animate

######################################################################
#Predefined parameters

quantum_number = 500
x = np.linspace(0,100,1000).astype(complex).reshape(1000,1)
n = np.arange(1,quantum_number+1).reshape(1,quantum_number)
x0 = 30
a = 5
l = 2
A = (1/(4*a**2))**(1/4.0)
m = 1#int(938000000)
hbar = 1#6.58211951*10**(-16)
total_time = 1*10**2
L = x[-1]
dt = 10

######################################################################
#Welcome statement

print('-'*100 + '\n' + 'Analytical solution to the Time-Dependent Schrodinger equation \n' +
'for an unbounded particle in an infinite square well \n \n' +
'author: Timothy Holmes \n' +
'email: tpholmes7@gmail.com \n' +
'website: http://timothypholmes.github.io \n \n' +
'-'*100)

########################################################################
#Inputs for customization

choose = input('Enter 1 to run or enter any key to customize: ')
if choose == 1:
    pass
else:
    quantum_number = int(input('Quantum number: '))
    length_of_well = int(input('Length of the well (nm): '))
    x0 = int(input('Center of wave packet (i.e. center of well): '))
    a = int(input('Enter the width of wave packet (sigma): '))
    l = int(input('Enter number of waves: '))
    total_time = int(input('Total run time: '))
    dt = int(input('Enter time step: '))
    dx = int(input('Enter length intervals: '))
    x = np.linspace(0,int(length_of_well),int(dx)).astype(complex).reshape(int(dx),1)

test = time_evolution(hbar,m,quantum_number,total_time,dt,
L,x,n,a,l)
print(test.gaussan_wave_packet(x,x0,l,a))
test.normalize()
test.phi_n()
test.energy_eigenvalues()
test.C_n(500)
print(test.schrodinger_equation(total_time))
