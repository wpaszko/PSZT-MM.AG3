import numpy as np


class ExponentialDistanceBasedSatisfactionEvaluator:
    def __init__(self, genotype_length):
        self._genotype_length = genotype_length

    def evaluate(self, fitness):
        return np.exp(
            - (fitness ** 2) / (2 * self._genotype_length ** 2))  # fitness equal to genotype_length is 68% satisfactory
