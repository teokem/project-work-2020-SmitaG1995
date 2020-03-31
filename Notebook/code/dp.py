# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:57:43 2020
@author: Smita Ganguly
"""
from  scipy import *
from  matplotlib.pyplot import *



def dp(data, ef):
    ''' this function calculates the momentum of the particles  after ionization
    Input :
        
        EF - the electric field in spectrometer
    output :
        dataframe with p0x, p0y,p0z'''
        
    e = 1.602176634e-19
    data['px'] = data['m2q'] * 1.6605e-27 *(data['x'] /data['tof']) * 1e6
    data['py'] = data['m2q'] * 1.6605e-27 *(data['y'] /data['tof']) * 1e6
    data['pz'] = data['charge'] * e * ef * (data['tof'] - data['tof_no_p']) * 1e-9

    data['dpx'] = (data['px'] - data['p0x']) / 1.9929e-24 ### momentum in atomic units
    data['dpy'] = (data['py'] - data['p0y']) / 1.9929e-24 ### momentum in atomic units
    data['dpz'] = (data['pz'] - data['p0z']) / 1.9929e-24 ### momentum in atomic units
    data['dp_norm'] = sqrt(data['dpx'] **2 + data['dpy'] **2 + data['dpz'] **2)
    
    for i in ['p0x','p0y','p0z','px','py','pz']:
        del data[i] ##too many columns in dataframe 
    
    return data