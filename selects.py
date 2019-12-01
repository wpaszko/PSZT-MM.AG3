import random
import sys

import numpy as np

EPSILON = sys.float_info.epsilon


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
    def __init__(self, np_rng=np.random.RandomState()):
        self._np_rng = np_rng

    def select(self, population, fitnesses, size):
        best = [(y, x) for y, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]

        fitness_mean = np.mean(fitnesses)
        ln = np.log(fitness_mean)
        fitnesses = [i for i, _ in best]
        p = [0.5 * (1 - np.tanh(((2 * ln * i) / fitness_mean) - ln)) for i in fitnesses]

        p[0] = 0.0

        p /= sum(p)

        best_selected = [best[0]]
        for i in self._np_rng.choice(len(best), size-1, replace=False, p=p):
            best_selected.append(best[i])
        return [x for _, x in sorted(best_selected, key=lambda x: x[0])]


class ExponentialSelection:
    def __init__(self, selective_pressure, np_rng=np.random.RandomState()):
        self._selective_pressure = selective_pressure
        self._np_rng = np_rng

    def select(self, population, fitnesses, size):
        best = [(y, x) for y, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]

        fitness_std = np.std(fitnesses)
        fitness_mean = np.mean(fitnesses)
        fitnesses = [i for i, _ in best]

        if fitness_std > EPSILON:
            p = [np.exp(-self._selective_pressure * (i - fitness_mean) / fitness_std) for i in fitnesses]
        else:
            p = np.full(len(fitnesses), 1.0)

        p[0] = 0.0

        p /= sum(p)

        best_selected = [best[0]]
        for i in self._np_rng.choice(len(best), size-1, replace=False, p=p):
            best_selected.append(best[i])
        return [x for _, x in sorted(best_selected, key=lambda x: x[0])]
