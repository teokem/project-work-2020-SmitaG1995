# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:57:43 2020
@author: Smita Ganguly
"""
from  scipy import *
from  matplotlib.pyplot import *
from matplotlib import pyplot as plt
from scipy.signal import find_peaks

def momentum_plot(data, x1, y1, x2, y2, param, mass, norm = matplotlib.colors.LogNorm() ):
    ''' this function creates histogram plots of momentum while the parameter v1 is changed
    Input :
    the x, y data (can make a plot with two subplot)
    mass = the m2q you want to visualise
    output :
        figure'''
    data44 = data.loc[data['m2q'] == mass]
    
    plt.rcParams['font.size'] = 20
    
    fig = plt.figure(figsize=(13,5))
    ## first subplot
    x1 = data44[x1]
    y1 = data44[y1]
    
    plt.subplot(1, 2, 1)
    BinWidth = 1 #2d
    binp = np.arange(min(x1), max(x1), BinWidth)
    plt.hist2d(x1,y1,norm=matplotlib.colors.LogNorm(),bins =[binp,binp]) #
    plt.xlabel(x1.name)
    plt.ylabel(y1.name)
    plt.ylim(0, 150)
    plt.xlim(-150, 150)
    
    ## second subplot
    x2 = data44[x2]
    
    plt.subplot(1, 2, 2)
    BinWidth = 2.5 #1d
    binq = np.arange(min(x2), max(x2), BinWidth)
    if y2 == 0:
        n, b, patches = plt.hist(x2,bins = binq) #1d hist
        bin_max = np.where(n == n.max())
        plt.scatter(b[bin_max][0], n.max(), s=80,marker='*',c='r')
        plt.text(50,n.max(),'%d' %b[bin_max][0])
        plt.xlabel(x2.name)
        plt.ylabel('Counts')
        plt.xlim(-150, 150)
    else:
        y2 = data44[y2]
        plt.hist2d(x2,y2,norm=matplotlib.colors.LogNorm(),bins =[binp,binp])
        plt.xlabel(x2.name)
        plt.ylabel(y2.name)
        plt.ylim(0, 150)
        plt.xlim(-150, 150)
    
    
    plt.suptitle(param)

    plt.show()
    
    return 