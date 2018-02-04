import numpy as np

def local_max(coords, radius, density_threshold=0):
    '''
    Find local maxima of points in a pointcloud.
    '''
    max_box = coords.copy()
    for i in range(2):
        max_box['X{}'.format(i)] = ((coords['X']/radius + i) /2).astype(int)*2
        max_box['Y{}'.format(i)] = ((coords['Y']/radius + i) /2).astype(int)*2
    max_box['X_'] = (coords['X']/radius).astype(int)
    max_box['Y_'] = (coords['Y']/radius).astype(int)
    for i in range(2):
        for j in range(2):
            max_box[str(i)+str(j)] = max_box.groupby(['X{}'.format(i), 'Y{}'.format(j)])['Z'].transform(np.max)
    density = max_box.groupby(['X_','Y_'])['Z'].transform(len)
    is_max = (max_box['00'] == max_box['10']) & (max_box['10'] == max_box['01']) & (max_box['01'] == max_box['11']) & (max_box['11'] == coords['Z'])
    return coords[is_max & (density >= (density_threshold))]