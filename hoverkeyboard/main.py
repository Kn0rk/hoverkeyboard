from collections import namedtuple
import logging
import tkinter
import numpy as np
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
from hoverkeyboard.action import Action
from hoverkeyboard.button import PolygonButton, load_from_file, recalculate_polygon, save_to_file


from hoverkeyboard.make_grid import simple_staggered_grid


# 

logging.basicConfig(level=logging.DEBUG)
root = tkinter.Tk()
root.config(cursor="none")
root.attributes("-topmost", True)
#root.attributes("-type", "splash")
#root.overrideredirect(True)

root.bind("<Control-s>", lambda event: save_to_file(buttons))
canvas = tkinter.Canvas(root,takefocus=0)
canvas.pack(fill=tkinter.BOTH, expand=True)

# canvas.pack()

# screen_with = root.winfo_width()
# screen_height = root.winfo_height() 
# screen_with = 1440
# screen_height = 900

# print(screen_with, screen_height)

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tkinter.Canvas.create_circle = _create_circle

points = simple_staggered_grid()

# points[::2] = [x * screen_with for x in points[::2]]
# points[1::2] = [x * screen_height for x in points[1::2]]

# for point in range(0, len(points),2):
#     # print(points[point], points[point+1])
    # canvas.create_circle(points[point], points[point+1], 10, fill="red")

buttons = load_from_file(root, canvas)
saved_points = False

def redraw_canvas(event):
    width = root.winfo_width()
    height = root.winfo_height()
    print(width, height)
    canvas.config(width=width-2, height=height-2)
    canvas.delete('all')
    # points = simple_staggered_grid()
    # global buttons
    # buttons = []
    # for point in range(0, len(points),2):
    #     buttons.append(PolygonButton(canvas, [],[points[point], points[point+1]], Action("x")))
    recalculate_polygon(root,buttons)
    for button in buttons:
        button.draw()
    if not saved_points:
        save_to_file(buttons)

    
    





    

tag = canvas.create_text(10, 10, text="", anchor="nw")  

canvas.bind("<Configure>", redraw_canvas)





root.mainloop()