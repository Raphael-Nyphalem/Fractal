# -*- coding: utf-8 -*-
"""
@author: hbouia (Created on Fri Oct 18 18:49:19 2013)
Ensembles de Julia
""" 
import numpy as np, matplotlib.pyplot as plt,time

c_ = 0.58


def f(z,c):
    fz=z*z+c
    return fz

def fZ(k,k1,k2):
    a=2*k*np.pi/na
    a=2*np.pi/na *(k1+(k2-k1)*(k-1.)/(na/2-1.))
    c=c_*complex(np.cos(a),np.sin(a))
    Z=np.zeros((nx,ny),float)
    for i in range(nx):
        for j in range(ny):
            z=Z0[i,j]
            for n in range(itermax):
                if np.abs(z)<=2:
                    z=f(z,c)
                else:
                    Z[i,j]=np.sqrt(n)
                    break
    return Z

nl=3
nc=6
na=2*nl*nc
itermax=300
xmin,xmax,ymin,ymax=[-2.,2.,-2.,2.]
nx,ny=200,200
x=np.linspace(xmin,xmax,nx)
y=np.linspace(ymin,ymax,ny).reshape(-1,1)
Z0=x+1j*y

fig = plt.figure()
fig.patch.set_facecolor('#FFFFFF')
titre=r"$Ensembles\ de\ Julia\ :\ z=z^2+c\ avec\ c=ccc\ e^{i\frac{2k\pi}{s_na}}$"
titre=titre.replace('s_na',str(na))
titre=titre.replace('ccc',str(c_))
fig.suptitle(titre, fontsize=24)
'''t0=time.clock()'''
for k in range(1,18):
    Z=fZ(k,1,nl*nc)
    ax=fig.add_subplot(nl,nc,k)
    ax.set_title('k = %d' % k,fontsize=14)
    im = plt.imshow(Z, interpolation='bicubic', cmap=plt.cm.hot)
    plt.axis('off')
plt.show()
'''t1=time.clock()
///print ('CPU = %10.3f sec.' %(t1-t0))'''
