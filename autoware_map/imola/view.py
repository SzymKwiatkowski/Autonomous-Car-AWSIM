import cv2
import numpy as np
import json

def export2d(map_image, replace_val: np.uint8, max_val: np.uint8):
    map_to_export = map_image
    for i in range(map_image.shape[0]):
        for j in range(map_image.shape[1]):
            if (map_image[i, j] == replace_val):
                map_to_export[i, j] = max_val
    return map_to_export
    

im = cv2.imread('imola.pgm',-1) 
ret,thresh2 = cv2.threshold(im,240,255,cv2.THRESH_BINARY_INV)

# erode
kernel1 = np.ones((25, 25), np.uint8)
image = cv2.dilate(thresh2, kernel1)

ret, thresh3 = cv2.threshold(image,240,255,cv2.THRESH_BINARY_INV)

map_known = export2d(thresh2, 255, 50)

image_replaced = thresh3 + map_known

map_export = export2d(image_replaced, 0, 100)

data = {
    'heigth': map_export.shape[0],
    'width': map_export.shape[1],
    'map': map_export.tolist()
}

json_string = json.dumps(data)
with open('json_data.json', 'w') as outfile:
    outfile.write(json_string)

cv2.imshow('track', image_replaced)
cv2.waitKey(0)