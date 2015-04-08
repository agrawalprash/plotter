""" A class representing a dependent expression """


# 3rd party library
from matplotlib.pylab import plot, show, xlabel, ylabel


class Expression(object):

    def __init__(self, x_array, t_array, data):
        self.x_array = x_array
        self.t_array = t_array
        self.data = data

    def plot(self, x=None, t=None):
        if x is None and t is None:
            raise RuntimeError("Invalid input")

        if t is not None:
            y_array = self.data[:, t]
            title = 'At t=%s' % t
            plot(self.x_array, y_array)
            xlabel('x_array')
            ylabel(title)
            show()

        if x is not None:
            y_array = self.data[x, :]
            title = 'At x=%s' % x
            plot(self.t_array, y_array)
            xlabel('t_array')
            ylabel(title)
            show()
