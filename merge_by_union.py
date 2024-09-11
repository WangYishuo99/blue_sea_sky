'''
Author: Yishuo Wang
Date: 2024-07-03 14:00:28
LastEditors: Yishuo Wang
LastEditTime: 2024-07-29 15:39:45
Description: this is a function for merge by union, where if there is 1 1 occur, then it is 1, otherwise 0
'''
import numpy as np

def merge_binary(skeleton_SCS, skeleton_BHD, skeleton_KUR, skeleton_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon):

    lat_SCS_A1_indices = np.where((lat_SCS >= 18) & (lat_SCS < 21))
    lon_SCS_A1_indices = np.where((lon_SCS >= 115) & (lon_SCS < 135))

    SCS_A1 = skeleton_SCS[lat_SCS_A1_indices[0][0]:lat_SCS_A1_indices[0][-1]+1, lon_SCS_A1_indices[0][0]:lon_SCS_A1_indices[0][-1]+1]

    lat_BHD_A1_indices = np.where((lat_BHD >= 18) & (lat_BHD < 21))
    lon_BHD_A1_indices = np.where((lon_BHD >= 115) & (lon_BHD < 135))

    BHD_A1 = skeleton_BHD[lat_BHD_A1_indices[0][0]:lat_BHD_A1_indices[0][-1]+1, lon_BHD_A1_indices[0][0]:lon_BHD_A1_indices[0][-1]+1]

    lat_SCS_A2_indices = np.where((lat_SCS >= 0) & (lat_SCS < 18))
    lon_SCS_A2_indices = np.where((lon_SCS >= 135) & (lon_SCS < 140))

    SCS_A2 = skeleton_SCS[lat_SCS_A2_indices[0][0]:lat_SCS_A2_indices[0][-1]+1, lon_SCS_A2_indices[0][0]:lon_SCS_A2_indices[0][-1]+1]

    lat_STP_A2_indices = np.where((lat_STP >= 0) & (lat_STP < 18))
    lon_STP_A2_indices = np.where((lon_STP >= 135) & (lon_STP < 140))

    STP_A2 = skeleton_STP[lat_STP_A2_indices[0][0]:lat_STP_A2_indices[0][-1]+1, lon_STP_A2_indices[0][0]:lon_STP_A2_indices[0][-1]+1]

    lat_STP_A3_indices = np.where((lat_STP >= 20) & (lat_STP < 21))
    lon_STP_A3_indices = np.where((lon_STP >= 140) & (lon_STP < 180))

    STP_A3 = skeleton_STP[lat_STP_A3_indices[0][0]:lat_STP_A3_indices[0][-1]+1, lon_STP_A3_indices[0][0]:lon_STP_A3_indices[0][-1]+1]

    lat_KUR_A3_indices = np.where((lat_KUR >= 20) & (lat_KUR < 21))
    lon_KUR_A3_indices = np.where((lon_KUR >= 140) & (lon_KUR < 180))

    KUR_A3 = skeleton_KUR[lat_KUR_A3_indices[0][0]:lat_KUR_A3_indices[0][-1]+1, lon_KUR_A3_indices[0][0]:lon_KUR_A3_indices[0][-1]+1]

    lat_KUR_A4_indices = np.where((lat_KUR >= 21) & (lat_KUR < 41))
    lon_KUR_A4_indices = np.where((lon_KUR >= 135) & (lon_KUR < 140))

    KUR_A4 = skeleton_KUR[lat_KUR_A4_indices[0][0]:lat_KUR_A4_indices[0][-1]+1, lon_KUR_A4_indices[0][0]:lon_KUR_A4_indices[0][-1]+1]

    lat_BHD_A4_indices = np.where((lat_BHD >= 21) & (lat_BHD < 41))
    lon_BHD_A4_indices = np.where((lon_BHD >= 135) & (lon_BHD < 140))

    BHD_A4 = skeleton_BHD[lat_BHD_A4_indices[0][0]:lat_BHD_A4_indices[0][-1]+1, lon_BHD_A4_indices[0][0]:lon_BHD_A4_indices[0][-1]+1]

    lat_BHD_B_indices = np.where((lat_BHD >= 18) & (lat_BHD <20))
    lon_BHD_B_indices = np.where((lon_BHD >= 135) & (lon_BHD < 140))

    BHD_B = skeleton_BHD[lat_BHD_B_indices[0][0]:lat_BHD_B_indices[0][-1]+1, lon_BHD_B_indices[0][0]:lon_BHD_B_indices[0][-1]+1]

    lat_STP_B_indices = np.where((lat_STP >= 18) & (lat_STP <20))
    lon_STP_B_indices = np.where((lon_STP >= 135) & (lon_STP < 140))

    STP_B = skeleton_STP[lat_STP_B_indices[0][0]:lat_STP_B_indices[0][-1]+1, lon_STP_B_indices[0][0]:lon_STP_B_indices[0][-1]+1]

    lat_SCS_B_indices = np.where((lat_SCS >= 18) & (lat_SCS <20))
    lon_SCS_B_indices = np.where((lon_SCS >= 135) & (lon_SCS < 140))

    SCS_B = skeleton_SCS[lat_SCS_B_indices[0][0]:lat_SCS_B_indices[0][-1]+1, lon_SCS_B_indices[0][0]:lon_SCS_B_indices[0][-1]+1]

    lat_BHD_C_indices = np.where((lat_BHD >= 20) & (lat_BHD <21))
    lon_BHD_C_indices = np.where((lon_BHD >= 135) & (lon_BHD < 140))

    BHD_C = skeleton_BHD[lat_BHD_C_indices[0][0]:lat_BHD_C_indices[0][-1]+1, lon_BHD_C_indices[0][0]:lon_BHD_C_indices[0][-1]+1]

    lat_SCS_C_indices = np.where((lat_SCS >= 20) & (lat_SCS <21))
    lon_SCS_C_indices = np.where((lon_SCS >= 135) & (lon_SCS < 140))

    SCS_C = skeleton_SCS[lat_SCS_C_indices[0][0]:lat_SCS_C_indices[0][-1]+1, lon_SCS_C_indices[0][0]:lon_SCS_C_indices[0][-1]+1]

    lat_STP_C_indices = np.where((lat_STP >= 20) & (lat_STP <21))
    lon_STP_C_indices = np.where((lon_STP >= 135) & (lon_STP < 140))

    STP_C = skeleton_STP[lat_STP_C_indices[0][0]:lat_STP_C_indices[0][-1]+1, lon_STP_C_indices[0][0]:lon_STP_C_indices[0][-1]+1]

    lat_KUR_C_indices = np.where((lat_KUR >= 20) & (lat_KUR <21))
    lon_KUR_C_indices = np.where((lon_KUR >= 135) & (lon_KUR < 140))

    KUR_C = skeleton_KUR[lat_KUR_C_indices[0][0]:lat_KUR_C_indices[0][-1]+1, lon_KUR_C_indices[0][0]:lon_KUR_C_indices[0][-1]+1]

    # extract the lat and lons of every overlapped regions
    lat_A1 = np.array(lat_SCS[lat_SCS_A1_indices])
    lon_A1 = np.array(lon_SCS[lon_SCS_A1_indices])
    lat_A2 = np.array(lat_SCS[lat_SCS_A2_indices])
    lon_A2 = np.array(lon_SCS[lon_SCS_A2_indices])
    lat_A3 = np.array(lat_STP[lat_STP_A3_indices])
    lon_A3 = np.array(lon_STP[lon_STP_A3_indices])
    lat_A4 = np.array(lat_KUR[lat_KUR_A4_indices])
    lon_A4 = np.array(lon_KUR[lon_KUR_A4_indices])
    lat_B = np.array(lat_BHD[lat_BHD_B_indices])
    lon_B = np.array(lon_BHD[lon_BHD_B_indices])
    lat_C = np.array(lat_BHD[lat_BHD_C_indices])
    lon_C = np.array(lon_BHD[lon_BHD_C_indices])

    # rewrite the A1, A2, A3, A4, B, C, if there is 1 in union then 1, else 0, nan is nan
    rows, cols = SCS_A1.shape
    A1 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if SCS_A1[i][j] == 1 or BHD_A1[i][j] == 1:
                A1[i][j] = 1
            elif np.isnan(SCS_A1[i][j]):
                A1[i][j] = np.nan

    rows, cols = SCS_A2.shape
    A2 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if SCS_A2[i][j] == 1 or STP_A2[i][j] == 1:
                A2[i][j] = 1
            elif np.isnan(SCS_A2[i][j]):
                A2[i][j] = np.nan

    rows, cols = STP_A3.shape
    A3 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if STP_A3[i][j] == 1 or KUR_A3[i][j] == 1:
                A3[i][j] = 1
            elif np.isnan(STP_A3[i][j]):
                A3[i][j] = np.nan

    rows, cols = KUR_A4.shape
    A4 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if KUR_A4[i][j] == 1 or BHD_A4[i][j] == 1:
                A4[i][j] = 1
            elif np.isnan(KUR_A4[i][j]):
                A4[i][j] = np.nan

    rows, cols = SCS_B.shape
    B = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if SCS_B[i][j] == 1 or BHD_B[i][j] == 1 or STP_B[i][j] == 1:
                B[i][j] = 1
            elif np.isnan(SCS_B[i][j]):
                B[i][j] = np.nan

    rows, cols = SCS_C.shape
    C = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if SCS_C[i][j] == 1 or BHD_C[i][j] == 1 or STP_C[i][j] == 1 or KUR_C[i][j] == 1:
                C[i][j] = 1
            elif np.isnan(SCS_C[i][j]):
                C[i][j] = np.nan

    # Get the indices where lon is between 100 and 180
    lon_all_indices = np.where((lon >= 100) & (lon < 180))

    # Get the indices where lat is between 0 and 48
    lat_all_indices = np.where((lat >= 0) & (lat < 48))

    lon_all = np.array(lon[lon_all_indices])

    lat_all = np.array(lat[lat_all_indices])

    # lat_all = np.flipud(lat_all)

    # connect the regions
    connected_front_matrix = np.zeros((lat_all.shape[0], lon_all.shape[0]))

    rows, cols = connected_front_matrix.shape
    for i in range(rows):
        for j in range(cols):
            if lat_all[i]>= 41 and lat_all[i]<48:
                if lon_all[j]<135:
                    connected_front_matrix[i][j] = np.nan
                else:
                    # find the indices of lat_all[i] and lon_all[j] in lat_KUR and lon_KUR
                    lat_KUR_indices = np.where(lat_KUR == lat_all[i])[0][0]
                    lon_KUR_indices = np.where(lon_KUR == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_KUR[lat_KUR_indices][lon_KUR_indices]
            elif lat_all[i]>= 21 and lat_all[i]<41:
                if lon_all[j]<115:
                    connected_front_matrix[i][j] = np.nan
                elif lon_all[j]>= 115 and lon_all[j]<135:
                    lat_BHD_indices = np.where(lat_BHD == lat_all[i])[0][0]
                    lon_BHD_indices = np.where(lon_BHD == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_BHD[lat_BHD_indices][lon_BHD_indices]
                elif lon_all[j]>= 135 and lon_all[j]<140:
                    lat_A4_indices = np.where(lat_A4 == lat_all[i])[0][0]
                    lon_A4_indices = np.where(lon_A4 == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = A4[lat_A4_indices][lon_A4_indices]
                else:
                    lat_KUR_indices = np.where(lat_KUR == lat_all[i])[0][0]
                    lon_KUR_indices = np.where(lon_KUR == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_KUR[lat_KUR_indices][lon_KUR_indices]
            elif lat_all[i]>= 20 and lat_all[i]<21:
                if lon_all[j]<115:
                    lat_SCS_indices = np.where(lat_SCS == lat_all[i])[0][0]
                    lon_SCS_indices = np.where(lon_SCS == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_SCS[lat_SCS_indices][lon_SCS_indices]
                elif lon_all[j]>=115 and lon_all[j]<135:
                    lat_A1_indices = np.where(lat_A1 == lat_all[i])[0][0]
                    lon_A1_indices = np.where(lon_A1 == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  A1[lat_A1_indices][lon_A1_indices]
                elif lon_all[j]>=135 and lon_all[j]<140:
                    lat_C_indices = np.where(lat_C == lat_all[i])[0][0]
                    lon_C_indices = np.where(lon_C == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  C[lat_C_indices][lon_C_indices]
                else:
                    lat_A3_indices = np.where(lat_A3 == lat_all[i])[0][0]
                    lon_A3_indices = np.where(lon_A3 == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  A3[lat_A3_indices][lon_A3_indices]
            elif lat_all[i]>=18 and lat_all[i]<20:
                if lon_all[j]<115:
                    lat_SCS_indices = np.where(lat_SCS == lat_all[i])[0][0]
                    lon_SCS_indices = np.where(lon_SCS == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_SCS[lat_SCS_indices][lon_SCS_indices]
                elif lon_all[j]>=115 and lon_all[j]<135:
                    lat_A1_indices = np.where(lat_A1 == lat_all[i])[0][0]
                    lon_A1_indices = np.where(lon_A1 == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  A1[lat_A1_indices][lon_A1_indices]
                elif lon_all[j]>=135 and lon_all[j]<140:
                    lat_B_indices = np.where(lat_B == lat_all[i])[0][0]
                    lon_B_indices = np.where(lon_B == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  B[lat_B_indices][lon_B_indices]
                else:
                    lat_STP_indices = np.where(lat_STP == lat_all[i])[0][0]
                    lon_STP_indices = np.where(lon_STP == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  skeleton_STP[lat_STP_indices][lon_STP_indices]
            else:
                if lon_all[j]<135:
                    lat_SCS_indices = np.where(lat_SCS == lat_all[i])[0][0]
                    lon_SCS_indices = np.where(lon_SCS == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_SCS[lat_SCS_indices][lon_SCS_indices]
                elif lon_all[j]>= 135 and lon_all[j]<140:
                    lat_A2_indices = np.where(lat_A2 == lat_all[i])[0][0]
                    lon_A2_indices = np.where(lon_A2 == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = A2[lat_A2_indices][lon_A2_indices]
                else:
                    lat_STP_indices = np.where(lat_STP == lat_all[i])[0][0]
                    lon_STP_indices = np.where(lon_STP == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  skeleton_STP[lat_STP_indices][lon_STP_indices]

    return connected_front_matrix

def merge_real_number(skeleton_SCS, skeleton_BHD, skeleton_KUR, skeleton_STP, lat_SCS, lon_SCS, lat_BHD, lon_BHD, lat_KUR, lon_KUR, lat_STP, lon_STP, lat, lon):

    lat_SCS_A1_indices = np.where((lat_SCS >= 18) & (lat_SCS < 21))
    lon_SCS_A1_indices = np.where((lon_SCS >= 115) & (lon_SCS < 135))

    SCS_A1 = skeleton_SCS[lat_SCS_A1_indices[0][0]:lat_SCS_A1_indices[0][-1]+1, lon_SCS_A1_indices[0][0]:lon_SCS_A1_indices[0][-1]+1]

    lat_BHD_A1_indices = np.where((lat_BHD >= 18) & (lat_BHD < 21))
    lon_BHD_A1_indices = np.where((lon_BHD >= 115) & (lon_BHD < 135))

    BHD_A1 = skeleton_BHD[lat_BHD_A1_indices[0][0]:lat_BHD_A1_indices[0][-1]+1, lon_BHD_A1_indices[0][0]:lon_BHD_A1_indices[0][-1]+1]

    lat_SCS_A2_indices = np.where((lat_SCS >= 0) & (lat_SCS < 18))
    lon_SCS_A2_indices = np.where((lon_SCS >= 135) & (lon_SCS < 140))

    SCS_A2 = skeleton_SCS[lat_SCS_A2_indices[0][0]:lat_SCS_A2_indices[0][-1]+1, lon_SCS_A2_indices[0][0]:lon_SCS_A2_indices[0][-1]+1]

    lat_STP_A2_indices = np.where((lat_STP >= 0) & (lat_STP < 18))
    lon_STP_A2_indices = np.where((lon_STP >= 135) & (lon_STP < 140))

    STP_A2 = skeleton_STP[lat_STP_A2_indices[0][0]:lat_STP_A2_indices[0][-1]+1, lon_STP_A2_indices[0][0]:lon_STP_A2_indices[0][-1]+1]

    lat_STP_A3_indices = np.where((lat_STP >= 20) & (lat_STP < 21))
    lon_STP_A3_indices = np.where((lon_STP >= 140) & (lon_STP < 180))

    STP_A3 = skeleton_STP[lat_STP_A3_indices[0][0]:lat_STP_A3_indices[0][-1]+1, lon_STP_A3_indices[0][0]:lon_STP_A3_indices[0][-1]+1]

    lat_KUR_A3_indices = np.where((lat_KUR >= 20) & (lat_KUR < 21))
    lon_KUR_A3_indices = np.where((lon_KUR >= 140) & (lon_KUR < 180))

    KUR_A3 = skeleton_KUR[lat_KUR_A3_indices[0][0]:lat_KUR_A3_indices[0][-1]+1, lon_KUR_A3_indices[0][0]:lon_KUR_A3_indices[0][-1]+1]

    lat_KUR_A4_indices = np.where((lat_KUR >= 21) & (lat_KUR < 41))
    lon_KUR_A4_indices = np.where((lon_KUR >= 135) & (lon_KUR < 140))

    KUR_A4 = skeleton_KUR[lat_KUR_A4_indices[0][0]:lat_KUR_A4_indices[0][-1]+1, lon_KUR_A4_indices[0][0]:lon_KUR_A4_indices[0][-1]+1]

    lat_BHD_A4_indices = np.where((lat_BHD >= 21) & (lat_BHD < 41))
    lon_BHD_A4_indices = np.where((lon_BHD >= 135) & (lon_BHD < 140))

    BHD_A4 = skeleton_BHD[lat_BHD_A4_indices[0][0]:lat_BHD_A4_indices[0][-1]+1, lon_BHD_A4_indices[0][0]:lon_BHD_A4_indices[0][-1]+1]

    lat_BHD_B_indices = np.where((lat_BHD >= 18) & (lat_BHD <20))
    lon_BHD_B_indices = np.where((lon_BHD >= 135) & (lon_BHD < 140))

    BHD_B = skeleton_BHD[lat_BHD_B_indices[0][0]:lat_BHD_B_indices[0][-1]+1, lon_BHD_B_indices[0][0]:lon_BHD_B_indices[0][-1]+1]

    lat_STP_B_indices = np.where((lat_STP >= 18) & (lat_STP <20))
    lon_STP_B_indices = np.where((lon_STP >= 135) & (lon_STP < 140))

    STP_B = skeleton_STP[lat_STP_B_indices[0][0]:lat_STP_B_indices[0][-1]+1, lon_STP_B_indices[0][0]:lon_STP_B_indices[0][-1]+1]

    lat_SCS_B_indices = np.where((lat_SCS >= 18) & (lat_SCS <20))
    lon_SCS_B_indices = np.where((lon_SCS >= 135) & (lon_SCS < 140))

    SCS_B = skeleton_SCS[lat_SCS_B_indices[0][0]:lat_SCS_B_indices[0][-1]+1, lon_SCS_B_indices[0][0]:lon_SCS_B_indices[0][-1]+1]

    lat_BHD_C_indices = np.where((lat_BHD >= 20) & (lat_BHD <21))
    lon_BHD_C_indices = np.where((lon_BHD >= 135) & (lon_BHD < 140))

    BHD_C = skeleton_BHD[lat_BHD_C_indices[0][0]:lat_BHD_C_indices[0][-1]+1, lon_BHD_C_indices[0][0]:lon_BHD_C_indices[0][-1]+1]

    lat_SCS_C_indices = np.where((lat_SCS >= 20) & (lat_SCS <21))
    lon_SCS_C_indices = np.where((lon_SCS >= 135) & (lon_SCS < 140))

    SCS_C = skeleton_SCS[lat_SCS_C_indices[0][0]:lat_SCS_C_indices[0][-1]+1, lon_SCS_C_indices[0][0]:lon_SCS_C_indices[0][-1]+1]

    lat_STP_C_indices = np.where((lat_STP >= 20) & (lat_STP <21))
    lon_STP_C_indices = np.where((lon_STP >= 135) & (lon_STP < 140))

    STP_C = skeleton_STP[lat_STP_C_indices[0][0]:lat_STP_C_indices[0][-1]+1, lon_STP_C_indices[0][0]:lon_STP_C_indices[0][-1]+1]

    lat_KUR_C_indices = np.where((lat_KUR >= 20) & (lat_KUR <21))
    lon_KUR_C_indices = np.where((lon_KUR >= 135) & (lon_KUR < 140))

    KUR_C = skeleton_KUR[lat_KUR_C_indices[0][0]:lat_KUR_C_indices[0][-1]+1, lon_KUR_C_indices[0][0]:lon_KUR_C_indices[0][-1]+1]

    # extract the lat and lons of every overlapped regions
    lat_A1 = np.array(lat_SCS[lat_SCS_A1_indices])
    lon_A1 = np.array(lon_SCS[lon_SCS_A1_indices])
    lat_A2 = np.array(lat_SCS[lat_SCS_A2_indices])
    lon_A2 = np.array(lon_SCS[lon_SCS_A2_indices])
    lat_A3 = np.array(lat_STP[lat_STP_A3_indices])
    lon_A3 = np.array(lon_STP[lon_STP_A3_indices])
    lat_A4 = np.array(lat_KUR[lat_KUR_A4_indices])
    lon_A4 = np.array(lon_KUR[lon_KUR_A4_indices])
    lat_B = np.array(lat_BHD[lat_BHD_B_indices])
    lon_B = np.array(lon_BHD[lon_BHD_B_indices])
    lat_C = np.array(lat_BHD[lat_BHD_C_indices])
    lon_C = np.array(lon_BHD[lon_BHD_C_indices])

    # rewrite the A1, A2, A3, A4, B, C, if there is 1 in union then 1, else 0, nan is nan
    rows, cols = SCS_A1.shape
    A1 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
                A1[i][j] = SCS_A1[i][j]

    rows, cols = SCS_A2.shape
    A2 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            A2[i][j] = SCS_A2[i][j]

    rows, cols = STP_A3.shape
    A3 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            A3[i][j] = STP_A3[i][j]

    rows, cols = KUR_A4.shape
    A4 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            A4[i][j] = KUR_A4[i][j]

    rows, cols = SCS_B.shape
    B = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            B[i][j] = SCS_B[i][j]
 
    rows, cols = SCS_C.shape
    C = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            C[i][j] =  SCS_C[i][j]

    # Get the indices where lon is between 100 and 180
    lon_all_indices = np.where((lon >= 100) & (lon < 180))

    # Get the indices where lat is between 0 and 48
    lat_all_indices = np.where((lat >= 0) & (lat < 48))

    lon_all = np.array(lon[lon_all_indices])

    lat_all = np.array(lat[lat_all_indices])

    # lat_all = np.flipud(lat_all)

    # connect the regions
    connected_front_matrix = np.zeros((lat_all.shape[0], lon_all.shape[0]))

    rows, cols = connected_front_matrix.shape
    for i in range(rows):
        for j in range(cols):
            if lat_all[i]>= 41 and lat_all[i]<48:
                if lon_all[j]<135:
                    connected_front_matrix[i][j] = np.nan
                else:
                    # find the indices of lat_all[i] and lon_all[j] in lat_KUR and lon_KUR
                    lat_KUR_indices = np.where(lat_KUR == lat_all[i])[0][0]
                    lon_KUR_indices = np.where(lon_KUR == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_KUR[lat_KUR_indices][lon_KUR_indices]
            elif lat_all[i]>= 21 and lat_all[i]<41:
                if lon_all[j]<115:
                    connected_front_matrix[i][j] = np.nan
                elif lon_all[j]>= 115 and lon_all[j]<135:
                    lat_BHD_indices = np.where(lat_BHD == lat_all[i])[0][0]
                    lon_BHD_indices = np.where(lon_BHD == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_BHD[lat_BHD_indices][lon_BHD_indices]
                elif lon_all[j]>= 135 and lon_all[j]<140:
                    lat_A4_indices = np.where(lat_A4 == lat_all[i])[0][0]
                    lon_A4_indices = np.where(lon_A4 == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = A4[lat_A4_indices][lon_A4_indices]
                else:
                    lat_KUR_indices = np.where(lat_KUR == lat_all[i])[0][0]
                    lon_KUR_indices = np.where(lon_KUR == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_KUR[lat_KUR_indices][lon_KUR_indices]
            elif lat_all[i]>= 20 and lat_all[i]<21:
                if lon_all[j]<115:
                    lat_SCS_indices = np.where(lat_SCS == lat_all[i])[0][0]
                    lon_SCS_indices = np.where(lon_SCS == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_SCS[lat_SCS_indices][lon_SCS_indices]
                elif lon_all[j]>=115 and lon_all[j]<135:
                    lat_A1_indices = np.where(lat_A1 == lat_all[i])[0][0]
                    lon_A1_indices = np.where(lon_A1 == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  A1[lat_A1_indices][lon_A1_indices]
                elif lon_all[j]>=135 and lon_all[j]<140:
                    lat_C_indices = np.where(lat_C == lat_all[i])[0][0]
                    lon_C_indices = np.where(lon_C == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  C[lat_C_indices][lon_C_indices]
                else:
                    lat_A3_indices = np.where(lat_A3 == lat_all[i])[0][0]
                    lon_A3_indices = np.where(lon_A3 == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  A3[lat_A3_indices][lon_A3_indices]
            elif lat_all[i]>=18 and lat_all[i]<20:
                if lon_all[j]<115:
                    lat_SCS_indices = np.where(lat_SCS == lat_all[i])[0][0]
                    lon_SCS_indices = np.where(lon_SCS == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_SCS[lat_SCS_indices][lon_SCS_indices]
                elif lon_all[j]>=115 and lon_all[j]<135:
                    lat_A1_indices = np.where(lat_A1 == lat_all[i])[0][0]
                    lon_A1_indices = np.where(lon_A1 == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  A1[lat_A1_indices][lon_A1_indices]
                elif lon_all[j]>=135 and lon_all[j]<140:
                    lat_B_indices = np.where(lat_B == lat_all[i])[0][0]
                    lon_B_indices = np.where(lon_B == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  B[lat_B_indices][lon_B_indices]
                else:
                    lat_STP_indices = np.where(lat_STP == lat_all[i])[0][0]
                    lon_STP_indices = np.where(lon_STP == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  skeleton_STP[lat_STP_indices][lon_STP_indices]
            else:
                if lon_all[j]<135:
                    lat_SCS_indices = np.where(lat_SCS == lat_all[i])[0][0]
                    lon_SCS_indices = np.where(lon_SCS == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = skeleton_SCS[lat_SCS_indices][lon_SCS_indices]
                elif lon_all[j]>= 135 and lon_all[j]<140:
                    lat_A2_indices = np.where(lat_A2 == lat_all[i])[0][0]
                    lon_A2_indices = np.where(lon_A2 == lon_all[j])[0][0]
                    connected_front_matrix[i][j] = A2[lat_A2_indices][lon_A2_indices]
                else:
                    lat_STP_indices = np.where(lat_STP == lat_all[i])[0][0]
                    lon_STP_indices = np.where(lon_STP == lon_all[j])[0][0]
                    connected_front_matrix[i][j] =  skeleton_STP[lat_STP_indices][lon_STP_indices]

    return connected_front_matrix