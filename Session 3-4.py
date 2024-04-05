import random

from point import Point


class ColoredPoint(Point):  # this class inherits from point
    COLORS = ["red", "blue", "green", "purple", "pink", "beige", "bordeaux", "marsala", "peach", "turquoise", "saffron",
              "magenta"]

    def init(self, x, y, color):
        self.x = x
        self.y = y
        if color in self.COLORS:  # you can only assign colors in COLORS
            self.color = color
        else:
            raise Exception(f"That is an invalid color, accepted colors are {self.COLORS}")

    def str(self):
        return f"{self.color}({self.x}, {self.y})"

    @classmethod  # decorator, method that is a classmethod, can be called with the name of a class instead of having to call p1
    def add_extra_color(cls, color):
        cls.COLORS_append(color)

    @property
    def distance_origin(self):
        result = (self.x * 2 + self.y2) * 0.5
        if result == int(result):
            return int(result)
        else:
            return result


p1 = ColoredPoint(10, 10, "red")

# lets create a list of random 5 colored points
colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100, 100),
                     random.randint(-100, 100),
                     random.choice(ColoredPoint.COLORS)
                     )
    )

if name = "main":
    print()
print(colored_points)

# p1.add_extra_color("orange") (without classmethod using "self" instead of "cls")
ColoredPoint.add_extra_color("orange")
p2 = ColoredPoint(3, 4, "orange")
p2.x = 77  # retroactively changing the x?? no bueno
print(p2)
print(f"p2 = {p2} and has distance to origin = {p2.distance_origin()}")
