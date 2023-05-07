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
        path.append([int(height - int(math.ceil((point[1] - origin[1])/resolution))), int(math.ceil((point[0] - origin[0])/resolution))])
    
    return path
    
def load_map(map_dir: str):
    im = cv2.imread(map_dir,-1)
    map_origin = [-24.1, -8.52, 0]
    return [im, 0.05, map_origin]

def draw_path_on_map(map, trajectory, origin, resolution):
    transformed_trajectory = transform_trajectory(trajectory, resolution, map.shape[0], origin)
    for point in transformed_trajectory:
        map[point[0], point[1]] = 0
    
    return map
    