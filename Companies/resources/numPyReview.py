"""
    Review of main numPy features

    *https://docs.scipy.org/doc/numpy/user/quickstart.html
    *https://www.youtube.com/watch?v=xECXZ3tyONo
    *http://scipy-lectures.org/
    *http://cs231n.github.io/python-numpy-tutorial/#numpy

    *Introduction to Statistical Learning http://www-bcf.usc.edu/~gareth/ISL/
"""
import numpy

# create zero array
zero_float_ar = numpy.zeros(6, numpy.float, 'F')  # with default values
print(zero_float_ar)
zero_int_ar = numpy.zeros(6, numpy.int8, 'C')
print(zero_int_ar)

print(zero_int_ar.shape)
zero_int_ar.shape = (6, 1)
print(zero_int_ar)
zero_int_ar.shape = (3, 2)
print(zero_int_ar)

# create one array
one_ar = numpy.ones(8)
print(one_ar)

# create empty array
empty_ar = numpy.empty(3)
print(empty_ar)

lin_ar = numpy.linspace(5, 11, 4)
print(lin_ar)

# create array from list
real_array = numpy.array([3, 5])
print(real_array)

real_array = numpy.array([3, 5])
print(real_array)

real_array = numpy.array([[3, 4], [5, 6]])
print(real_array)

# create array of random
print(numpy.random.seed(0))
random_ar = numpy.random.randint(1, 8, 10)
print(random_ar)


###########################################################
# 2D array or image processing
from skimage import io
photo = io.imread('Capture-Zalando.PNG')
print(type(photo))
print(photo.shape)


import matplotlib.pyplot as plt
#plt.imshow(photo)
#plt.show()

#plt.imshow(photo[::-1])
# plt.show()
#plt.imshow(photo[:, ::-1])
#plt.imshow(photo[650:800, 800:1100])
#plt.imshow(photo[::2, ::2])
#plt.show()

# photo_sin = numpy.sign(photo)
print(numpy.sign(photo))
print(numpy.prod(photo))
print(numpy.mean(photo))
print(numpy.std(photo))
print(numpy.var(photo))
print(numpy.min(photo))
print(numpy.max(photo))
print(numpy.argmin(photo))
print(numpy.argmax(photo))

#plt.imshow(photo_sin)
#plt.show()


another_ar = numpy.array([1, 2, 3, 4, 5])
print(another_ar > 3)

#photo_mask = numpy.where(photo > 128, 200, 0)
# plt.imshow(photo_mask)
# plt.show()

a_array = numpy.array([1, 2, 3, 4, 5])
b_array = numpy.array([6, 7, 8, 9, 10])
print(a_array + b_array)
print(a_array + 5)
print(a_array * b_array)
print(a_array * 5)
print(a_array @ b_array)

#plt.imshow(photo[:, :, 0].T)
#plt.show()

sort_array = numpy.array([61, 17, 81, 19, 10])
print(sort_array)

print(numpy.sort(sort_array))
#print(sort_array)
sort_array.sort()
print(sort_array)



