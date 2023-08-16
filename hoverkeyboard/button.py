import json
from typing import List

import numpy as np

from hoverkeyboard.action import Action
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

        

class PolygonButton:

    
    def __init__(self, canvas, polygon: List[float],center: List[float],action: Action):
        assert len(polygon) % 2 == 0
        assert len(center) == 2
        self.polygon = None
        self.text = None
        self.canvas = canvas
        self.polygon_points = polygon
        self.transformed_center=[]
        self.center = center

        # self._create_circle(self.center[0],self.center[1],5,fill="red")


        self.action = action
        self.hover_start = None




    def draw(self):
        scaled_points = self.scale_points(1)
        if len(self.transformed_center ) == 0:
            return
        if self.polygon is not None:
            self.canvas.delete(self.polygon)
            self.canvas.delete(self.text)        
        self.text= self.canvas.create_text(self.transformed_center[0],self.transformed_center[1],text=self.action.text,font=("Arial", 17))
        self.polygon = self.canvas.create_polygon(scaled_points, fill="", outline="black", width=2)
        self.canvas.tag_bind(self.polygon, "<Enter>", self.hover)
        self.canvas.tag_bind(self.polygon, "<Leave>", self.unhover)
        self.canvas.tag_bind(self.polygon, "<Button-1>", self.on_click)


    def _create_circle(self, x, y, r, **kwargs):
        return self.canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

    def scale_points(self,scale: float):
        scale_points = []
        for point_index in range(0, len(self.polygon_points),2):
            vector = [self.polygon_points[point_index]-self.center[0],self.polygon_points[point_index+1]-self.center[1]]
            scaled_vector = [vector[0]*scale,vector[1]*scale]
            scale_points.append(self.center[0]+scaled_vector[0])
            scale_points.append(self.center[1]+scaled_vector[1])                            
        return scale_points
    
    def on_click(self, event):
        #pop up text box
        input_text = input("Enter text for button: ")
        self.action = Action(input_text)
        self.hover_start = None
        self.draw()

    def hover(self, event):
        self.canvas.itemconfigure(self.polygon, fill="", outline="black", width=7)
        self.hover_start = self.canvas.tk.call('clock','milliseconds')
        self.canvas.after(70,self.check_hover)


    def check_hover(self):
        if self.hover_start is not None:
            delta = self.canvas.tk.call('clock','milliseconds') - self.hover_start

            if self.hover_start + 700 < self.canvas.tk.call('clock','milliseconds'):
                self.action.perform_action()
                self.canvas.itemconfigure(self.polygon, fill="red", outline="black", width=1)
                self.hover_start = None
            else:
                self.canvas.after(70,self.check_hover)
        

    def unhover(self, event):
        self.canvas.itemconfigure(self.polygon, fill="", outline="black", width=1)
        self.hover_start = None

def recalculate_polygon(root, buttons: List[PolygonButton]):
    points = []
    for button in buttons:
        points.append(button.center[0])
        points.append(button.center[1])
    width = root.winfo_width()
    height = root.winfo_height()
    points[::2] = [x * width for x in points[::2]]
    points[1::2] = [x * height for x in points[1::2]]

    tuple_points = np.array([[x,y] for x,y in zip(points[::2], points[1::2])])
    tessellation_results = Voronoi(tuple_points)
    point_regions = tessellation_results.point_region
    regions = tessellation_results.regions
    vertices = tessellation_results.vertices
    for polyButton,region_index in zip(buttons,point_regions):
        region = regions[region_index]
        if -1 in region or len(region) == 0:
            # Skip infinite regions
            continue
        polygon_points = np.array([vertices[i] for i in region])
        polygon_points = polygon_points.flatten().tolist()
        polyButton.polygon_points = polygon_points
        polyButton.transformed_center = [polyButton.center[0]*width,polyButton.center[1]*height]

def save_to_file(buttons: List[PolygonButton]):
    output = [
        {
            "center": button.center,
            "action": button.action.text
        }
        for button in buttons
    ]
    json_output = json.dumps(output,indent=4)
    with open("button_data.json","w") as f:
        f.write(json_output)
    print("Saved to file")

def load_from_file(root,canvas):

    with open("button_data.json","r") as f:
        data = json.load(f)

    
    buttons = []
    for button_data in data:
        buttons.append(PolygonButton(canvas,[],
                      [button_data["center"][0],
                          button_data["center"][1]]                       
                       ,Action(button_data["action"])))
    recalculate_polygon(root,buttons)
    print("Loaded from file")
    return buttons