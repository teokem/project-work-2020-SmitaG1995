# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:21:11 2020
@author: Smita Ganguly
"""
from  scipy import *
from  matplotlib.pyplot import *
import numpy as np

def tof_no_p(m2q,t0,factor):
    '''Input:
        m2q      [a.u] The m2q labels interested in
        t0       The time-zero shift [ns].
        factor     The conversion factor
        Output:
        TOF_no_p   The TOF values corresponding to m2q labels if particles had no p'''
    tof = t0 + factor*sqrt(m2q)
    return tof