'''
Author: Yishuo Wang
Date: 2024-06-27 16:05:39
LastEditors: Yishuo Wang
LastEditTime: 2024-07-25 18:44:22
Description: the function is to calculate the length, width and strength of the detected fronts
'''
import numpy as np

def strength_calculation(magnitude, data):

    strength = np.zeros_like(magnitude)
    strength[np.isnan(magnitude)] = np.nan

    strength_list = [0] * len(data)

    for k in range(len(data)):
        for j in range(len(data[k])):
            x = data[k][j][0]
            y = data[k][j][1]
            strength_list[k] += magnitude[x][y]
        # calculate the average value
        strength_list[k] = strength_list[k] / len(data[k])

    for k in range(len(data)):
        for j in range(len(data[k])):
            x = data[k][j][0]
            y = data[k][j][1]
            strength[x][y] = strength_list[k]

    return strength

def width_calculation(magnitude, distance, data):

    width = np.zeros_like(magnitude)
    width[np.isnan(magnitude)] = np.nan

    width_list =  [0]*len(data)

    for k in range(len(data)):
        for j in range(len(data[k])):
            x = data[k][j][0]
            y = data[k][j][1]
            width_list[k] += distance[x][y]
        # calculate the average value
        width_list[k] = width_list[k] / len(data[k])

    for k in range(len(data)):
        for j in range(len(data[k])):
            x = data[k][j][0]
            y = data[k][j][1]
            width[x][y] = width_list[k] * 9

    return width

def length_calculation(magnitude, data):

    length = np.zeros_like(magnitude)
    length[np.isnan(magnitude)] = np.nan

    length_list =  [0]*len(data)

    for k in range(len(data)):
        for j in range(len(data[k])):
            x = data[k][j][0]
            y = data[k][j][1]
            length_list[k] += 1

    for k in range(len(data)):
        for j in range(len(data[k])):
            x = data[k][j][0]
            y = data[k][j][1]
            length[x][y] = length_list[k] * 9

    return length