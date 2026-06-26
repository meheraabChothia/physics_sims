import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')

G = 9.81
H = 1000  # meters


# s=ut + 0.5a(t^2)
# Should just need this tbh

def calculate_position(time: float):
    # time in seconds
    dis = 0.5*G*(time**2)
    return dis  # How much of the 1000 meters it has fallen


def loop():
    # How tf do I verify this??
    for i in range(100):
        print(f"Position at {i} seconds: {calculate_position(i)}")
        input()


def plotter():
    # How tf do I verify this??
    x = []
    y = []
    for i in range(100):
        # print(f"Position at {i} seconds: {calculate_position(i)}")
        x.append(calculate_position(i))
        y.append(i)

    plt.plot(x, y)
    plt.savefig('ball.png')


def time():
    import math
    t = math.sqrt(2 * 1000 / 9.81)
    print(t)
    print(calculate_position(t))


def main():
    print(calculate_position(14.27))


if __name__ == "__main__":
    plotter()
