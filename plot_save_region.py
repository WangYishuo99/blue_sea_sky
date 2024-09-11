'''
Author: Yishuo Wang
Date: 2024-03-27 11:10:25
LastEditors: Yishuo Wang
LastEditTime: 2024-08-02 11:13:46
FilePath: /blue_sea_sky_v5/plot_save_region.py
Description: the funcition is to add projection to the plotted files

Copyright (c) 2024 by Yishuo Wang, All Rights Reserved. 
'''

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# plot for different regions
region_extents = [[100, 140, 0, 21], [115, 140, 18, 41], [135, 180, 20, 48], [135, 180, 0, 21], [100, 180, 0, 48]]
region_x_ticks = [[100, 105, 110, 115, 120, 125, 130, 135, 140], [115, 120, 125, 130, 135, 140], [135, 140, 145, 150, 155, 160, 165, 170, 175, 180], [135, 140, 145, 150, 155, 160, 165, 170, 175, 180], [100, 120, 140, 160, 180]]
region_y_ticks = [[0, 3, 6, 9, 12, 15, 18, 21], [18, 21, 24, 27, 30, 33, 36, 39], [20, 24, 28, 32, 36, 40, 44, 48], [0, 3, 6, 9, 12, 15, 18, 21], [0, 8, 16, 24, 32, 40, 48]]

# define the colobar size
fraction_size = 0.025

def plot_gradient(gradient, output, graph_name, type, i):
    
    # Plot and save the gradient magnitude
    fig1 = plt.figure(figsize=(10, 7))
    ax = fig1.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    plt.imshow(gradient, cmap='jet', extent = region_extents[i], origin='lower', transform=ccrs.PlateCarree(), zorder = 1)

    # create the map
    ax.set_xlim(region_extents[i][0], region_extents[i][1]), ax.set_ylim(region_extents[i][2], region_extents[i][3])
    ax.coastlines()
    ax.add_feature(cfeature.LAND, edgecolor='black')

    ax.set_xticks(region_x_ticks[i], crs=ccrs.PlateCarree())
    ax.set_yticks(region_y_ticks[i], crs=ccrs.PlateCarree())

    # Set the x-axis and y-axis labels
    plt.xlabel('°E')
    plt.ylabel('°N')

    year = graph_name[0:4]
    month = graph_name[4:6]
    day = graph_name[6:8]

    if type == 'SST':
        plt.title('SST Gradient Magnitude in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Gradient Magnitude (°C/km)', fraction=fraction_size, pad=0.04)
    elif type == 'SSS':
        plt.title('SSS Gradient Magnitude in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Gradient Magnitude (PSU/km)', fraction=fraction_size, pad=0.04)
    elif type == 'density':
        plt.title('Density Gradient Magnitude in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Gradient Magnitude (kg/m^3/km)', fraction=fraction_size, pad=0.04)
        
    cbar.mappable.set_clim(0, 1)

    plt.savefig(output + graph_name, dpi=300)
    plt.close()

def plot_front_zone(front_zone, output, graph_name, type, i):

    # Plot and save the gradient magnitude
    fig1 = plt.figure(figsize=(10, 7))
    ax = fig1.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    plt.imshow(front_zone, cmap='binary', extent = region_extents[i], origin='lower', transform=ccrs.PlateCarree(), zorder = 1)

    # create the map
    ax.set_xlim(region_extents[i][0], region_extents[i][1]), ax.set_ylim(region_extents[i][2], region_extents[i][3])
    ax.coastlines()
    ax.add_feature(cfeature.LAND, edgecolor='black')

    ax.set_xticks(region_x_ticks[i], crs=ccrs.PlateCarree())
    ax.set_yticks(region_y_ticks[i], crs=ccrs.PlateCarree())

    # Set the x-axis and y-axis labels
    plt.xlabel('°E')
    plt.ylabel('°N')

    year = graph_name[0:4]
    month = graph_name[4:6]
    day = graph_name[6:8]

    if type == 'SST':
        plt.title('SST Front Zone in ' + year + '-' + month  + '-' + day)
    elif type == 'SSS':
        plt.title('SSS Front Zone in ' + year + '-' + month  + '-' + day)
    elif type == 'density':
        plt.title('Density Front Zone in ' + year + '-' + month  + '-' + day)

    plt.savefig(output + graph_name, dpi=300)
    plt.close()   
    
