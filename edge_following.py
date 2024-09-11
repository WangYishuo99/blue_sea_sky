'''
Author: Yishuo Wang
Date: 2024-03-12 16:39:59
LastEditors: Yishuo Wang
LastEditTime: 2024-04-17 15:01:02
FilePath: /传统方法识别/edge_following.py
Description: an edge following algorithm to merge the edges of the SST fronts, using deep first search to find the connected components

Copyright (c) 2024 by Yishuo Wang, All Rights Reserved. 
'''
import numpy as np

# Define the DFS function, using deep first search to find the connected components
def dfs(x, y, visited, current_list, marked_matrix, direction):
    # Define the 8 directions of neighbours
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    # Mark the current point as visited
    visited[x][y] = True
    current_list.append((x, y))
    
    # Check all 8 neighbours
    # set a pointer to record points on standby
    # the max difference of the direction
    pointers = []
    direction_difference = []
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        
        # Check if the neighbour is within the matrix bounds and is a 1
        # Check if the neighbour has not been visited and record the angle difference
        if 0 <= nx < len(marked_matrix) and 0 <= ny < len(marked_matrix[0]) and marked_matrix[nx][ny] == 1 and not visited[nx][ny]:
            pointers.append(i)
            direction_difference.append(abs(direction[x][y] - direction[nx][ny]))
    
    # if the pointers is empty, return
    if not pointers:
        return current_list
    # if the pointers is not empty, find the minimum difference position
    # and go to the point
    else:
        min_index = direction_difference.index(min(direction_difference))
        nx, ny = x + dx[pointers[min_index]], y + dy[pointers[min_index]]
        return dfs(nx, ny, visited, current_list, marked_matrix, direction)

# find the fronts and save them in a list, the list is nested, each element is a list of points of a front
def follow(marked_matrix, direction):
    # Initialize the visited matrix
    visited = [[False]*len(marked_matrix[0]) for _ in range(len(marked_matrix))]
    
    nested_list = []
    
    # Scan the marked_matrix
    for i in range(len(marked_matrix)):
        for j in range(len(marked_matrix[0])):
            # If the point is 1 and has not been visited, start a DFS from it
            if marked_matrix[i][j] == 1 and not visited[i][j]:
                current_list = []
                current_list = dfs(i, j, visited, current_list, marked_matrix, direction)
                nested_list.append(current_list)
    
    return nested_list