'''
Author: Yishuo Wang
Date: 2024-07-19 10:40:18
LastEditors: Yishuo Wang
LastEditTime: 2024-07-31 09:35:33
Description: the funs for txt statistics
'''
import numpy as np

def daily_accuracy(front_zone_bayes, front_zone_unet, output):
    
    # calculate the number of same value
    same = 0
    rows, cols = front_zone_bayes.shape
    for i in range(0, rows):
        for j in range(0, cols):
            if np.isnan(front_zone_unet[i][j]):
                same += 1
            elif front_zone_bayes[i][j] == front_zone_unet[i][j]:
                same += 1
    accuracy = same / (rows * cols)

    # make the accuracy to be percentile and reserve 2 decimal places
    accuracy = round(accuracy * 100, 2)
    str_accuracy = str(accuracy)

    # save the accuracy to a txt file, if the file does not exist, create it
    with open(output, 'w', encoding = 'UTF-8') as f:
        f.write('识别准确率为: ' + str_accuracy + '%')

def daily_front_error(fronts_bayes, fronts_unet, output):
    length_intersection = 0

    for front_unet in fronts_unet:
        for point_unet in front_unet:
            for front_bayes in fronts_bayes:
                if point_unet in front_bayes:
                    length_intersection += 1

    length_bayes = 0
    for front_bayes in fronts_bayes:
        length_bayes += len(front_bayes) 
                    
    accuracy = (length_intersection * 9) / length_bayes
    accuracy = round(accuracy, 2)

    # save the accuracy to a txt file, if the file does not exist, create it
    with open(output, 'w', encoding = 'UTF-8') as f:
        f.write('锋面识别位置误差(km): ' + str(accuracy) + '\n')

def daily_width_error(width_bayes, width_unet, output):
        width_bayes[np.where(width_bayes == 0)] = np.nan
        width_unet[np.where(width_unet == 0)] = np.nan
        
        width_error = np.abs(width_bayes - width_unet)
       
        mean_error = np.nanmean(width_error)
        mean_error = round(mean_error, 2)
    
        # save the error to a txt file, if the file does not exist, create it
        with open(output, 'w', encoding = 'UTF-8') as f:
            f.write('平均宽度误差(km): ' + str(mean_error) + '\n')

def daily_strength(strength, number_fronts, type, output):

    strength[np.where(strength == 0)] = np.nan
    max_strength = np.nanmax(strength)
    # reserve 2 decimal places
    max_strength = round(max_strength, 2)
    min_strength = np.nanmin(strength)
    min_strength = round(min_strength, 2)
    mean_strength = np.nanmean(strength)
    mean_strength = round(mean_strength, 2)
    median_strength = np.nanmedian(strength)
    median_strength = round(median_strength, 2)

    if type == 'SST':
        unit_strength = '°C/km'
    elif type == 'SSS':
        unit_strength = 'PSU/km'
    else:
        unit_strength = 'kg/m^3/km'

    # save the strength to a txt file, if the file does not exist, create it
    with open(output, 'w', encoding = 'UTF-8') as f:
        f.write('锋面数量(个): ' + str(number_fronts) + '\n')
        f.write('最大强度(' + unit_strength + '): ' + str(max_strength) + '\n')
        f.write('最小强度(' + unit_strength + '): ' + str(min_strength) + '\n')
        f.write('平均强度(' + unit_strength + '): ' + str(mean_strength) + '\n')
        f.write('中位强度(' + unit_strength + '): ' + str(median_strength) + '\n')

def daily_width(strength, number_fronts, output):
    
    strength[np.where(strength == 0)] = np.nan
    max_strength = np.nanmax(strength)
    # reserve 2 decimal places
    max_strength = round(max_strength, 2)
    min_strength = np.nanmin(strength)
    min_strength = round(min_strength, 2)
    mean_strength = np.nanmean(strength)
    mean_strength = round(mean_strength, 2)
    median_strength = np.nanmedian(strength)
    median_strength = round(median_strength, 2)

    # save the strength to a txt file, if the file does not exist, create it
    with open(output, 'w', encoding = 'UTF-8') as f:
        f.write('锋面数量(个): ' + str(number_fronts) + '\n')
        f.write('最大宽度(km): ' + str(max_strength) + '\n')
        f.write('最小宽度(km): ' + str(min_strength) + '\n')
        f.write('平均宽度(km): ' + str(mean_strength) + '\n')
        f.write('中位宽度(km): ' + str(median_strength) + '\n')

def daily_length(strength, number_fronts, output):

    strength[np.where(strength == 0)] = np.nan
    max_strength = np.nanmax(strength)
    # reserve 2 decimal places
    max_strength = round(max_strength, 2)
    min_strength = np.nanmin(strength)
    min_strength = round(min_strength, 2)
    mean_strength = np.nanmean(strength)
    mean_strength = round(mean_strength, 2)
    median_strength = np.nanmedian(strength)
    median_strength = round(median_strength, 2)

    # save the strength to a txt file, if the file does not exist, create it
    with open(output, 'w', encoding = 'UTF-8') as f:
        f.write('锋面数量(个): ' + str(number_fronts) + '\n')
        f.write('最大长度(km): ' + str(max_strength) + '\n')
        f.write('最小长度(km): ' + str(min_strength) + '\n')
        f.write('平均长度(km): ' + str(mean_strength) + '\n')
        f.write('中位长度(km): ' + str(median_strength) + '\n')