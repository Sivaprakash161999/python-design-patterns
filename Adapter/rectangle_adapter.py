

class RectangleAdapter:
    def __init__(self, rectangle):
        self._rectangle = rectangle
    
    def get_new_rectangle(self):
        return NewRectangle(self._rectangle.x, self._rectangle.y,
                            self._rectangle.x + self._rectangle.w,
                            self._rectangle.y + self._rectangle.h)

class OldRectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return f"Old Rectangle x: {self.x}, y: {self.y}," \
                + f" w: {self.w}, h: {self.h}"
    

class NewRectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"New Rectangle x1: {self.x1}, y1: {self.y1}," \
                + f" x2: {self.x2}, y2: {self.y2}"
    


if __name__ == '__main__':
    old_rectangle = OldRectangle(0, 0, 10, 5)
    new_rectangle = NewRectangle(0, 0, 10, 5)

    adapter = RectangleAdapter(old_rectangle)
    print(new_rectangle)
    print(adapter.get_new_rectangle())