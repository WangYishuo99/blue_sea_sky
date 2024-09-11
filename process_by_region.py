'''
Author: Yishuo Wang
Date: 2024-07-31 23:40:37
LastEditors: Yishuo Wang
LastEditTime: 2024-08-02 00:28:52
FilePath: /blue_sea_sky_v4/process_by_region.py
Description: process the 4 regions 

Copyright (c) 2024 by Yishuo Wang, All Rights Reserved. 
'''
import plot_save_region as psr
import os
import zone2line as z2l
import length_width_strength_calculation as lwsc
import txt_func as tf

region_names = ['南中国海', '渤黄东海', '黑潮', '热带太平洋', '西太平洋']
types_names = ['温度', '盐度', '密度']
types = ['SST', 'SSS', 'density']

def process_gradient_frontzone(output, magnitude, direction, frontzone, region, type, year, date):
    # 1. gradient magnitude
    output_path = output + '贝叶斯/' + region_names[region] + '/' + year + '/' + types_names[type] + '/梯度/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '梯度识别图片.png'
    psr.plot_gradient(magnitude, output_path, graph_name, types[type], region)

    # 2. front zone
    output_path = output + '贝叶斯/' + region_names[region] + '/' + year + '/' + types_names[type] + '/锋区/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '锋区识别图片.png'
    psr.plot_front_zone(frontzone, output_path, graph_name, types[type], region)

    # 3. front
    # if it is the west pacific, we do not need to calculate the front for its highly complexity
    if region != 4:
        front_matrix, distance, fronts = z2l.zone2line(frontzone, direction)
        return front_matrix, distance, fronts
    else:
        return 
    

def process(output, magnitude, front_matrix, distance, fronts, region, type, year, date):

    output_path = output + '贝叶斯/' + region_names[region] + '/' + year + '/' + types_names[type] + '/锋面/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '锋面识别图片.png'
    psr.plot_front(front_matrix, output_path, graph_name, types[type], region)

    # 4. strength
    strength = lwsc.strength_calculation(magnitude, fronts)

    output_path = output + '贝叶斯/' + region_names[region] + '/' + year + '/' + types_names[type] + '/强度/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '强度识别图片.png'
    psr.plot_strength(strength, output_path, graph_name, types[type], region)

    output_path = output + '贝叶斯/' + region_names[region] + '/' + year + '/' + types_names[type] + '/强度/详情数据/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '强度识别数据.txt'
    tf.daily_strength(strength, len(fronts), types[type], output_path + graph_name)

    # 5. width
    width = lwsc.width_calculation(magnitude, distance, fronts)

    output_path = output + '贝叶斯/' + region_names[region] + '/' + year + '/' + types_names[type] + '/宽度/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '宽度识别图片.png'
    psr.plot_width(width, output_path, graph_name, types[type], region)

    output_path = output + '贝叶斯/' + region_names[region] + '/' + year + '/' + types_names[type] + '/宽度/详情数据/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '宽度识别数据.txt'
    tf.daily_width(width, len(fronts), output_path + graph_name)

    # 6. length
    length = lwsc.length_calculation(magnitude, fronts)

    output_path = output + '贝叶斯/' + region_names[region] + '/' + year + '/' + types_names[type] + '/长度/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '长度识别图片.png'
    psr.plot_length(length, output_path, graph_name, types[type], region)

    output_path = output + '贝叶斯/' + region_names[region] + '/' + year + '/' + types_names[type] + '/长度/详情数据/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '长度识别数据.txt'
    tf.daily_length(length, len(fronts), output_path + graph_name)