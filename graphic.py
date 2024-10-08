import matplotlib.pyplot as plt
import sys


def plot_curve(values):

    plt.plot([i for i in range(len(values))], values)
    plt.title("Evolution of average distance of bees per generation")
    plt.xlabel("Generation")
    plt.ylabel("Average Distance")
    plt.grid(True)
    plt.show()


def drow_path_bee_matplotlib(path: list):
    # Start at (500, 500)
    start_point = (500, 500)
    end_point = (500, 500)

    x_coords, y_coords = zip(*path)

    full_x_coords = [start_point[0]] + list(x_coords) + [end_point[0]]
    full_y_coords = [start_point[1]] + list(y_coords) + [end_point[1]]

    plt.plot(full_x_coords, full_y_coords, marker="o", linestyle="-", color="b")

    plt.title("Linked Path of Positions")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")

    plt.grid(True)

    plt.show()


def drow_path_bee_turtle(path):
    import turtle as tr

    screen = tr.Screen()

    screen.setup(1000, 1000, 0, 0)
    screen.bgcolor("lightblue")

    bee = tr.Turtle()
    for pos in path:
        bee.goto(pos[0] - 500, pos[1] - 500)

    bee.goto(0, 0)
    tr.done


def print_bar(iteration, total):
    length = 40
    fill = "█"
    empty = "-"
    suffix = "Complete"
    percent = iteration / total
    filled_length = int(length * percent)
    bar = fill * filled_length + empty * (length - filled_length)
    sys.stdout.write(f"\r|{bar}| {percent:.2%} {suffix}")
    sys.stdout.flush()
