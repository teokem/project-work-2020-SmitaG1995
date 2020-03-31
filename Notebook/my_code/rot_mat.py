# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:33:01 2020
@author: Smita Ganguly
"""
from  scipy import *
from  matplotlib.pyplot import *
import numpy as np
from scipy import ndimage


def rot_mat(img,theta):
    '''the function rotates matrix v by angle theta (degrees)'''
    rot_image = ndimage.rotate(img, theta, reshape=True)
    return rot_image
    
