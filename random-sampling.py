#!/usr/bin/env python3.9
# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
import scipy.optimize as optim

def poly(x,a0,a1,a2):
  y=np.log10(x)
  return a0*y*y+a1*y+a2

def rejection(rng,par):
  a=True
  emax=3.0
  emin=np.log10(0.8)
  m=(1.0/3.0)*(-4.0-np.log10(0.5))
  j=0
  while(a==True):
    xrnd=(emax-emin)*rng.random()+emin
    c=m*xrnd-0.25
    M=np.power(10.0,c)
    p=M*rng.random()
    q=np.power(10.0,par[0]*xrnd*xrnd+par[1]*xrnd+par[2])
    if p<q:
      a=False
    j+=1
  return 10.0**(xrnd),j

seed=100
N=1000000
rng=rnd.default_rng(seed)
es=np.zeros(N)
ktot=np.zeros(N)
ebins=np.arange(0.8,1000.8,0.8)
e=np.loadtxt('gamma-energy-spectrum.dat')
eg=np.loadtxt('sample-geant.txt')

sel=e[:,1]!=0.0
e0,e1=e[sel,0],e[sel,1]
p,pcov=optim.curve_fit(poly,e0,np.log10(e1))

for j in range(0,N):
  es[j],i=rejection(rng,p)
  ktot[j]=i
print(np.mean(ktot))

a=np.arange(-0.5,3.0,0.01)
fe=10.0**(p[0]*a*a+p[1]*a+p[2])
fig,ax=plt.subplots(nrows=1,ncols=1,sharex=False,sharey=True)
ax.plot(e0,e1,'o')
ax.hist(es,bins=ebins,density=True)
ax.hist(eg,bins=ebins,density=True,histtype='step')
ax.plot(10.0**(a),fe,'o')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
