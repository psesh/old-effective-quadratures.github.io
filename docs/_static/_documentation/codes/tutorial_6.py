from equadratures import *
import numpy as np
import matplotlib.pyplot as plt


dimensions = 1
M = 12
param = Parameter(distribution='Uniform', lower=0, upper=1., order=1)
myParameters = [param for i in range(dimensions)] # one-line for loop for parameters
x_train = np.mat([0,0.0714,0.1429,0.2857,0.3571,0.4286,0.5714,0.6429,0.7143,0.7857,0.9286,1.0000], dtype='float64')
y_train = np.mat([6.8053,-1.5184,1.6416,6.3543,14.3442,16.4426,18.1953,28.9913,27.2246,40.3759,55.3726,72.0], dtype='float64')
x_train = np.reshape(x_train, (M, 1))
y_train = np.reshape(y_train, (M, 1))

myBasis = Basis('Univariate')
poly = Poly(myParameters, myBasis, method='least-squares', \
    sampling_args={'sample-points':x_train, 'sample-outputs':y_train} )
poly.set_model()
N = 100
x_test = np.reshape(np.linspace(0, 1, N), (N, 1) )

# Plot the results
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
for i in range(0, M):
        plt.scatter(x_train[i,0], y_train[i,0], marker='o', s=80, color='tomato')
plt.plot(x_test, poly.get_polyfit(x_test), 'k-')
plt.xlabel('$X$', fontsize=13)
plt.ylabel('$Y$', fontsize=13)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.savefig('../Figures/tutorial_6_fig_a.png' , dpi=200, bbox_inches='tight', pad_inches=0.1)

# Now let's increase the order!
param = Parameter(distribution='Uniform', lower=0, upper=1., order=2)
myParameters = [param for i in range(dimensions)] # one-line for loop for parameters
x_train = np.mat([0,0.0714,0.1429,0.2857,0.3571,0.4286,0.5714,0.6429,0.7143,0.7857,0.9286,1.0000], dtype='float64')
y_train = np.mat([6.8053,-1.5184,1.6416,6.3543,14.3442,16.4426,18.1953,28.9913,27.2246,40.3759,55.3726,72.0], dtype='float64')
x_train = np.reshape(x_train, (M, 1))
y_train = np.reshape(y_train, (M, 1))

myBasis = Basis('Univariate')
poly = Poly(myParameters, myBasis, method='least-squares', \
    sampling_args={'sample-points':x_train, 'sample-outputs':y_train} )
poly.set_model()
N = 100
x_test = np.reshape(np.linspace(0, 1, N), (N, 1) )

# Plot the results
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
for i in range(0, M):
        plt.scatter(x_train[i,0], y_train[i,0], marker='o', s=80, color='tomato')
plt.plot(x_test, poly.get_polyfit(x_test), 'k-')
plt.xlabel('$X$', fontsize=13)
plt.ylabel('$Y$', fontsize=13)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.savefig('../Figures/tutorial_6_fig_b.png' , dpi=200, bbox_inches='tight', pad_inches=0.1)