# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 04:02:17 2020
@author: Smita Ganguly
"""
from  scipy import *
from my_code.img_hotspot import *
import numpy as np
import matplotlib.pyplot as plt

def x0y0_calc(data,m,theta,BinWidth = 0.5,Graphics = 1):
    '''this function calculates the x0, y0 for the given mat data
    the data is rotated by theta
    m is the array of m2q labels
    binwidth is the width for histogram calculation of x y data (optional)
    
    It returns the x0, y0 lists '''
    
   # calculate x0, y0 for given m2q labels
    x0 = [] #lists are created
    y0 = []
    for i in m:
        data_filt = data.loc[data['m2q'] == i]
        c= img_hotspot(i,data_filt['x'], data_filt['y'], BinWidth,theta,Graphics)
        # plots are shown for hotspot detection
        x0.append(c[0])
        y0.append(c[1])
        del data_filt #to avoid mistakes
        if Graphics == 0:
            plt.close('all')
    return x0, y0

