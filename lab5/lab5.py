import math


class FigColor:
    color = str

    def __init__(self, _color):
        self.color = _color

    def __repr__(self):
        return self.color


class FigName:
    name = str

    def __init__(self, _name):
        self.name = _name

    def __repr__(self):
        return self.name


class Rect:
    color = FigColor
    width = int
    height = int
    name = FigName

    def __init__(self, _width, _height, _color):
        self.width = _width
        self.height = _height
        self.color = FigColor(_color)
        self.name = FigName('rectangle')

    def area(self):
        return self.width * self.height

    def getName(self):
        return self.name

    def __repr__(self):
        return str(self.width) + ' ' + str(self.height) + ' ' + str(self.color) + ' ' + str(self.name)


class Circle:
    color = FigColor
    radius = int
    name = FigName

    def __init__(self, _radius, _color):
        self.radius = _radius
        self.color = FigColor(_color)
        self.name = FigName('circle')

    def area(self):
        return self.radius ** 2 * math.pi

    def getName(self):
        return self.name

    def __repr__(self):
        return str(self.radius) + ' ' + str(self.color) + ' ' + str(self.name)


class Square(Rect):
    name = FigName

    def __init__(self, _n, _color):
        super().__init__(_n, _n, _color)
        self.name = FigName('square')

    def getName(self):
        return self.name

    def __repr__(self):
        return str(self.width) + ' ' + str(self.height) + ' ' + str(self.color) + ' ' + str(self.name)


class Point:
    __x = int()
    __y = int()

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        __x = x

    def setY(self, y):
        __y = y


class Figure:
    points = list

    def __init__(self, _lst):
        self.points = _lst

    def isPointIn(self, point):
        for i in self.points:
            if i.getX() == point.getX() and i.getY() == point.getY():
                return True
        return False


if __name__ == "__main__":
    f = Figure([Point(1, 2), Point(2, 3), Point(2, 1)])
    print(f.isPointIn(Point(2, 2)))
    print(f.isPointIn(Point(2, 1)))
    print(f.isPointIn(Point(2, 3)))
