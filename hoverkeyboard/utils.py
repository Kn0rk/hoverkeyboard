import math

def distance_squared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def centroid(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    center_x = sum(x_coords) / len(points)
    center_y = sum(y_coords) / len(points)
    return center_x, center_y

def voronoi_tessellation(points):
    voronoi_loops = {}

    for i, point in enumerate(points):
        voronoi_polygon = []

        for j, other_point in enumerate(points):
            if i != j:
                bisector_slope = -1 * (point[1] - other_point[1]) / (point[0] - other_point[0])
                bisector_center_x = (point[0] + other_point[0]) / 2
                bisector_center_y = (point[1] + other_point[1]) / 2

                # Find the point on the bisector that is furthest from both points
                bisector_len = math.sqrt(distance_squared(point, other_point)) / 2
                dx = math.sqrt(bisector_len**2 / (1 + bisector_slope**2))
                if point[0] < other_point[0]:
                    bisector_center_x += dx
                else:
                    bisector_center_x -= dx
                bisector_center_y = bisector_slope * (bisector_center_x - (point[0] + other_point[0]) / 2) + (point[1] + other_point[1]) / 2

                voronoi_polygon.append((bisector_center_x, bisector_center_y))
        
        # Sort the points in the Voronoi polygon by their angle to the centroid
        voronoi_polygon.sort(key=lambda p: math.atan2(p[1] - point[1], p[0] - point[0]))

        # Compute the centroid of the Voronoi polygon
        c = centroid(voronoi_polygon)
        voronoi_polygon.append(c)
        voronoi_loops[point] = voronoi_polygon

    return voronoi_loops

# Example usage
input_points = [(0, 0), (1, 2), (3, 1), (4, 3)]
output = voronoi_tessellation(input_points)

# Printing the result
for point, loop in output.items():
    print("Point:", point)
    print("Loop (Voronoi polygon) vertices:", loop)
    print()
import math

def distance_squared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def centroid(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    center_x = sum(x_coords) / len(points)
    center_y = sum(y_coords) / len(points)
    return center_x, center_y

def voronoi_tessellation(points):
    voronoi_loops = {}

    for i, point in enumerate(points):
        voronoi_polygon = []

        for j, other_point in enumerate(points):
            if i != j:
                bisector_slope = -1 * (point[1] - other_point[1]) / (point[0] - other_point[0])
                bisector_center_x = (point[0] + other_point[0]) / 2
                bisector_center_y = (point[1] + other_point[1]) / 2

                # Find the point on the bisector that is furthest from both points
                bisector_len = math.sqrt(distance_squared(point, other_point)) / 2
                dx = math.sqrt(bisector_len**2 / (1 + bisector_slope**2))
                if point[0] < other_point[0]:
                    bisector_center_x += dx
                else:
                    bisector_center_x -= dx
                bisector_center_y = bisector_slope * (bisector_center_x - (point[0] + other_point[0]) / 2) + (point[1] + other_point[1]) / 2

                voronoi_polygon.append((bisector_center_x, bisector_center_y))
        
        # Sort the points in the Voronoi polygon by their angle to the centroid
        voronoi_polygon.sort(key=lambda p: math.atan2(p[1] - point[1], p[0] - point[0]))

        # Compute the centroid of the Voronoi polygon
        c = centroid(voronoi_polygon)
        voronoi_polygon.append(c)
        voronoi_loops[point] = voronoi_polygon

    return voronoi_loops

# Example usage
input_points = [(0, 0), (1, 2), (3, 1), (4, 3)]
output = voronoi_tessellation(input_points)

# Printing the result
for point, loop in output.items():
    print("Point:", point)
    print("Loop (Voronoi polygon) vertices:", loop)
    print()
