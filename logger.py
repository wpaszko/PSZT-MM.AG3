import statistics
import matplotlib.pyplot as plt


class Logger:
    DEF_PLOT_WIDTH = 6
    DEF_PLOT_HEIGHT = 6
    DEF_PLOT_DPI = 144

    def __init__(self):
        self.means = []
        self.medians = []
        self.highests = []
        self.lowests = []

    def log(self, fitnesses):
        sorted_fitnesses = sorted(fitnesses)
        self.means.append(statistics.mean(sorted_fitnesses))
        self.medians.append(statistics.median(sorted_fitnesses))
        self.highests.append(sorted_fitnesses[-1])
        self.lowests.append(sorted_fitnesses[0])

    def plot(self, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        fig, axs = plt.subplots(2, 2, sharex='all', sharey='all', figsize=figsize, dpi=dpi)
        fig.suptitle("Statistics of fitness in each generation:")
        axs[0, 0].plot(range(len(self.means)), self.means)
        axs[0, 0].set_title("Mean")
        axs[0, 1].plot(range(len(self.medians)), self.medians)
        axs[0, 1].set_title("Median")
        axs[1, 0].plot(range(len(self.highests)), self.highests)
        axs[1, 0].set_title("Highest")
        axs[1, 1].plot(range(len(self.lowests)), self.lowests)
        axs[1, 1].set_title("Lowest")
        fig.tight_layout(rect=[0, 0.03, 1, 0.9])
        plt.show()

    def plot_mean(self, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        self._plot_single_data(self.means, "Mean fitness in each generation:", figsize, dpi)

    def plot_median(self, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        self._plot_single_data(self.medians, "Median fitness in each generation:", figsize, dpi)

    def plot_highest(self, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        self._plot_single_data(self.highests, "Highest fitness in each generation:", figsize, dpi)

    def plot_lowest(self, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        self._plot_single_data(self.lowests, "Lowest fitness in each generation:", figsize, dpi)

    def _plot_single_data(self, data, title, figsize, dpi):
        plt.figure(figsize=figsize, dpi=dpi)
        plt.title(title)
        plt.plot(range(len(data)), data)
        plt.show()

    def clear(self):
        self.means = []
        self.medians = []
        self.highests = []
        self.lowests = []
