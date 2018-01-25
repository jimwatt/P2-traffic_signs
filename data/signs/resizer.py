from skimage.transform import resize
from skimage.io import imread
from skimage.io import imsave

numimages = 10

for ii in range(numimages):
    fname = "sign{}.jpg".format(ii)
    
    image = imread(fname)
    image = resize(image,(32,32,3),mode='reflect')
    
    fout= "./resized/sign{}.png".format(ii)
    imsave(fout,image)

    