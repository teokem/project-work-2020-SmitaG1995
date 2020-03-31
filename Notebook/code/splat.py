# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:28:05 2020
@author: Smita Ganguly
"""
from  scipy import *
from  matplotlib.pyplot import *
from tof_no_p import *
import numpy as np

def splat(m2q,tof_no_p, v_mb):
    '''Calculates the splat position(x,y,z) (assumed that molecular beam is in x direction)
    Input:
        m2q - array of m2q labels
        tof_no_p array of corresponding tof for no momentum
        v_mb the molecular beam velocity (m/s)
    Output:
        [x0 y0 t0]'''
    v = np.array([1, 0, 0]) #assumption that molecular beam velocity has only x direction
    x0 = v[0] * v_mb * tof_no_p * 1e-6
    y0 = v[1] * tof_no_p * 1e-6 #zeros
    t0 = v[2] + tof_no_p  #
    return [x0, y0, t0]
    