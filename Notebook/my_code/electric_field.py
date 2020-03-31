# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:00:54 2020
@author: Smita Ganguly
"""
from  scipy import *
from  matplotlib.pyplot import *

#%% Calculate the electric field in spectrometer

def electric_field(vol1,vol2,dist):
    '''Input:
        voltage1      [V] The voltage at the lowest position electrode
        voltage2      [V] The voltage at the highest position electrode
        distance      [m] The distance between the electrodes
        Output:
            E             [V/m] The electric field strengths.'''
    E = (vol2 - vol1)/dist 
    return E