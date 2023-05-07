import cv2
import numpy as np
import json
import math

def load_trajectory(trajectory_path: str):
    f = open(trajectory_path)
    data =  json.loads(f.read())
    f.close()
    return data['trajectory']


def transform_trajectory(trajectory, resolution: float, height: int, origin):
    path = []
    for point in trajectory:
        # path.append([int((point[0] - origin[0])/resolution), height - int((point[1] - origin[1])/resolution)])
        path.append([int(height - int(math.ceil((point[1] - origin[1])/resolution))), int(math.ceil((point[0] - origin[0])/resolution))])
    
    return path
    

im = cv2.imread('../imola/imola.pgm',-1)
resolution = 0.05 # form imola.yaml
map_origin = [-24.1, -8.52, 0]
trajectory_path = 'waypoints.json'
trajectory = load_trajectory(trajectory_path)

transformed_trajectory = transform_trajectory(trajectory, resolution, im.shape[0], map_origin)
# print(im.shape)
# print(transformed_trajectory)

for point in transformed_trajectory:
    im[point[0], point[1]] = 0
    # print(im[point[0], point[1]])
    
cv2.imshow('path', im)
cv2.waitKey(0)