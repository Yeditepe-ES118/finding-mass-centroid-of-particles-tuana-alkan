import numpy as np
# remove this line after


def centroid(p1x, p1y, p2x, p2y, p3x, p3y, m1, m2, m3):
    
    positions = np.array([[p1x, p2x, p3x],[p1y, p2y, p3y]])
    masses = np.array([m1, m2, m3])
    
    cx = np.sum(positions[0,:]*masses) / np.sum(masses)
    cy = np.sum(positions[1,:]*masses) / np.sum(masses)
    tot_mass = np.sum(masses)
    
    # remove these Lines after
   
    
    return tot_mass, cx, cy

result = centroid(1,1,2,1,1.5,2,1.0008,1.0008,16)

