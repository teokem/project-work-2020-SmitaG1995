from scipy import *
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from skimage.feature import peak_local_max
from skimage import img_as_float
import numpy as np
from my_code.rot_mat import *
from my_code.rot_axes import *

def img_hotspot(i,x,y,BinWidth,theta,Graphics):
    '''calculates the hotspot in given 2d data'''
    binp = np.arange(min(x), max(x), BinWidth)
    x,y = rot_axes(x,y,theta)
    ## we use the same binwidth for x and y
    fig = plt.figure()
    hist2, xedges, yedges,img = plt.hist2d(x,y,bins =[binp,binp]) 
    plt.close(fig)
    ##rotate the matrix
    #hist2 = rot_mat(hist2,theta)
    
    #%%
    ##IMAGE PROCESSING
    im = img_as_float(np.transpose(hist2))
    # image_max is the dilation of im with a 20*20 structuring element
    # It is used within peak_local_max function
    image_max = ndi.maximum_filter(im, size=2.5, mode='constant')

    # Comparison between image_max and im to find the coordinates of local maxima
    coordinates = peak_local_max(im, min_distance=1,threshold_rel = 0.75 )
#, num_peaks =1
    # display results
    
    if Graphics == 1 :
        fig, axes = plt.subplots(1, 3, figsize=(8, 3), sharex=True, sharey=True)
        ax = axes.ravel()
        ax[0].imshow(im, cmap=plt.cm.gray)
        ax[0].axis('off')
        ax[0].set_title('Original')

        ax[1].imshow(image_max, cmap=plt.cm.gray)
        ax[1].axis('off')
        ax[1].set_title('Maximum filter')
    
        ax[2].imshow(im, cmap=plt.cm.gray)
        ax[2].autoscale(False)
        ax[2].plot(coordinates[:, 1], coordinates[:, 0], 'r.')
        ax[2].axis('off')
        ax[2].set_title('Peak local max')
    
        fig.tight_layout()
        fig.suptitle(i,fontsize=20)
    
    #calculate the hotspot (in image)
        peakx = np.sum(coordinates[:, 1])/np.size(coordinates[:, 1])
        peaky = np.sum(coordinates[:, 0])/np.size(coordinates[:, 0])
        plt.scatter(peakx, peaky, color='g', marker='+', s=1e5);
    
        plt.show()
    
    #calculate the center of mass
    cgx = np.sum(xedges[coordinates[:, 1]])/np.size(xedges[coordinates[:, 1]])
    cgy = np.sum(yedges[coordinates[:, 0]])/np.size(yedges[coordinates[:, 0]])
    
    return  cgx,cgy