# !/usr/bin/python
# -*- coding: UTF-8 -*-

from math import pi

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * pi

    def perimeter(self):
        return self.radius * 2 * pi


class Ring:
    def __init__(self, radius_outside, radius_inside):

        self.outside_redius = Circle(radius_outside)
        self.inside_redius = Circle(radius_inside)

    def rin_area(self):

        return self.outside_redius.area() - self.inside_redius.area()

    def rin_perimeter(self):

        return self.outside_redius.perimeter() + self.inside_redius.perimeter()


ring = Ring(9, 3)   # 实例化一个圆环
rinArea = ring.rin_area()   # 计算圆环的面积
rinPer = ring.rin_perimeter()   # 计算圆环的周长
print(rinArea, rinPer)  # 打印圆环的面积和周长

