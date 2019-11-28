import numpy as np


class ExponentialDistanceBasedSatisfactionEvaluator:
    def __init__(self, genome_length):
        self._genome_length = genome_length

    def evaluate(self, fitness):
        return np.exp(- (fitness**2) / (2 * self._genome_length**2))  # fitness equal to genome_length is 68% satisfactory
