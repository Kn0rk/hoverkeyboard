
import numpy as np

def simple_staggered_grid():
    points = []
    x_space = np.linspace(0.05,0.95, 12)
    x_space = [x+0.3*x*x*x for x in x_space ]

    y_space = np.linspace(0.05,0.95, 6) 
    # points = points.tolist()
    offset = False
    for y in y_space:
        offset = not offset
        for x in x_space:
            if offset:
                points.append(x + 0.05)
            else:
                points.append(x)
            points.append(y)





    # Include Points outside of the boundary box
    points.extend([-5,-5, 5,-5, 5,5, -5,5])
    return points