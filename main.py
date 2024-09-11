'''
Author: Yishuo Wang
Date: 2024-07-29 14:13:37
LastEditors: Yishuo Wang
LastEditTime: 2024-08-02 03:45:01
FilePath: /blue_sea_sky_v5/main.py
Description: the main function for merge the results

Copyright (c) 2024 by Yishuo Wang, All Rights Reserved. 
'''
import get_date
import gradient_front_zone
import merge_by_union
import front_zone_ai
import process_by_region
import remove_lines_ai
import process_by_region_ai
import edge_following
import os
import netCDF4 as nc
import numpy as np
import pickle

txt_path = './predictParam.txt'

types = ['SST', 'SSS', 'density']

if __name__ == '__main__':
    # first, read the predictParam.txt
    lines = open(txt_path, encoding= 'UTF-8').readlines()
    exec(lines[1][:-1])
    exec(lines[3][:-1])
    exec(lines[5][:-1])
    exec(lines[7][:-1])
    exec(lines[9])
    
    date_list = get_date.date_range(StartTime, EndTime)
    
    for date in date_list:
        date = str(date)
        year = date[0:4]
        month = date[4:6]
        day = date[6:8]

        if analysisType == 'phy':
            for type in range(len(types)):
                input_path = input + types[type] + '/' + year + '/'
                files = os.listdir(input_path)
                for file in files:
                    # judge if the file begin with the date
                    if file[0:8] == date:
                        # read the file
                        data = nc.Dataset(input_path + file)
                        
                        lon = data.variables['lon'][:]
                        lat = data.variables['lat'][:]

                        magnitude_SCS, direction_SCS, frontzone_SCS, lon_SCS, lat_SCS = gradient_front_zone.get_gradient_front_zone(data, 0, type)
                        magnitude_BHD, direction_BHD, frontzone_BHD, lon_BHD, lat_BHD = gradient_front_zone.get_gradient_front_zone(data, 1, type)
                        magnitude_KUR, direction_KUR, frontzone_KUR, lon_KUR, lat_KUR = gradient_front_zone.get_gradient_front_zone(data, 2, type)
                        magnitude_STP, direction_STP, frontzone_STP, lon_STP, lat_STP = gradient_front_zone.get_gradient_front_zone(data, 3, type)

                        # process the four regions first
                        front_matrix_SCS, distance_SCS, fronts_SCS = process_by_region.process_gradient_frontzone(output, magnitude_SCS, direction_SCS, frontzone_SCS, 0, type, year, date)
                        front_matrix_BHD, distance_BHD, fronts_BHD = process_by_region.process_gradient_frontzone(output, magnitude_BHD, direction_BHD, frontzone_BHD, 1, type, year, date)
                        front_matrix_KUR, distance_KUR, fronts_KUR = process_by_region.process_gradient_frontzone(output, magnitude_KUR, direction_KUR, frontzone_KUR, 2, type, year, date)
                        front_matrix_STP, distance_STP, fronts_STP = process_by_region.process_gradient_frontzone(output, magnitude_STP, direction_STP, frontzone_STP, 3, type, year, date)

                        process_by_region.process(output, magnitude_SCS, front_matrix_SCS, distance_SCS, fronts_SCS, 0, type, year, date)
                        process_by_region.process(output, magnitude_BHD, front_matrix_BHD, distance_BHD, fronts_BHD, 1, type, year, date)
                        process_by_region.process(output, magnitude_KUR, front_matrix_KUR, distance_KUR, fronts_KUR, 2, type, year, date)
                        process_by_region.process(output, magnitude_STP, front_matrix_STP, distance_STP, fronts_STP, 3, type, year, date)

                        # merge the results
                        gradient_magnitude = merge_by_union.merge_real_number(magnitude_SCS, magnitude_BHD, magnitude_KUR, magnitude_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        gradient_direction = merge_by_union.merge_real_number(direction_SCS, direction_BHD, direction_KUR, direction_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        front_zone = merge_by_union.merge_binary(frontzone_SCS, frontzone_BHD, frontzone_KUR, frontzone_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        front_matrix = merge_by_union.merge_binary(front_matrix_SCS, front_matrix_BHD, front_matrix_KUR, front_matrix_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        distance = merge_by_union.merge_real_number(distance_SCS, distance_BHD, distance_KUR, distance_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)

                        process_by_region.process_gradient_frontzone(output, gradient_magnitude, gradient_direction, front_zone, 4, type, year, date)

                        front_matrix_temp = front_matrix.copy()

                        front_matrix_temp[np.isnan(front_matrix_temp)] = 0

                        fronts = edge_following.follow(front_matrix_temp, gradient_direction)

                        process_by_region.process(output, gradient_magnitude, front_matrix, distance, fronts, 4, type, year, date)
                        
                        data.close()
        
        elif analysisType == 'ai':
            for type in range(len(types)):
                input_path = input + types[type] + '/' + year + '/'
                files = os.listdir(input_path)
                for file in files:
                    # judge if the file begin with the date
                    if file[0:8] == date:
                        # read the file
                        data = nc.Dataset(input_path + file)
                        
                        lon = data.variables['lon'][:]
                        lat = data.variables['lat'][:]

                        magnitude_SCS, direction_SCS, frontzone_SCS, lon_SCS, lat_SCS = gradient_front_zone.get_gradient_front_zone(data, 0, type)
                        magnitude_BHD, direction_BHD, frontzone_BHD, lon_BHD, lat_BHD = gradient_front_zone.get_gradient_front_zone(data, 1, type)
                        magnitude_KUR, direction_KUR, frontzone_KUR, lon_KUR, lat_KUR = gradient_front_zone.get_gradient_front_zone(data, 2, type)
                        magnitude_STP, direction_STP, frontzone_STP, lon_STP, lat_STP = gradient_front_zone.get_gradient_front_zone(data, 3, type)

                        # merge the results
                        frontzone_SCS_ai = front_zone_ai.get_front_zone(data, 0, type)
                        frontzone_BHD_ai = front_zone_ai.get_front_zone(data, 1, type)
                        frontzone_KUR_ai = front_zone_ai.get_front_zone(data, 2, type)
                        frontzone_STP_ai = front_zone_ai.get_front_zone(data, 3, type)
                        
                        # remove the irrelevant lines 
                        frontzone_BHD_ai = remove_lines_ai.remove(frontzone_BHD_ai, 1)
                        frontzone_KUR_ai = remove_lines_ai.remove(frontzone_KUR_ai, 2)
                        
                        front_matrix_SCS, distance_SCS, fronts_SCS, front_matrix_SCS_ai, distance_SCS_ai, fronts_SCS_ai = process_by_region_ai.process_gradient_frontzone(output, magnitude_SCS, direction_SCS, frontzone_SCS_ai, frontzone_SCS, 0, type, year, date)
                        front_matrix_BHD, distance_BHD, fronts_BHD, front_matrix_BHD_ai, distance_BHD_ai, fronts_BHD_ai = process_by_region_ai.process_gradient_frontzone(output, magnitude_BHD, direction_BHD, frontzone_BHD_ai, frontzone_BHD, 1, type, year, date)
                        front_matrix_KUR, distance_KUR, fronts_KUR, front_matrix_KUR_ai, distance_KUR_ai, fronts_KUR_ai = process_by_region_ai.process_gradient_frontzone(output, magnitude_KUR, direction_KUR, frontzone_KUR_ai, frontzone_KUR, 2, type, year, date)
                        front_matrix_STP, distance_STP, fronts_STP, front_matrix_STP_ai, distance_STP_ai, fronts_STP_ai = process_by_region_ai.process_gradient_frontzone(output, magnitude_STP, direction_STP, frontzone_STP_ai, frontzone_STP, 3, type, year, date)

                        process_by_region_ai.process(output, magnitude_SCS, front_matrix_SCS_ai, fronts_SCS, fronts_SCS_ai, distance_SCS, distance_SCS_ai, 0, type, year, date)
                        process_by_region_ai.process(output, magnitude_BHD, front_matrix_BHD_ai, fronts_BHD, fronts_BHD_ai, distance_BHD, distance_BHD_ai, 1, type, year, date)
                        process_by_region_ai.process(output, magnitude_KUR, front_matrix_KUR_ai, fronts_KUR, fronts_KUR_ai, distance_KUR, distance_KUR_ai, 2, type, year, date)
                        process_by_region_ai.process(output, magnitude_STP, front_matrix_STP_ai, fronts_STP, fronts_STP_ai, distance_STP, distance_STP_ai, 3, type, year, date)

                        # merge the results
                        gradient_magnitude = merge_by_union.merge_real_number(magnitude_SCS, magnitude_BHD, magnitude_KUR, magnitude_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        gradient_direction = merge_by_union.merge_real_number(direction_SCS, direction_BHD, direction_KUR, direction_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        front_zone_bayes = merge_by_union.merge_binary(frontzone_SCS, frontzone_BHD, frontzone_KUR, frontzone_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        front_zone_unet = merge_by_union.merge_binary(frontzone_SCS_ai, frontzone_BHD_ai, frontzone_KUR_ai, frontzone_STP_ai, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        distance_bayes = merge_by_union.merge_real_number(distance_SCS, distance_BHD, distance_KUR, distance_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        distance_unet = merge_by_union.merge_real_number(distance_SCS_ai, distance_BHD_ai, distance_KUR_ai, distance_STP_ai, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        front_matrix_bayes = merge_by_union.merge_binary(front_matrix_SCS, front_matrix_BHD, front_matrix_KUR, front_matrix_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)
                        front_matrix_unet = merge_by_union.merge_binary(front_matrix_SCS_ai, front_matrix_BHD_ai, front_matrix_KUR_ai, front_matrix_STP_ai, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon)

                        process_by_region_ai.process_gradient_frontzone(output, gradient_magnitude, gradient_direction, front_zone_unet, front_zone_bayes, 4, type, year, date)

                        front_matrix_temp = front_matrix_unet.copy()

                        front_matrix_temp[np.isnan(front_matrix_temp)] = 0

                        fronts_unet = edge_following.follow(front_matrix_temp, gradient_direction)

                        front_matrix_temp = front_matrix_bayes.copy()

                        front_matrix_temp[np.isnan(front_matrix_temp)] = 0

                        fronts_bayes = edge_following.follow(front_matrix_temp, gradient_direction)
                        
                        process_by_region_ai.process(output, gradient_magnitude, front_matrix_unet, fronts_bayes, fronts_unet, distance_bayes, distance_unet, 4, type, year, date)
                        
                        data.close()