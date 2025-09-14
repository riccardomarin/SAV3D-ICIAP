import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import scipy.io as sio
from sklearn.cluster import KMeans
import cv2 

### TASK 1 -- D1 Eigenfunctions

# 1: Building the adjacency matrix
n = 50

A = np.zeros((n, n))
a = np.array([i for i in np.arange(1,n)]) 
A[np.arange(a.size),a] = 1

# Enforcing symmetry
A = np.logical_or(A, A.T).astype(np.int32)
print(A)

# It generates:
# A = np.array([  [0,1,0,0,0],
#                 [1,0,1,0,0],
#                 [0,1,0,1,0],
#                 [0,0,1,0,1],
#                 [0,0,0,1,0]])


# 2: Computing the Laplacian
# Vertex degree
D = np.sum(A, axis=0)
L = np.diag(D) - A

print(L)

# 3: Compute the eigenvectors
evals, evecs = np.linalg.eigh(L)


# Create a networkx Graph object starting from our adjacency matrix
G = nx.from_numpy_array(A)

# Nodes displacement for visualization
pos = {i : np.asarray([i,0]) for i in np.arange(0,n)}

# 4: Plot the graph with one eigenfunction

fig, all_axes = plt.subplots(1, 4)
ax = all_axes.flat
# Visualizing the eig_n eigenfunction
nx.draw(G, pos, node_color=evecs[:,1] , node_size=40, cmap=plt.cm.bwr, vmin=np.min(evecs), vmax=np.max(evecs), ax=ax[0])
nx.draw(G, pos, node_color=evecs[:,2] , node_size=40, cmap=plt.cm.bwr, vmin=np.min(evecs), vmax=np.max(evecs), ax=ax[1])
nx.draw(G, pos, node_color=evecs[:,3] , node_size=40, cmap=plt.cm.bwr, vmin=np.min(evecs), vmax=np.max(evecs), ax=ax[2])
nx.draw(G, pos, node_color=evecs[:,4] , node_size=40, cmap=plt.cm.bwr, vmin=np.min(evecs), vmax=np.max(evecs), ax=ax[3])

# Set margins for the axes so that nodes aren't clipped
for a in ax:
    a.margins(0.10)
fig.tight_layout()
plt.show()

# Eigenvalues plot
plt.plot(evals)
plt.show()

#########
# Since the eigenfunctions of the Laplacian provide an analougy with the Fourier Transform, 
# we can use them as a basis to perform low-pass filtering of the functions.
# 4: Low pass filtering

# Define a function
f = np.ones(evecs.shape[0]) * -1
f[15:25] = 1
f[40:43] = 1
# nx.draw(G,pos, node_color=f, node_size=40, cmap=plt.cm.bwr, vmin=np.min(evecs), vmax=np.max(evecs))
# plt.show()

k = 10

# Truncating the basis
evecs_trim = evecs[:,0:k]

# Synthesis and analysis with truncated basis
f_recon = np.matmul(evecs_trim, np.matmul(evecs_trim.T, f))

# Computing the reconstruction error
err = np.sqrt(np.sum(np.square(f_recon - f)))

fig, all_axes = plt.subplots(1, 2)
ax = all_axes.flat

nx.draw(G,pos, node_color=f, node_size=40, cmap=plt.cm.bwr, vmin=np.min(evecs), vmax=np.max(evecs), ax=ax[0])
plt.title('Error: ' + "{:10.3f}".format(err))
nx.draw(G,pos, node_color=f_recon, node_size=40, cmap=plt.cm.bwr, vmin=np.min(evecs), vmax=np.max(evecs), ax=ax[1])
plt.show()


##### 
# MINNESOTA

minnesota = sio.loadmat('./dataset/spectral/minnesota_g.mat')

D = np.sum(minnesota['A'], axis=0)
L = np.diag(D).astype(np.int32) - minnesota['A'].astype(np.int32)

evals_min, evecs_min = np.linalg.eigh(L)

# We can visualize the eigenfunctions over the graph. Notice that the first two eigenfunctions are constant! 
# This is due to disconnected components on a graph (i.e., the multiplicity of the $0$ eigenvalue equals the number of graph components, 
# and each $0$ eigenvalue is associated with a constant function localized on the component).

G = nx.from_numpy_array(minnesota['A'])
pos = minnesota['pos']

fig, all_axes = plt.subplots(3, 3)
ax = all_axes.flat

# Visualizing the eig_n eigenfunction
for i in np.arange(0,9):
    im = nx.draw(G, pos, node_color=evecs_min[:,i] , node_size=40, cmap=plt.cm.bwr, ax=ax[i])


# Set margins for the axes so that nodes aren't clipped
for a in ax:
    a.margins(0.10)
fig.tight_layout()

plt.show()

### Visualizing eigenvalues
plt.plot(evals_min)
plt.title('Eigenvalues Minnesota')
plt.show()