def plot_front(front_matrix, output, graph_name, type, i):

    # Plot and save the gradient magnitude
    fig1 = plt.figure(figsize=(10, 7))
    ax = fig1.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    plt.imshow(front_matrix, cmap='binary', extent = region_extents[i], origin='lower', transform=ccrs.PlateCarree(), zorder = 1)

    # create the map
    ax.set_xlim(region_extents[i][0], region_extents[i][1]), ax.set_ylim(region_extents[i][2], region_extents[i][3])
    ax.coastlines()
    ax.add_feature(cfeature.LAND, edgecolor='black')

    ax.set_xticks(region_x_ticks[i], crs=ccrs.PlateCarree())
    ax.set_yticks(region_y_ticks[i], crs=ccrs.PlateCarree())

    # Set the x-axis and y-axis labels
    plt.xlabel('°E')
    plt.ylabel('°N')

    year = graph_name[0:4]
    month = graph_name[4:6]
    day = graph_name[6:8]

    if type == 'SST':
        plt.title('SST Front in ' + year + '-' + month  + '-' + day)
    elif type == 'SSS':
        plt.title('SSS Front in ' + year + '-' + month  + '-' + day)
    elif type == 'density':
        plt.title('Density Front in ' + year + '-' + month  + '-' + day)

    plt.savefig(output + graph_name, dpi=300)
    plt.close() 

def plot_strength(strength_matrix, output, graph_name, type, i):

    # make the 0 value to nan, to beautify the plot
    strength_matrix[strength_matrix < 0.01] = np.nan

    # Plot and save the gradient magnitude
    if i != 4:
        fig1 = plt.figure(figsize=(10, 7))
    else:
        fig1 = plt.figure(figsize=(40, 28))

    ax = fig1.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    plt.imshow(strength_matrix, cmap='jet', extent = region_extents[i], origin='lower', transform=ccrs.PlateCarree(), zorder = 1)

    # create the map
    ax.set_xlim(region_extents[i][0], region_extents[i][1]), ax.set_ylim(region_extents[i][2], region_extents[i][3])
    ax.coastlines()
    ax.add_feature(cfeature.LAND, edgecolor='black')

    ax.set_xticks(region_x_ticks[i], crs=ccrs.PlateCarree())
    ax.set_yticks(region_y_ticks[i], crs=ccrs.PlateCarree())

    # make the x and y ticks bigger
    if i == 4:
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)

    # Set the x-axis and y-axis labels
    if i == 4:
        plt.xlabel('°E', fontsize=20)
        plt.ylabel('°N', fontsize=20)
    else:
        plt.xlabel('°E')
        plt.ylabel('°N')
    
    year = graph_name[0:4]
    month = graph_name[4:6]
    day = graph_name[6:8]
    
    if type == 'SST':
        plt.title('SST Front Strength in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Gradient Magnitude (°C/km)', fraction=fraction_size, pad=0.04)
    elif type == 'SSS':
        plt.title('SSS Front Strength in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Gradient Magnitude (PSU/km)', fraction=fraction_size, pad=0.04)
    elif type == 'density':
        plt.title('Density Front Strength in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Gradient Magnitude (kg/m^3/km)', fraction=fraction_size, pad=0.04)

    if i == 4:
        # adjust the colorbar font size
        cbar.ax.tick_params(labelsize=20)
        # adjust the colorbar label font size
        cbar.ax.yaxis.label.set_size(20)
        
    cbar.mappable.set_clim(0, 0.75)

    plt.savefig(output + graph_name, dpi=300)
    plt.close() 

