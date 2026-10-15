import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(x**2+y**2)

    def __str__(self):
        return f"Vector[ x:{self.x}, y:{self.y} ]"


if __name__ == "__main__":
    vector = Vector(1, 1)
    print(vector.magnitude)
