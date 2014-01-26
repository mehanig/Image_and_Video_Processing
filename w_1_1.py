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
try:
    original = Image.open("f2b.jpg")
except:
    print "Unable to load image"

pixels = original.getdata()
original.putdata(pixels, 1)    
original.show()
# data_arr = scipy.misc.fromimage(original)
# print type(data_arr)
# for i in range(original.size[0]):
# 	for j in range(original.size[1]):
# 		data_arr[i,j] = [100,100,100]
# # original.show()
# print type(data_arr[1,1])
# print data_arr[1,1].data


# rotated = original.rotate( 45, expand=1 )

# rotated.show()
# scipy.misc.imsave('outfile.jpg', data_arr)