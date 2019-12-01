import math

import numpy as np


def get_sum_of_list(l):
    return sum(l)


def get_product_of_list(l):
    if not l:
        return 0

    product = 1
    for x in l:
        product = product * x
    return product


def get_sum_on_stack(creature, stack_value):
    return get_sum_of_list(creature.get_stack(stack_value))


def get_product_on_stack(creature, stack_value):
    return get_product_of_list(creature.get_stack(stack_value))


def get_exponential_matching(x, ref_point):
    return np.exp(
        - (x ** 2) / (2 * ref_point ** 2))  # fitness equal to ref_point is 60% satisfactory


class DistanceSumDeckEvaluator:
    MATCH_REF_POINT = 1000

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def evaluate(self, creature):
        fitness_a = abs(self._a - get_sum_on_stack(creature, True))
        fitness_b = abs(self._b - get_product_on_stack(creature, False))
        return fitness_a + fitness_b

    def evaluate_matching(self, fitness):
        return get_exponential_matching(fitness, self.MATCH_REF_POINT)


class NormalizedMeanDeckEvaluator:
    MATCH_REF_POINT = 2.0

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def evaluate(self, creature):
        fitness_a = math.sqrt(abs(self._a - get_sum_on_stack(creature, True)))
        fitness_b = math.log10(1 + abs(self._b - get_product_on_stack(creature, False)))

        return (fitness_a + fitness_b) / 2

    def evaluate_matching(self, fitness):
        return get_exponential_matching(fitness, self.MATCH_REF_POINT)


class LogarithmicMeanDeckEvaluator:
    MATCH_REF_POINT = 2.0

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def evaluate(self, creature):
        fitness_a = math.log10(1 + abs(self._a - get_sum_on_stack(creature, True)))
        fitness_b = abs(math.log10(get_product_on_stack(creature, False) / self._b))

        return (fitness_a + fitness_b) / 2

    def evaluate_matching(self, fitness):
        return get_exponential_matching(fitness, self.MATCH_REF_POINT)
