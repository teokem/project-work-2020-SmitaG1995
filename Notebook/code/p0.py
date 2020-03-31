# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:57:43 2020
@author: Smita Ganguly
"""
from  scipy import *
from  matplotlib.pyplot import *
from splat import *

def p0(data, m2q, cq, tof_no_p, v_mb, EF):
    ''' this function calculates the momentum of the particles that gain no 
    momentum after ionization
    Input :
        m2q - array of m2q labels
        cq - array of charge labels
        tof_no_p array of corresponding tof for no momentum
        v_mb the molecular beam velocity (m/s)
        EF - the electric field in spectrometer
    output :
        dataframe with p0x, p0y,p0z'''
        
    [x0, y0, t0] = splat(m2q,tof_no_p, v_mb)
    e = 1.602176634e-19 #elementary charge
    p0x = m2q * 1.6605e-27 *(x0 /t0) * 1e6 
    p0y = m2q * 1.6605e-27 *(y0 /t0) * 1e6 
    p0z = cq * e * EF * (t0 - tof_no_p) *1e-9
    
    map_dict3 = { m2q[i] : p0x[i] for i in range(len(m2q)) }
    map_dict4 = { m2q[i] : p0y[i] for i in range(len(m2q)) }
    map_dict5 = { m2q[i] : p0z[i] for i in range(len(m2q)) }
    
    data['p0x'] = data.m2q.map(map_dict3)
    data['p0y'] = data.m2q.map(map_dict4)
    data['p0z'] = data.m2q.map(map_dict5)

    return data