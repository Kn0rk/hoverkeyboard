from collections import namedtuple
import logging
import tkinter
import numpy as np
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
from hoverkeyboard.action import Action
from hoverkeyboard.button import PolygonButton, buttons_from_centers, load_from_file, recalculate_polygon, save_to_file


from hoverkeyboard.make_grid import simple_staggered_grid
from hoverkeyboard.parser import parse

logging.basicConfig(level=logging.DEBUG)
root = tkinter.Tk()
root.config(cursor="none")
root.attributes("-topmost", True)
canvas = tkinter.Canvas(root,takefocus=0)
canvas.pack(fill=tkinter.BOTH, expand=True)

with open("custom_grid.board","r") as f:
    data = f.read()
keyboard,centers=parse(data)
buttons=buttons_from_centers(centers,keyboard,canvas)

def redraw_canvas(event):
    width = root.winfo_width()
    height = root.winfo_height()
    print(width, height)
    canvas.config(width=width-2, height=height-2)
    canvas.delete('all')

    recalculate_polygon(root,buttons)
    for button in buttons:
        button.draw()


canvas.bind("<Configure>", redraw_canvas)
root.mainloop()