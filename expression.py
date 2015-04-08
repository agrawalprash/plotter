""" A class representing a dependent expression """


# 3rd party library
from numpy import zeros
from matplotlib.pylab import plot, show, legend, xlabel, ylabel


class Expression(object):

    def __init__(self, x_array, t_array, func):
        self.x_array = x_array
        self.t_array = t_array
        self.func = func

        self._create_data()

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
            y_array = self.data[::x]
            plot(
                self.t_array, y_array, legend='At x=%s' % x,
                xlabel='t_array', ylabel='y at x=%s' % x
            )
            show()

    #### Private protocol #####################################################

    def _create_data(self):
        """ Create a 2D data object based on the object's x and t arrays
        """
        shape = (len(self.x_array), len(self.t_array))
        self.data = zeros(shape)
        for i, x in enumerate(self.x_array):
            for j, t in enumerate(self.t_array):
                self.data[i][j] = self.func(x, t)

        return
