import numpy as np
from PIL import Image

img = Image.open('lena.png')
img = np.asarray(img)

flat = img.flatten()

def get_histogram(image, bins):
    histogram = np.zeros(bins)

    for pixel in image:
        histogram[pixel] += 1
    
    return histogram

hist = get_histogram(flat, 256)

def cumsum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)

cs = cumsum(hist)

nj = (cs - cs.min()) * 255
N = cs.max() - cs.min()

cs = nj / N
cs = cs.astype('uint8')

img_new = cs[flat]
img_new = np.reshape(img_new, img.shape)

im = Image.fromarray(img_new)
im.save("equilized.png")