'''
Author: Yishuo Wang
Date: 2024-08-01 10:10:04
LastEditors: Yishuo Wang
LastEditTime: 2024-08-02 02:41:37
FilePath: /blue_sea_sky_v4/process_by_region_ai.py
Description: the code for ai processing by region

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

def process_gradient_frontzone(output, magnitude, direction, frontzone, frontzone_bayes, region, type, year, date):
    # 1. gradient magnitude
    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/梯度/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '梯度识别图片.png'
    psr.plot_gradient(magnitude, output_path, graph_name, types[type], region)

    # 2. front zone
    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/锋区/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '锋区识别图片.png'
    psr.plot_front_zone(frontzone, output_path, graph_name, types[type], region)

    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/锋区/计算误差/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '识别准确度.txt'
    tf.daily_accuracy(frontzone, frontzone_bayes, output_path + graph_name)

    # 3. front
    if region != 4:
        front_matrix, distance, fronts = z2l.zone2line(frontzone_bayes, direction)
        front_matrix_ai, distance_ai, fronts_ai = z2l.zone2line(frontzone, direction)
        return front_matrix, distance, fronts, front_matrix_ai, distance_ai, fronts_ai
    else:
        return

def process(output, magnitude, front_matrix_ai, fronts, fronts_ai, distance, distance_ai, region, type, year, date):

    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/锋面/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '锋面识别图片.png'
    psr.plot_front(front_matrix_ai, output_path, graph_name, types[type], region)

    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/锋面/计算误差/'
    os.makedirs(output_path, exist_ok=True)
    front_graph_name = date + region_names[region]  + types_names[type] + '锋面位置误差.txt'
    tf.daily_front_error(fronts, fronts_ai, output_path + front_graph_name)

    # 4. strength
    strength = lwsc.strength_calculation(magnitude, fronts_ai)

    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/强度/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '强度识别图片.png'
    psr.plot_strength(strength, output_path, graph_name, types[type], region)

    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/强度/详情数据/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '强度识别数据.txt'
    tf.daily_strength(strength, len(fronts_ai), types[type], output_path + graph_name)

    # 5. width
    width_bayes = lwsc.width_calculation(magnitude, distance, fronts)
    width = lwsc.width_calculation(magnitude, distance_ai, fronts_ai)

    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/宽度/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '宽度识别图片.png'
    psr.plot_width(width, output_path, graph_name, types[type], region)

    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/宽度/详情数据/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '宽度识别数据.txt'
    tf.daily_width(width, len(fronts_ai), output_path + graph_name)

    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/宽度/计算误差/'
    os.makedirs(output_path, exist_ok=True)
    width_graph_name = date + region_names[region] + types_names[type] + '宽度误差.txt'
    tf.daily_width_error(width_bayes, width, output_path + width_graph_name)

    # 6. length
    length = lwsc.length_calculation(magnitude, fronts_ai)

    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/长度/结果图片/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '长度识别图片.png'
    psr.plot_length(length, output_path, graph_name, types[type], region)

    output_path = output + '深度学习/' + region_names[region] + '/' + year + '/' + types_names[type] + '/长度/详情数据/'
    os.makedirs(output_path, exist_ok = True)
    graph_name = date + region_names[region] + types_names[type] + '长度识别数据.txt'
    tf.daily_length(length, len(fronts_ai), output_path + graph_name)