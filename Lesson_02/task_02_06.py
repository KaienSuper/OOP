class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def intersection(self, rect):
        left_x = max(self.x, rect.get_x())
        right_x = min(self.x + self.w, rect.get_x()+rect.get_w())
        top_y = max(self.y, rect.get_y())
        bottom_y = min(self.y + self.h, rect.get_y()+rect.get_h())
        if left_x < right_x and top_y < bottom_y:
            return Rectangle(left_x, top_y, right_x-left_x, bottom_y-top_y)
        else:
            return None

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_w(self):
        return self.w
    
    def get_h(self):
        return self.h
    
rect1 = Rectangle(3, 5, 2, 1)
rect2 = Rectangle(1, 2, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())