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

ret, thresh3 = cv2.threshold(image,240,255,cv2.THRESH_BINARY)

map_known = export2d(thresh2, 255, 50)

image_replaced = thresh3 + map_known

map_export = export2d(image_replaced, 0, 100)

# data = {
#     'heigth': map_export.shape[0],
#     'width': map_export.shape[1],
#     'map': map_export.tolist()
# }

# json_string = json.dumps(data)
# with open('json_data.json', 'w') as outfile:
#     outfile.write(json_string)

# cv2.imshow('track', thresh3)
# cv2.waitKey(0)

edges = cv2.Canny(image=thresh3, threshold1=100, threshold2=200) # Canny Edge Detection
sobelxy = cv2.Sobel(src=thresh3, ddepth=cv2.CV_8U, dx=0, dy=1, ksize=1)

contours, hierarchy = cv2.findContours(sobelxy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# print(len(contours))
# 18, 16, 15, 14, 13, 11, 10, 8, 6, 4, 2, 0 - outside path
# ids = [18, 15, 14, 13, 11, 10, 8, 6, 4, 2, 0]
# upper = [18]
# lower = [15, 14, 13, 11, 10, 8, 6, 4, 2, 0]
# lower.reverse()
# contour = []
# for id in ids:
#     contour.append(contours[id])
    
# up_cont = []
# for id in upper:
#     up_cont.append(contours[id])
    
# down_cont = []
# for id in lower:
#     down_cont.append(contours[id])
height = im.shape[0]
print(height)
path = []
for cnt in contours:
    for point in cnt:
        path.append([int(point[0][0]), int(height - point[0][1])])

map_cp = np.zeros(thresh2.shape, dtype=np.uint8)
cv2.drawContours(map_cp, contours, -1, (255,255,255), 1)
contours2, hierarchy = cv2.findContours(map_cp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# contours_result = [contours[18], contours2[0]]
# empty = np.zeros(thresh2.shape, dtype=np.uint8)
# cv2.drawContours(empty, contour, -1, (255,255,255), 1)
cv2.imshow('track', sobelxy)
cv2.imshow('canny', map_cp)
cv2.waitKey(0)
print(contours[18])
traj = {
    'heigth': map_cp.shape[0],
    'width': map_cp.shape[1],
    'trajectory': path
}
json_string = json.dumps(traj)
with open('traj.json', 'w') as outfile:
    outfile.write(json_string)