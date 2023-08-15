from typing import List

from hoverkeyboard.action import Action


    


class PolygonButton:

    
    def __init__(self, canvas, polygon: List[float],center: List[float],action: Action):
        assert len(polygon) % 2 == 0
        assert len(center) == 2
        
        self.canvas = canvas
        self.polygon_points = polygon
        self.center = center
        self._create_circle(self.center[0],self.center[1],5,fill="red")


        scaled_points = self.scale_points(1)
        self.polygon = self.canvas.create_polygon(scaled_points, fill="", outline="black", width=2)
        self.canvas.tag_bind(self.polygon, "<Enter>", self.hover)
        self.canvas.tag_bind(self.polygon, "<Leave>", self.unhover)
        



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
    
    def hover(self, event):
        self.canvas.itemconfigure(self.polygon, fill="green")

    def unhover(self, event):
        self.canvas.itemconfigure(self.polygon, fill="")