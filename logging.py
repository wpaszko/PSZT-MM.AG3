import pandas as pd


class Logger:
    def __init__(self):
        self._history = pd.DataFrame()

    def log(self, population, fitnesses, generation_number):
        return None  # TODO: log all the data

    def plot(self):
        return None  # TODO: plot everything (or pass what to plot)
