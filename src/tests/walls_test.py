import pyglet
from wall import Wall

window = pyglet.window.Window()
WIDTH = window.width
HEIGHT = window.height
LINE_COLOR = (255, 255, 255)

batch = pyglet.graphics.Batch()


def draw_walls(line):
    obj = pyglet.shapes.Line()


def main():
    line = []
    wall = Wall()
    line.append(wall.left_wall)
    line.append(wall.right_wall)
    line.append(wall.top_wall)
    line.append(wall.bottom_wall)
