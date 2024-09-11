'''
Author: Yishuo Wang
Date: 2024-05-13 19:31:43
LastEditors: Yishuo Wang
LastEditTime: 2024-05-15 14:41:07
FilePath: /digital_image_processing/edge_pruning.py
Description: skeleton pruning using discrete skeleton evolution methond (Bai, 2007)

Copyright (c) 2024 by Yishuo Wang, All Rights Reserved. 
'''

from skimage import morphology
import numpy as np
import sknw, math
from skimage.draw import line

def flatten(l):
    return [item for sublist in l for item in sublist]

def recnstrc_by_disk(pts,dist_tr,reconstruct):
    """
    Attempt to reconstruct the binary image from the skeleton using distance transform
    
    Arguments:
    pts (list) - branch points
    dist_tr (nd) - Distance transform matrix
    reconstruct (nd) - reconstructed image only on branch
    
    Return:
    reconstruct (nd) - reconstructed image
    """
    reconstruct = reconstruct * 1
    for pt in pts:
        r, c = pt
        radius = math.ceil(dist_tr[r,c])
        stel = morphology.disk(radius)
        if r - radius >= 0 and r + radius + 1 <= reconstruct.shape[0] and c - radius >= 0 and c + radius + 1 <= reconstruct.shape[1]:
            reconstruct[r-radius:r+radius+1,c-radius:c+radius+1] += stel

    return reconstruct

def get_weight(recn,branch):
    """
    The weights are calculated using reconstruction pixel loss.
    i.e. the number of pixels loss when comparing reconstruction and original image
    """
    w = 0
    reconstruction = np.reshape(recn,-1)
    branch_image = np.reshape(branch,-1)
    
    for i in range(recn.shape[0]*recn.shape[1]):
        # Given a pixel in the reconstruction, if the branch gives the reconstruction pixel, then add its weight.
        # If reconstruction pixel > branch image then it means other branches have an effect on the pixel.
        # Therefore, the branch that provides to the reconstruction pixel obtains a higher weight.
        w += (reconstruction[i] > 0) ^ ((reconstruction[i] - branch_image[i]) > 0)
    
    return w


def _remove_branch_by_DSE(G, recn, dist, max_px_weight, checked_terminal=set()):
    deg = dict(G.degree())
    terminal_points = [i for i, d in deg.items() if d == 1]
    edges = list(G.edges())
    for s, e in edges:
        branch_recn = np.zeros_like(recn, dtype=np.int32)
        if s == e:
            G.remove_edge(s, e)
            continue
        
        pts = flatten([[v] for v in G[s][e].values()])[0]['pts']
        branch_recn = recnstrc_by_disk(pts,dist,branch_recn)
        weight = get_weight(recn, branch_recn)

        if s in terminal_points:
            checked_terminal.add(s)
            if weight < max_px_weight:
                G.remove_node(s)
                recn = recn - branch_recn
        if e in terminal_points:
            checked_terminal.add(e)
            if weight < max_px_weight:
                G.remove_node(e)
                recn = recn - branch_recn

    return G, recn

def _remove_mid_node(G):
    start_index = 0
    while True:
        nodes = [x for x in G.nodes() if G.degree(x) == 2]
        if len(nodes) == start_index:
            break
        i = nodes[start_index]
        connected_nodes = list(G[i])
        # assert len(nbs)==2, 'degree not match'
        if len(connected_nodes) != 2:
            start_index = start_index + 1
            continue

        edge1 = G[i][connected_nodes[0]][0]
        edge2 = G[i][connected_nodes[1]][0]

        s1, e1 = edge1['pts'][0], edge1['pts'][-1]
        s2, e2 = edge2['pts'][0], edge2['pts'][-1]
        dist = np.array(list(map(np.linalg.norm, [s1-s2, e1-e2, s1-e2, s2-e1])))
        if dist.argmin() == 0:
            line = np.concatenate([edge1['pts'][::-1], [G.nodes[i]['o'].astype(np.int32)], edge2['pts']], axis=0)
        elif dist.argmin() == 1:
            line = np.concatenate([edge1['pts'], [G.nodes[i]['o'].astype(np.int32)], edge2['pts'][::-1]], axis=0)
        elif dist.argmin() == 2:
            line = np.concatenate([edge2['pts'], [G.nodes[i]['o'].astype(np.int32)], edge1['pts']], axis=0)
        elif dist.argmin() == 3:
            line = np.concatenate([edge1['pts'], [G.nodes[i]['o'].astype(np.int32)], edge2['pts']], axis=0)

        G.add_edge(connected_nodes[0], connected_nodes[1], weight=edge1['weight']+edge2['weight'], pts=line)
        G.remove_node(i)
    return G

def skel_pruning_DSE(skel, dist, min_area_px=100, return_graph=False):
    """Skeleton pruning using dse
    
    Arguments:
        skel {ndarray} -- skeleton obtained from skeletonization algorithm
        dist {ndarray} -- distance transfrom map
    
    Keyword Arguments:
        min_area_px {int} -- branch reconstruction weights, measured by pixel area. Branch reconstruction weights smaller than this threshold will be pruned. (default: {100})
        return_graph {bool} -- return graph

    Returns:
        ndarray -- pruned skeleton map
    """
    graph = sknw.build_sknw(skel, multi=True)
    dist = dist.astype(np.int32)
    graph = _remove_mid_node(graph)
    edges = list(set(graph.edges()))
    pts = []
    for s, e in edges:
        temp_pts = flatten([[v] for v in graph[s][e].values()])[0]['pts']
        pts.extend(temp_pts)

    recnstrc = np.zeros_like(dist, dtype=np.int32)
    recnstrc = recnstrc_by_disk(np.array(pts, dtype=np.int32), dist, recnstrc) 
    num_nodes = len(graph.nodes())
    checked_terminal = set()
    while True:
        # cannot combine with other pruning method because the reconstruction map is not updated in other approach
        graph, recnstrc = _remove_branch_by_DSE(graph, recnstrc, dist, min_area_px, checked_terminal=checked_terminal)
        if len(graph.nodes()) == num_nodes:
            break
        graph = _remove_mid_node(graph)
        num_nodes = len(graph.nodes())
    if return_graph:
        return graph2im(graph, skel.shape), graph
    else:
        return graph2im(graph, skel.shape)      

def graph2im(graph, shape):
    mask = np.zeros(shape, dtype=bool)
    for s,e in graph.edges():
        vals = flatten([[v] for v in graph[s][e].values()])
        for val in vals:
            coords = val.get('pts')
            coords_1 = np.roll(coords, -1, axis=0)
            for i in range(len(coords)-1):
                rr, cc = line(*coords[i], *coords_1[i])
                mask[rr, cc] = True
            mask[tuple(graph.nodes[s]['pts'].T.tolist())] = True
            mask[tuple(graph.nodes[e]['pts'].T.tolist())] = True
    return mask
