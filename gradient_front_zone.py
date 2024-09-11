'''
Author: Yishuo Wang
Date: 2024-07-29 14:24:58
LastEditors: Yishuo Wang
LastEditTime: 2024-07-29 18:17:19
FilePath: /blue_sea_sky/gradient_front_zone.py
Description: calculate the gradient and front zone of the 4 regions

Copyright (c) 2024 by Yishuo Wang, All Rights Reserved. 
'''
import numpy as np
import gradient_calculation
import threshold
import bayesian_decision

regions_lon_start = [100, 115, 135, 135]
regions_lon_end = [140, 140, 180, 180]
regions_lat_start = [0, 18, 20, 0]
regions_lat_end = [21, 41, 48, 21]

types_names_in_file = ['analysed_sst', 'sss', 'density']

# Define the thresholds
upper_threshold = 90
lower_threshold = 80

def get_gradient_front_zone(data, region, type):
    # 1. prepossess
    lon_start = regions_lon_start[region]
    lon_end = regions_lon_end[region]
    lat_start = regions_lat_start[region]
    lat_end = regions_lat_end[region]

    lon = data.variables['lon'][:]
    lat = data.variables['lat'][:]
    
    lon_index = np.where((lon >= lon_start) & (lon < lon_end))[0]
    lat_index = np.where((lat >= lat_start) & (lat < lat_end))[0]

    lon_extracted = lon[lon_index]
    lat_extracted = lat[lat_index]

    if type == 0:
            # if it is sst, then should minus 273.15 and treat the nan values
        data_temp = data.variables[types_names_in_file[type]][:, lat_index, lon_index]
        data_temp = data_temp[0]
        data_temp = np.array(data_temp)
        data_temp = data_temp - 273.15
        data_temp[np.where(data_temp > 100)]=np.nan
        data_temp[np.where(data_temp < -100)]=np.nan

    elif type == 1:
        # if it is sss, set the nan values
        data_temp = data.variables[types_names_in_file[type]][lat_index, lon_index]
        data_temp = np.array(data_temp)
        data_temp[np.where(data_temp > 100)]=np.nan
        data_temp[np.where(data_temp < -100)]=np.nan
    
    else:
        data_temp = data.variables[types_names_in_file[type]][lat_index, lon_index]
        data_temp = np.array(data_temp)
    
    # 2. gradient
    gradient_magnitude, gradient_direction = gradient_calculation.magnitude_and_direction_gradient(data_temp)
    
    # 3. front_zone
    marked_matrix, p10, p20 = threshold.thresholds_calculation(gradient_magnitude, upper_threshold, lower_threshold)

    marked_matrix, LDE, BD, prior_matrix, likelihood_fornt_matrix, likelihood_nonfront_matrix = bayesian_decision.bayesian(marked_matrix, p10, p20, gradient_magnitude, data_temp)

    marked_matrix[np.where(marked_matrix == 2)] = 0
    
    return gradient_magnitude, gradient_direction, marked_matrix, lon_extracted, lat_extracted
