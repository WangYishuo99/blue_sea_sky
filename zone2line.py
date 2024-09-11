'''
Author: Yishuo Wang
Date: 2024-07-29 16:09:34
LastEditors: Yishuo Wang
LastEditTime: 2024-07-29 16:15:36
FilePath: /blue_sea_sky/zone2line.py
Description: the function making front zone to front line 

Copyright (c) 2024 by Yishuo Wang, All Rights Reserved. 
'''
from skimage import morphology
import numpy as np

import edge_following
import edge_pruning

min_area_px = 100

def zone2line(marked_matrix, gradient_direction):
    converted_matrix = marked_matrix.copy()
    # make the nan values be 0
    converted_matrix[np.where(np.isnan(converted_matrix))] = 0
    # calculate the skeleton and distance
    skel, distance =morphology.medial_axis(converted_matrix, return_distance=True)

    new_skel = edge_pruning.skel_pruning_DSE(skel, distance, min_area_px)

    fronts = edge_following.follow(new_skel, gradient_direction)

    # discard the fronts shorter than 12(>99km)
    fronts = [front for front in fronts if len(front) >= 12]

    front_matrix = np.zeros_like(marked_matrix)

    for k in range(len(fronts)):
        for j in range(len(fronts[k])):
            x = fronts[k][j][0]
            y = fronts[k][j][1]
            front_matrix[x][y] = 1

    front_matrix[np.isnan(marked_matrix)] = np.nan

    return front_matrix, distance, fronts