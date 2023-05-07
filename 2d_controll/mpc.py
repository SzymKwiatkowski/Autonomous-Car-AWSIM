from utils.trajectory_util import load_map
from utils.trajectory_util import load_trajectory
from utils.trajectory_util import draw_path_on_map

import cv2

def draw_reference_trajectory():
    trajectory = load_trajectory('data/waypoints.json')
    map, resolution, map_origin = load_map('data/imola.pgm')
    map_with_trajectory = draw_path_on_map(map, trajectory, map_origin, resolution)
    
    cv2.imshow('Trajectory', map_with_trajectory)
    cv2.waitKey(0)
    

draw_reference_trajectory()

    
