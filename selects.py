import random

import numpy as np


class FromTheLowestFitnessesSelection:
    def select(self, population, fitnesses, size):
        best = [x for _, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]
        return best[:size]


class SwapRandomSelection:
    def __init__(self, probability, rng=random.Random()):
        self._probability = probability
        self._rng = rng

    def select(self, population, fitnesses, size):
        best = [(y, x) for y, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]
        return [x for _, x in sorted(self._swap(best, size), key=lambda x: x[0])]

    def _swap(self, best, size):
        half_index = int(len(best) / 2)
        left_half = best[:half_index]
        right_half = best[half_index:]
        for current_id, x in enumerate(left_half):
            if self._rng.random() < self._probability:
                id = self._rng.randint(half_index, len(best) - 1)
                best[current_id], best[id] = best[id], best[current_id]
        return best[:size]


class TanhSelection:
    def select(self, population, fitnesses, size):
        best = [(y, x) for y, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]

        fitness_mean = np.mean(fitnesses)
        ln = np.log(fitness_mean)
        fitnesses = [i for i, _ in best]
        self._p = [0.5 * (1 - np.tanh(((2 * ln * i) / fitness_mean) - ln)) for i in fitnesses]
        self._p = self._p / sum(self._p)

        best_selected = []
        for i in np.random.choice(len(best), size, replace=False, p=self._p):
            best_selected.append(best[i])
        return [x for _, x in sorted(best_selected, key=lambda x: x[0])]


class ExponentialSelection:
    def __init__(self, selective_pressure):
        self._selective_pressure = selective_pressure

    def select(self, population, fitnesses, size):
        best = [(y, x) for y, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]
        fitness_std = np.std(fitnesses)
        fitness_mean = np.mean(fitnesses)
        fitnesses = [i for i, _ in best]
        p = [np.exp(-self._selective_pressure * (i - fitness_mean) / fitness_std) for i in fitnesses]
        p /= sum(p)
        best_selected = []
        for i in np.random.choice(len(best), size, replace=False, p=p):
            best_selected.append(best[i])
        return [x for _, x in sorted(best_selected, key=lambda x: x[0])]
