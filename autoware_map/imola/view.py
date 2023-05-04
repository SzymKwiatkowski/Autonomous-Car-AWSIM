import cv2
import numpy as np

def export2d(map_image):
    map_to_export = np.zeros(map_image.shape, dtype=int)
    for i in range(map_image.shape[0]):
        for j in range(map_image.shape[1]):
            if (map_image[i, j] == 0):
                map_to_export[i, j] = 100
    return map_to_export
    

im = cv2.imread('imola.pgm',-1) 
ret,thresh2 = cv2.threshold(im,240,255,cv2.THRESH_BINARY_INV)
map_export = export2d(thresh2)
print(map_export)

cv2.imshow('track', thresh2)
cv2.waitKey(0)