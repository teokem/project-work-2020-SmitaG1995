# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:19:27 2020
@author: Smita Ganguly
"""
from  scipy import *
from  matplotlib.pyplot import *
import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)
    
def rot_axes(x,y,theta):
    x= np.array(x)
    y= np.array(y)
    R , theta_0 = cart2pol(x,y)
    theta_out = theta_0 + (theta*pi/180)
    x,y = pol2cart(R,theta_out)
    return (x,y) 
    
    