def plot_width(width_matrix, output, graph_name, type, i):

    width_matrix[width_matrix < 9] = np.nan

    # Plot and save the gradient magnitude
    if i != 4:
        fig1 = plt.figure(figsize=(10, 7))
    else:
        fig1 = plt.figure(figsize=(40, 28))

    ax = fig1.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    plt.imshow(width_matrix, cmap='jet', extent = region_extents[i], origin='lower', transform=ccrs.PlateCarree(), zorder = 1)

    # create the map
    ax.set_xlim(region_extents[i][0], region_extents[i][1]), ax.set_ylim(region_extents[i][2], region_extents[i][3])
    ax.coastlines()
    ax.add_feature(cfeature.LAND, edgecolor='black')

    ax.set_xticks(region_x_ticks[i], crs=ccrs.PlateCarree())
    ax.set_yticks(region_y_ticks[i], crs=ccrs.PlateCarree())

    # make the x and y ticks bigger
    if i == 4:
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)

    # Set the x-axis and y-axis labels
    if i == 4:
        plt.xlabel('°E', fontsize=20)
        plt.ylabel('°N', fontsize=20)
    else:
        plt.xlabel('°E')
        plt.ylabel('°N')

    year = graph_name[0:4]
    month = graph_name[4:6]
    day = graph_name[6:8]
    
    if type == 'SST':
        plt.title('SST Front Width in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Width (km)', fraction=fraction_size, pad=0.04)
    elif type == 'SSS':
        plt.title('SSS Front Width in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Width (km)', fraction=fraction_size, pad=0.04)
    elif type == 'density':
        plt.title('Density Front Width in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Width (km)', fraction=fraction_size, pad=0.04)

    if i == 4:
        # adjust the colorbar font size
        cbar.ax.tick_params(labelsize=20)
        # adjust the colorbar label font size
        cbar.ax.yaxis.label.set_size(20)

    cbar.mappable.set_clim(9, 57)     

    plt.savefig(output + graph_name, dpi=300)
    plt.close() 

def plot_length(length_matrix, output, graph_name, type, i):

    length_matrix[length_matrix < 100] = np.nan
    
    # Plot and save the gradient magnitude
    if i != 4:
        fig1 = plt.figure(figsize=(10, 7))
    else:
        fig1 = plt.figure(figsize=(40, 28))
        
    ax = fig1.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    plt.imshow(length_matrix, cmap='jet', extent = region_extents[i], origin='lower', transform=ccrs.PlateCarree(), zorder = 1)

    # create the map
    ax.set_xlim(region_extents[i][0], region_extents[i][1]), ax.set_ylim(region_extents[i][2], region_extents[i][3])
    ax.coastlines()
    ax.add_feature(cfeature.LAND, edgecolor='black')

    ax.set_xticks(region_x_ticks[i], crs=ccrs.PlateCarree())
    ax.set_yticks(region_y_ticks[i], crs=ccrs.PlateCarree())

    # make the x and y ticks bigger
    if i == 4:
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)

    # Set the x-axis and y-axis labels
    if i == 4:
        plt.xlabel('°E', fontsize=20)
        plt.ylabel('°N', fontsize=20)
    else:
        plt.xlabel('°E')
        plt.ylabel('°N')

    year = graph_name[0:4]
    month = graph_name[4:6]
    day = graph_name[6:8]
    
    if type == 'SST':
        plt.title('SST Front Length in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Length (km)', fraction=fraction_size, pad=0.04)
    elif type == 'SSS':
        plt.title('SSS Front Length in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Length (km)', fraction=fraction_size, pad=0.04)
    elif type == 'density':
        plt.title('Density Front Length in ' + year + '-' + month  + '-' + day)
        cbar = plt.colorbar(label='Length (km)', fraction=fraction_size, pad=0.04)

    if i == 4:
        # adjust the colorbar font size
        cbar.ax.tick_params(labelsize=20)
        # adjust the colorbar label font size
        cbar.ax.yaxis.label.set_size(20)

    cbar.mappable.set_clim(108, 1090)     

    plt.savefig(output + graph_name, dpi=300)
    plt.close() 