
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib
from skimage.io import imread
from PIL import Image 
import PIL 

def divideImage(image,subImagesNum):
        '''
        I want to subdivide my image into pieces
        '''
        if subImagesNum==0:
            return image
        else:
            images=[]
            height,width,channel=image.shape
            indexer= 4*subImagesNum
            for i in range(0,height,height // indexer):
                for j in range(0,width,width // indexer):
                    images.append(image[i:i+height//indexer,j:j+width//indexer])
            return images

image = divideImage(imread("SmallFile.png"), 1)
for i,each in enumerate(image):
        im1 = each.save("geeks{}.jpg".format(i))