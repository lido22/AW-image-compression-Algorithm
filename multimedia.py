"""
After Running the program if you want to decode 
run decode() in terminal
"""
import cv2
import numpy as np
import timeit

"""
input: imageName
output: flattened "which is a numpy array that contains the flattened image"
output: dimensios of the original image
"""
def readImage(imgName):
    img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)
    imgArray = np.array(img)
    flattened = imgArray.flatten()
    return flattened, imgArray.shape

#index is zero-based and marks where I will stop decoding
#7 in the start means print 8
def createDict(flat, delta):
    counter = 0
    arr = []
    prev = flat[0]
    l = len(flat)-1
    for i in flat:
        if abs(int(prev)-int(i)) > delta or counter==255:
            arr.append(counter)
            arr.append(prev)
            prev = i
            counter = 0
        counter += 1
    if(l+1 != len(arr)):
        arr.append(counter)
        arr.append(prev)
    return arr

imageName = input("Enter image Name: ")
delta = int(input("Enter Delta: "))
start = timeit.default_timer()
flat, dimensions = readImage(imageName)
arr = createDict(flat, delta)

dt = np.dtype('uint8')
code = np.array(arr, dt)
stop = timeit.default_timer()
print('Encoding Time: ', stop - start)  
np.savez_compressed("coded "+imageName, code) 

def decode():
    file = np.load("code.npz")
    start = timeit.default_timer()
    code = file.f.arr_0
    decod = []
    count = 0
    for j in range(int(len(code)/2)):
        for i in range(code[count]):
            decod.append(code[count+1])
        count += 2
    finalArr = np.reshape(np.array(decod, dtype=np.uint8), dimensions)
    stop = timeit.default_timer()
    print('Decoding Time: ', stop - start) 
    cv2.imwrite('decoded '+imageName, finalArr)