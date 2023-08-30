
import numpy as np

from hoverkeyboard.action import Action
from hoverkeyboard.button import PolygonButton, save_to_file
from hoverkeyboard.keyboard import Keyboard
from hoverkeyboard.saver import save_keyboard

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


    # Include Points outside of the boundary boxt to make sure the delaunay triangulation works
    points.extend([-5,-5, 5,-5, 5,5, -5,5])
    return points

def custom_grid():
    x_space = [0.5,0.55,0.6,0.66,0.72,0.81,0.95]
    x_space.extend([1-x for x in x_space[1:]])
    x_space.sort()
    x_space_staggered = [(x_space[i]+x_space[i+1])/2 for i in range(len(x_space)-1)]
    y_space = [0.15,0.3,0.45,0.6,0.75,0.9]

    print(x_space)
    print(x_space_staggered)
    print(y_space)

    points = []
    for index,y in enumerate(y_space):
        if index % 2 == 0:
            for x in x_space:
                points.append(x)
                points.append(y)
        else:
            for x in x_space_staggered:
                points.append(x)
                points.append(y)

    return points


def save_points(centers,path):
    keyboard=Keyboard(centers,["base"])
    save_keyboard(keyboard,centers,path)

if __name__ == "__main__":
    points = custom_grid()
    centers = [[points[index],points[index+1]] for index in range(0,len(points),2)]
    save_points(centers,"custom_grid.board")
    exit()
    action = Action("xx")
    buttons = []
    for index in range(0,len(points),2):
        buttons.append(PolygonButton(None,[],
                      [points[index],points[index+1]                                                                          ]
                       ,action))
    
    save_to_file(buttons,"custom_grid.json") 
