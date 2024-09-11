'''
Author: Yishuo Wang
Date: 2024-07-29 18:18:24
LastEditors: Yishuo Wang
LastEditTime: 2024-08-01 10:08:02
FilePath: /blue_sea_sky_v3/front_zone_ai.py
Description: an ai model to calculate the gradient and front zone

Copyright (c) 2024 by Yishuo Wang, All Rights Reserved. 
'''
import numpy as np
from keras.models import load_model

regions_lon_start = [100, 115, 135, 135]
regions_lon_end = [140, 140, 180, 180]
regions_lat_start = [0, 18, 20, 0]
regions_lat_end = [21, 41, 48, 21]

types = ['SST', 'SSS', 'density']
types_names_in_file = ['analysed_sst', 'sss', 'density']
regions_names_ai =['SCS', 'BHD', 'KUR', 'STP']

# Define the thresholds
upper_threshold = 90
lower_threshold = 80

model_path = './unet_models/'

pad_patterns = [((0, 0), (2, 2), (0, 0)), ((0, 0), (2, 2), (2, 2)), ((0, 0), (0, 0), (2, 2)), ((0, 0), (2, 2), (2, 2))]
pad_patterns_sst = [((0, 0), (1, 0), (1, 0)), ((0, 0), (2, 1), (2, 1)), ((0, 0), (1, 1), (0, 0)), ((0, 0), (1, 0), (0, 0))]

def get_front_zone(data, region, type):
    # 1. prepossess
    lon_start = regions_lon_start[region]
    lon_end = regions_lon_end[region]
    lat_start = regions_lat_start[region]
    lat_end = regions_lat_end[region]

    lon = data.variables['lon'][:]
    lat = data.variables['lat'][:]
    
    lon_index = np.where((lon >= lon_start) & (lon < lon_end))[0]
    lat_index = np.where((lat >= lat_start) & (lat < lat_end))[0]

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
    
    # 2. front_zone_ai

    model = load_model('./unet_models/' + types[type] + '_' + regions_names_ai[region] + '.keras')

    data_normalized = (data_temp - np.nanmean(data_temp)) /  np.nanstd(data_temp)

    data_normalized[np.isnan(data_normalized)] = 0

    if types[type] == 'SST':
        if regions_names_ai[region] == 'SCS':
            pad_pattern = pad_patterns_sst[0]
        elif regions_names_ai[region] == 'BHD':
            pad_pattern = pad_patterns_sst[1]
        elif regions_names_ai[region] == 'KUR':
            pad_pattern = pad_patterns_sst[2]
        else:
            pad_pattern = pad_patterns_sst[3]
    else:
        if regions_names_ai[region] == 'SCS':
            pad_pattern = pad_patterns[0]
        elif regions_names_ai[region] == 'BHD':
            pad_pattern = pad_patterns[1]
        elif regions_names_ai[region] == 'KUR':
            pad_pattern = pad_patterns[2]
        else:
            pad_pattern = pad_patterns[3]

    # add a dimension in first place
    data_normalized = np.expand_dims(data_normalized, axis = 0)
    data_padded = np.pad(data_normalized, pad_pattern, mode='constant')

    data_predicted = model.predict(data_padded)

    data_predicted = data_predicted[0, :, :, 0]

    data_depadded = data_predicted[pad_pattern[1][0]: data_predicted.shape[0] - pad_pattern[1][1], pad_pattern[2][0]: data_predicted.shape[1] - pad_pattern[2][1]]
    data_depadded[np.isnan(data_temp)] = np.nan
    # assign the 1 and 0
    data_depadded[data_depadded >= 0.5] = 1
    data_depadded[data_depadded < 0.5] = 0


    return data_depadded