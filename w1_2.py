# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\WINPYTHON\WinPython-32bit-2.7.6.2\settings\.spyder2\.temp.py
"""

# from scipy import misc
# from pylab import imread, imshow, gray, mean

# image = imread('lena.png')
# #image_to_show =mean(image,2) # to get a 2-D array
# imshow(image)
# gray()

# # l = misc.lena()
# # misc.imsave('lena.png', l) # uses the Image module (PIL)
# # import matplotlib.pyplot as plt
# # plt.imshow(l)
# # plt.show()
from scipy import misc
from PIL import Image
from scipy import ndimage
import scipy

def open_and_edit(file,*levels):   
    try:
        original = Image.open(file)
    except:
        print "Unable to load image"
    
    #pixels = original.getdata()
    #original.putdata(pixels, 1) 
    #original.show()
    data_arr_orig = scipy.misc.fromimage(original)
    #print type(data_arr)
    for level in levels:
        data_arr = np.copy(data_arr_orig) 
        for i in range(original.size[1]):
            for j in range(original.size[0]):
                data_arr[i,j][0] = (data_arr[i,j][0]/level)*level
                data_arr[i,j][1] = (data_arr[i,j][1]/level)*level
                data_arr[i,j][2] = (data_arr[i,j][2]/level)*level
                
        # rotated = original.rotate( 45, expand=1 )
        # rotated.show()
        out_name = "outfile_{x}.jpg".format(x = level)
        scipy.misc.imsave(out_name, data_arr)

if __name__ == "__main__":    
    open_and_edit("vmworld.jpg",2)
