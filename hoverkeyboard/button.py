from typing import List


    


class PolygonButton:
    def __init__(self, canvas, polygon: List[float],center: List[float]):
        assert len(polygon) % 2 == 0
        assert len(center) == 2
        
        self.canvas = canvas
        self.polygon_points = polygon
        self.center = center
        def on_hover(event):

            print(f"hoverit{self.center }")

        scaled_points = self.scale_points(0.98)
        self.polygon = self.canvas.create_polygon(scaled_points, fill="", outline="black", width=2)
        self.canvas.tag_bind(self.polygon, "<Enter>", on_hover)

    def scale_points(self,scale: float):
        scale_points = []
        for point_index in range(0, len(scaled_points),2):
            vector = [self.polygon_points[point_index]-self.center[0],self.polygon_points[point_index+1]-self.center[1]]
            scaled_vector = [vector[0]*scale,vector[1]*scale]
            scale_points.append(self.center[0]+scaled_vector[0])
            scale_points.append(self.center[1]+scaled_vector[1])                            
        return scale_points
    
