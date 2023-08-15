from collections import namedtuple
import tkinter
import numpy as np
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
from hoverkeyboard.button import PolygonButton


from hoverkeyboard.make_grid import simple_staggered_grid


# 


root = tkinter.Tk()
canvas = tkinter.Canvas(root)
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

buttons = []
colors = ['green', 'blue', 'red', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black']
current_color = 0
class Polygon:
    def __init__(self, points):
        self.points = points
        self.tag = canvas.create_polygon(points, fill="red", outline="black",width=2)
        buttons.append(self)
        canvas.tag_bind(self.tag, "<Button-1>", self.clicked)
        canvas.tag_bind(self.tag, "<Button-3>", self.right_clicked)
        canvas.tag_bind(self.tag, "<Motion>", self.hover)


    def clicked(self, event):
        print("clicked")
        canvas.itemconfigure(self.tag, fill="blue")

    def right_clicked(self, event):
        print("right clicked")
        canvas.itemconfigure(self.tag, fill="red")

    def hover(self, event):
        print("hover")
        canvas.itemconfigure(self.tag, fill="green")

    def move(self, x, y):
        canvas.move(self.tag, x, y)

    def delete(self):
        canvas.delete(self.tag)
        buttons.remove(self)

    def get_coords(self):
        return canvas.coords(self.tag)

    def set_coords(self, coords):
        canvas.coords(self.tag, coords)

    def on_top(self):
        canvas.tag_raise(self.tag)

    def on_bottom(self):
        canvas.tag_lower(self.tag)

    def get_x(self):
        return canvas.coords(self.tag)[0]

    def get_y(self):
        return canvas.coords(self.tag)[1]

    def get_width(self):
        return canvas.coords(self.tag)[2] - canvas.coords(self.tag)[0]

    def get_height(self):
        return canvas.coords(self.tag)[5] - canvas.coords(self.tag)[1]

def moved(event):
    canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))

def redraw_canvas(event):
    width = root.winfo_width()
    height = root.winfo_height()
    print(width, height)
    canvas.config(width=width-2, height=height-2)
    canvas.delete('all')
    points = simple_staggered_grid()
    points[::2] = [x * width for x in points[::2]]
    points[1::2] = [x * height for x in points[1::2]]

    for point in range(0, len(points),2):
        # print(points[point], points[point+1])
        canvas.create_circle(points[point], points[point+1], 10, fill=colors[current_color])

    Point = namedtuple('Point', 'x y')
    tuple_points = np.array([[x,y] for x,y in zip(points[::2], points[1::2])])
    tessellation_results = Voronoi(tuple_points)
    point_regions = tessellation_results.point_region
    regions = tessellation_results.regions
    vertices = tessellation_results.vertices
    
    for index,region in enumerate((regions)):
        if -1 in region or len(region) == 0:
            # Skip infinite regions
            continue
        polygon_points = np.array([vertices[i] for i in region])
        polygon_points = polygon_points.flatten().tolist()
        PolygonButton(canvas,polygon_points,[points[index], points[index+1]])
        # canvas.create_polygon(polygon_points, outline='black', fill='', width=1)

    
    





    

tag = canvas.create_text(10, 10, text="", anchor="nw")  
canvas.bind("<Motion>", moved)
canvas.bind("<Configure>", redraw_canvas)

p = Polygon([0, 0, 100, 0, 100, 100, 0, 100])




root.mainloop()