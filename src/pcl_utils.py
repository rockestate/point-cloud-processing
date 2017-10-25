from scipy.spatial.kdtree import KDTree
import numpy as np

# Adapted from https://stackoverflow.com/a/27116281
def locally_extreme_points(coords, data, radius, smoothing_radius = None, min_neighbourhood_size = -1, lookfor = 'max', p_norm = 2):
    '''
    Find local maxima of points in a pointcloud.  Ties result in both points passing through the filter.

    Not to be used for high-dimensional data.  It will be slow.

    coords: A shape (n_points, n_dims) array of point locations
    data: A shape (n_points, ) vector of point values
    radius: The (scalar) size of the neighbourhood in which to search.
    min_neighbourhood_size: Extrema whose neighbourhood has less than min_neighbourhood_size points are discarded
    lookfor: Either 'max', or 'min', depending on whether you want local maxima or minima
    p_norm: The p-norm to use for measuring distance (e.g. 1=Manhattan, 2=Euclidian)

    returns
        filtered_coords: The coordinates of locally extreme points
        filtered_data: The values of these points
    '''
    assert coords.shape[0] == data.shape[0], 'You must have one coordinate per data point'
    extreme_fcn = {'min': np.min, 'max': np.max}[lookfor]
    kdtree = KDTree(coords)
    if smoothing_radius is not None:
        smoothing_neighbours = kdtree.query_ball_tree(kdtree, r=smoothing_radius, p = p_norm)
        smooth_data = np.array([np.mean(data[n]) for n in smoothing_neighbours])
    else:
        smooth_data = data
    neighbours = kdtree.query_ball_tree(kdtree, r=radius, p = p_norm)
    i_am_extreme = [(np.nonzero(np.equal(n,i))[0][0]==np.argmax(smooth_data[n])) & (len(n) > min_neighbourhood_size) for i, n in enumerate(neighbours)]
    extrema, = np.nonzero(i_am_extreme)  # This line just saves time on indexing
    return coords[extrema], data[extrema]

