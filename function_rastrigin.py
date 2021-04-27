import numpy as np


def error(current_pos):
    x = current_pos[0]
    y = current_pos[1]

    return (x ** 2 - 10 * np.cos(2 * np.pi * x)) + \
           (y ** 2 - 10 * np.cos(2 * np.pi * y)) + 20


def grad_error(current_pos):
    x = current_pos[0]
    y = current_pos[1]

    return np.array(
        [2 * x + 10 * 2 * np.pi * x * np.sin(2 * np.pi * x),
         2 * y + 10 * 2 * np.pi * y * np.sin(2 * np.pi * y)])