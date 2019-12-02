"""
Module with selector classes for genetic algorithm

Selector takes the whole population (parents + children) with their fitnesses
and picks a new population from them for next iteration

Usage example:
new_population = selector.select(combined_population, combined_population_fitnesses, new_population_size)
"""

import random
import sys

import numpy as np

EPSILON = sys.float_info.epsilon


class ConsecutiveSelection:
    """
    Consecutive Selection

    Most basic selector. Picks consecutive best creatures.
    Sorts creatures based on fitnesses and picks size of them from left.
    """

    def select(self, population, fitnesses, size):
        best = [x for _, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]
        return best[:size]


class SwapRandomSelection:
    """
    Swap Random Selection

    Sorts creatures based on fitnesses, then randomly swaps some of them and picks size of them from left.

    Also elitist strategy is used: the very best creature is always picked
    """

    def __init__(self, probability, rng=random.Random()):
        self._probability = probability
        self._rng = rng

    def select(self, population, fitnesses, size):
        best = [(y, x) for y, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]
        return [x for _, x in sorted(self._swap(best, size), key=lambda x: x[0])]

    def _swap(self, best, size):
        half_index = int(len(best) / 2)  # divide temporary population into better and worse creatures
        left_half = best[1:half_index]  # best[0] is the very best, therefore cannot be swapped
        for current_id, x in enumerate(left_half):  # going by the better half of temporary population
            if self._rng.random() < self._probability:  # if is about to swap
                id = self._rng.randint(half_index, len(best) - 1)   # picks random creature from the worse half
                best[current_id], best[id] = best[id], best[current_id]  # and swaps places with them
        return best[:size]


class TanhSelection:
    """
    Tanh Selection

    Picks creature based on probability.
    Probability is proportional to hyperbolic tangent scaled so that:
        - best fitness is given value close to 1
        - mean fitness is given value equal to 0.5

    In result creatures with the best fitnesses are almost always picked, with the worst fitnesses are almost never picked
    and with fitnesses close to mean are chosen the most randomly

    Also elitist strategy is used: the very best creature is always picked
    """

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
        for i in self._np_rng.choice(len(best), size - 1, replace=False, p=p):
            best_selected.append(best[i])
        return [x for _, x in sorted(best_selected, key=lambda x: x[0])]


class ExponentialSelection:
    """
    Exponential Selection

    Picks creature based on probability.
    Probability is proportional to exponential function normalized by mean and standard deviation

    In result creatures with the best (the lowest) fitnesses are picked very often and probability shrinks exponentially
    for higher fitnesses

    Also elitist strategy is used: the very best creature is always picked

    Tests showed that it works quite good, because it gives chance to currently worse creature that could have
    potentially grow into the best solution
    """

    def __init__(self, selective_pressure, np_rng=np.random.RandomState()):
        self._selective_pressure = selective_pressure  # around 1.0
        self._np_rng = np_rng

    def select(self, population, fitnesses, size):
        best = [(y, x) for y, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]

        fitness_std = np.std(fitnesses)  # standard deviation
        fitness_mean = np.mean(fitnesses)
        fitnesses = [i for i, _ in best]

        # p = list of probabilities
        if fitness_std > EPSILON:  # standard deviation is denominator of the fraction
            p = [np.exp(-self._selective_pressure * (i - fitness_mean) / fitness_std) for i in fitnesses]
        else:  # if 0 all the probabilities are equal
            p = np.full(len(fitnesses), 1.0)

        p[0] = 0.0  # elitist strategy, the very best doesn't take part in a draw

        p /= sum(p)  # all the probabilities have to sum up to 1, therefore we divide all of them by their sum

        best_selected = [best[0]]  # elitist strategy, the very best is always chosen
        for i in self._np_rng.choice(len(best), size - 1, replace=False, p=p):
            best_selected.append(best[i])
        return [x for _, x in sorted(best_selected, key=lambda x: x[0])]
