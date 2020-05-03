class Dot:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def set_coords(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_coords(self):
        return self._x, self._y, self._z

    def __add__(self, other):
        return self._x + other.get_x(), self._y + other.get_y(), self._z + other.get_z()

    def __sub__(self, other):
        return self._x - other.get_x(), self._y - other.get_y(), self._z - other.get_z()

    def __mul__(self, other):
        return self._x * other.get_x(), self._y * other.get_y(), self._z * other.get_z()

    def __truediv__(self, other):
        return self._x / other.get_x(), self._y / other.get_y(), self._z / other.get_z()

    def __neg__(self):
        return -self._x, -self._y, -self._z

    def __str__(self):
        return self.get_coords()


dot1 = Dot(1, 2, 3)
dot2 = Dot(4, 5, 6)

print(dot1 + dot2)
print(dot1 - dot2)
print(dot1 * dot2)
print(dot1 / dot2)
print(-dot1)
