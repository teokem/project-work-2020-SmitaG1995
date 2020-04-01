# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:57:43 2020
@author: Smita Ganguly
"""
from  scipy import *
from  matplotlib.pyplot import *
from matplotlib import pyplot as plt


def momentum_plot2(data, x1, y1, x2, y2, x3, y3, param, mass, norm = matplotlib.colors.LogNorm() ):
    ''' this function creates histogram plots of momentum while the parameter v1 is changed
    Input :
    the x, y data (can make a plot with two subplot)
    mass = the m2q you want to visualise
    output :
        figure'''
    data44 = data.loc[data['m2q'] == mass]
    
    plt.rcParams['font.size'] = 20
    
    fig = plt.figure(figsize=(18,5))
    ## first subplot
    x1 = data44[x1]
    y1 = data44[y1]
    
    plt.subplot(1, 3, 1)
    BinWidth = 0.5 #2d
    binp = np.arange(min(x1), max(x1), BinWidth)
    plt.hist2d(x1,y1,norm=matplotlib.colors.LogNorm(),bins =[binp,binp]) 
    plt.xlabel(x1.name)
    plt.ylabel(y1.name)
    plt.ylim(0, 150)
    plt.xlim(-150, 150)
    plt.tick_params(axis='both', labelsize=8)
    plt.grid(axis = 'y',color='r', linewidth=2)

    
    ## second subplot
    x2 = data44[x2]
    y2 = data44[y2]
    plt.subplot(1, 3, 2)
    plt.hist2d(x2,y2,norm=matplotlib.colors.LogNorm(),bins =[binp,binp]) #
    plt.xlabel(x2.name)
    plt.ylabel(y2.name)
    plt.ylim(0, 150)
    plt.xlim(-150, 150)
    plt.tick_params(axis='both', labelsize=8)    
    plt.grid(axis = 'y',color='r', linewidth=2)
    
    ## third subplot
    x3 = data44[x3]
    y3 = data44[y3]
    plt.subplot(1, 3, 3)
    plt.hist2d(x3,y3,norm=matplotlib.colors.LogNorm(),bins =[binp,binp]) #
    plt.xlabel(x3.name)
    plt.ylabel(y3.name)
    plt.ylim(0, 150)
    plt.xlim(-150, 150)
    plt.tick_params(axis='both', labelsize=8)
    plt.grid(axis = 'y',color='r', linewidth=2)
    
    plt.suptitle(param)

    plt.show()
    
    return 