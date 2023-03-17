class Point():
    def __init__(self, x, y):
        """
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    # checks values to see if point one = point two
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    # Rewrites print one to point 2
    def rewrite(self, other):
        self.x = other.x
        self.y = other.y


class Curve():
    def __init__(self, P, G, a, b):
        """
        :param P: Finite field (Fp)
        :param a/b: Curve parameters such that y^2 = x^3 + ax + b
        :param G: Base point upon the curve
        id_ele: the identity element (point of infinity)
        """
        self.p = P
        self.g = G
        self.a = a
        self.b = b
        self.id_ele = Point(0, 0)

    def infinite_point(self):
        return self.id_ele
