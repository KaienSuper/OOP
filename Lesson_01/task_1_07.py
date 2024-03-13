class BoundingRectangle:
    def __init__(self):
        self.point_x = []
        self.point_y = []
 
    def add_point(self, x, y):
        self.point_x.append(x)
        self.point_y.append(y)
 
    def width(self):
        return max(self.point_x) - min(self.point_x)
 
    def height(self):
        return max(self.point_y) - min(self.point_y)
 
    def bottom_y(self):
        return min(self.point_y)
 
    def top_y(self):
        return max(self.point_y)
 
    def left_x(self):
        return min(self.point_x)
 
    def right_x(self):
        return max(self.point_x)
    
rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())