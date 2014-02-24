import matplotlib.pyplot as plt
import pickle
from matplotlib.patches import Rectangle


class malama_figure:
    def __init__(self, savename):
        self.fig_dikt = pickle.load(open(savename, 'rb'))

    def plot_all(self):
        fig = plt.figure()
        # apparantly I need to add some axes before it can be seen
        #getattr(ax, 'set_ylabel')('bla')
        fig = self.__setup_figure(fig)
        if len(self.fig_dikt) <= 1:
            raise Exception('No subplot specified')
        fig = self.__setup_subplots(fig)

        fig.add_subplot(111)

        return fig

    def __setup_subplots(self, fig, ncol=None, nrow=None, number=[]):
        #
        if not number:
            # use all subplots in saved ncol and nrow
            if not number and not ncol and not nrow:
                ncol = self.fig_dikt[('ax', 0)]['ax_info']['numCols']
                nrow = self.fig_dikt[('ax', 0)]['ax_info']['numRows']
            for key, value in self.fig_dikt.iteritems():
                if key != 'fig_info':
                    pos = key[1] + 1
                    ax = fig.add_subplot(ncol, nrow, pos)
                    ax = self.__setup_subplot(ax, value['ax_info'])
                    #print 'value: ', value
                    ax = self.__draw_lines(ax, value['lines'])
                    ax = self.__draw_patches(ax, value['patches'])
                    ax.figure.canvas.draw()
        return fig

    def __draw_patches(self, ax, dikt):
        for label, patches in dikt.iteritems():
            for patch in patches:
                rect = Rectangle((patch['set_x'], patch['set_y']),
                                 width=patch['set_width'],
                                 height=patch['set_height'])
                for key, value in patch.iteritems():
                    getattr(rect, key)(value)
                ax.add_patch(rect)
        return ax

    def __draw_lines(self, ax, dikt):
        for label, line in dikt.iteritems():
            li = ax.plot(line['set_xdata'], line['set_ydata'])
            for key, value in line.iteritems():
                getattr(li[0], key)(value)
        return ax

    def __setup_subplot(self, ax, dikt):
        for key, value in dikt.iteritems():
            if 'set' in key:
                getattr(ax, key)(value)
        return ax

    def __setup_figure(self, fig):
        for key, value in self.fig_dikt['fig_info'].iteritems():
            if hasattr(fig, key):
                getattr(fig, key)(value)
        return fig
