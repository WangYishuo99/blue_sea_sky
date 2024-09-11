'''
Author: Yishuo Wang
Date: 2024-03-13 13:35:43
LastEditors: Yishuo Wang
LastEditTime: 2024-07-25 15:38:04
FilePath: /blue_sea_sky/gradient_calculation.py
Description: calculate the gradient magnitude and direction, plot and save them

Copyright (c) 2024 by Yishuo Wang, All Rights Reserved. 
'''

from scipy.ndimage import sobel
import numpy as np
import matplotlib.pyplot as plt

# the resolution of the data
resolution = 9

def magnitude_and_direction_gradient(SST):
    gradient_x = sobel(SST, axis=0)
    gradient_y = sobel(SST, axis=1)

    # Calculate the gradient magnitude
    gradient_magnitude = np.hypot(gradient_x, gradient_y)

    # change the unit
    gradient_magnitude = gradient_magnitude / resolution

    # Calculate the gradient direction
    # the range is -pi to pi
    gradient_direction = np.arctan2(gradient_y, gradient_x)

    return gradient_magnitude, gradient_direction

