# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 00:44:51 2020
@author: Smita Ganguly
"""
from  scipy import *
from  matplotlib.pyplot import *
from x0y0_calc import *
from scipy import stats


def theta_calib(data,m,tof_no_p,theta_min,theta_max,step):
    slope = 1
    for theta in np.arange(theta_min,theta_max,step):  #
        ## calculate xo, y0, tof_no_p
        x0, y0  = x0y0_calc(data,m,theta,Graphics = 0)
        slopey, intercept, r_value, p_value, std_err = stats.linregress(tof_no_p,y0)
        if np.abs(slopey) < np.abs(slope):
            slope = slopey
            theta_opt = theta
        #if np.abs(slopey) > np.abs(slope):
            #break
    return theta_opt

    
    
