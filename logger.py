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
        self.matchings = []
        self.current_gen = -1

    def log(self, fitnesses, matching):
        sorted_fitnesses = sorted(fitnesses)
        self.means.append(statistics.mean(sorted_fitnesses))
        self.medians.append(statistics.median(sorted_fitnesses))
        self.highests.append(sorted_fitnesses[-1])
        self.lowests.append(sorted_fitnesses[0])
        self.matchings.append(matching)
        self.current_gen = self.current_gen + 1

    def plot(self, start_gen=0, end_gen=None, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        if not end_gen or end_gen > self.current_gen:
            end_gen = self.current_gen

        x = range(start_gen, end_gen + 1)

        fig, axs = plt.subplots(2, 2, sharex='all', sharey='all', figsize=figsize, dpi=dpi)
        fig.suptitle("Statistics of fitness in each generation:")
        axs[0, 0].plot(x, self.means[start_gen:end_gen + 1])
        axs[0, 0].set_title("Mean")
        axs[0, 1].plot(x, self.medians[start_gen:end_gen + 1])
        axs[0, 1].set_title("Median")
        axs[1, 0].plot(x, self.highests[start_gen:end_gen + 1])
        axs[1, 0].set_title("Highest")
        axs[1, 1].plot(x, self.lowests[start_gen:end_gen + 1])
        axs[1, 1].set_title("Lowest")
        fig.tight_layout(rect=[0, 0.03, 1, 0.9])
        plt.show()

    def plot_mean(self, start_gen=0, end_gen=None, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        if not end_gen or end_gen > self.current_gen:
            end_gen = self.current_gen
        self._plot_single_data(self.means, "Mean fitness in each generation:", figsize, dpi, start_gen, end_gen)

    def plot_median(self, start_gen=0, end_gen=None, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        if not end_gen or end_gen > self.current_gen:
            end_gen = self.current_gen
        self._plot_single_data(self.medians, "Median fitness in each generation:", figsize, dpi, start_gen, end_gen)

    def plot_highest(self, start_gen=0, end_gen=None, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        if not end_gen or end_gen > self.current_gen:
            end_gen = self.current_gen
        self._plot_single_data(self.highests, "Highest fitness in each generation:", figsize, dpi, start_gen, end_gen)

    def plot_lowest(self, start_gen=0, end_gen=None, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        if not end_gen or end_gen > self.current_gen:
            end_gen = self.current_gen
        self._plot_single_data(self.lowests, "Lowest fitness in each generation:", figsize, dpi, start_gen, end_gen)

    def plot_matching(self, start_gen=0, end_gen=None, figsize=(DEF_PLOT_WIDTH, DEF_PLOT_HEIGHT), dpi=DEF_PLOT_DPI):
        if not end_gen or end_gen > self.current_gen:
            end_gen = self.current_gen
        self._plot_single_data(self.matchings, "Matching in each generation:", figsize, dpi, start_gen, end_gen)

    def _plot_single_data(self, data, title, figsize, dpi, start_gen, end_gen):
        x = range(start_gen, end_gen + 1)

        plt.figure(figsize=figsize, dpi=dpi)
        plt.title(title)
        plt.plot(x, data[start_gen:end_gen + 1])
        plt.show()

    def clear(self):
        self.means = []
        self.medians = []
        self.highests = []
        self.lowests = []
        self.matchings = []
        self.current_gen = -1
