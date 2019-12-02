"""
Module with creator classes for genetic algorithm

Creates new population of creatures

Usage example:
population = creator.create(population_size)
"""

import random


class RandomCreator:
    """
    Random Creator

    Creates population of creatures with random genotypes

    Each genotype is a list of random True/False values

    Attributes:
        creature_class - *class* of creatures, necessary to create instances
        n - genotype length
        rng - random number generator
    """

    def __init__(self, creature_class, n, rng=random.Random()):
        self._creature_class = creature_class
        self._n = n
        self._rng = rng

    def create(self, size):
        return [self._creature_class([self._rng.choice([True, False]) for i in range(self._n)]) for i in range(size)]
