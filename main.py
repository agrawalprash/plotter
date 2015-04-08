""" Main entry point. """

# Standard library
import math

# 3rd party library
from numpy import array, linspace

# Local library
from expression import Expression


def main():
    x_array = linspace(0, 2*math.pi, 100)
    t_array = array([0, 1, 2, 3])

    def func(x, t):
        return math.sin(x*t)

    y = Expression(x_array=x_array, t_array=t_array, func=func)
    y.plot(t=1)

if __name__ == "__main__":
    main()
