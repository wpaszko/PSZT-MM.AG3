import math
import sys

import numpy as np

EPSILON = sys.float_info.epsilon


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
        - x / (2 * ref_point))  # fitness equal to ref_point is 60% satisfactory


class BaseEvaluator:
    def __init__(self, a, b):
        self._a = a
        self._b = b
        if a == 0 and b == 0:
            self._match_ref_point = EPSILON
        else:
            self._match_ref_point = self._evaluate_fitness(1.1 * a, a, 2 * b, b)

    def evaluate(self, creature):
        return self._evaluate_fitness(get_sum_on_stack(creature, True),
                                      self._a,
                                      get_product_on_stack(creature, False),
                                      self._b)

    def _evaluate_fitness(self, score_a, goal_a, score_b, goal_b):
        raise NotImplementedError("Please Implement this method")

    def _evaluate_fitness_a(self, creature_score, goal):
        raise NotImplementedError("Please Implement this method")

    def _evaluate_fitness_b(self, creature_score, goal):
        raise NotImplementedError("Please Implement this method")

    def evaluate_matching(self, fitness):
        return get_exponential_matching(fitness, self._match_ref_point)


class DistanceSumDeckEvaluator(BaseEvaluator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def _evaluate_fitness(self, score_a, goal_a, score_b, goal_b):
        fitness_a = self._evaluate_fitness_a(score_a, goal_a)
        fitness_b = self._evaluate_fitness_b(score_b, goal_b)
        return fitness_a + fitness_b

    def _evaluate_fitness_a(self, creature_score, goal):
        return abs(goal - creature_score)

    def _evaluate_fitness_b(self, creature_score, goal):
        return abs(goal - creature_score)


class NormalizedDistanceSumDeckEvaluator(BaseEvaluator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def _evaluate_fitness(self, score_a, goal_a, score_b, goal_b):
        fitness_a = self._evaluate_fitness_a(score_a, goal_a)
        fitness_b = self._evaluate_fitness_b(score_b, goal_b)
        return fitness_a + fitness_b

    def _evaluate_fitness_a(self, creature_score, goal):
        if goal == 0:
            fitness = creature_score
        else:
            fitness = abs(goal - creature_score) / goal

        return fitness

    def _evaluate_fitness_b(self, creature_score, goal):
        if goal == 0:
            fitness = creature_score
        else:
            fitness = abs(goal - creature_score) / goal

        return fitness


class NormalizedMeanDeckEvaluator(BaseEvaluator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def _evaluate_fitness(self, score_a, goal_a, score_b, goal_b):
        fitness_a = self._evaluate_fitness_a(score_a, goal_a)
        fitness_b = self._evaluate_fitness_b(score_b, goal_b)
        return (fitness_a + fitness_b) / 2

    def _evaluate_fitness_a(self, creature_score, goal):
        return math.sqrt(abs(goal - creature_score))

    def _evaluate_fitness_b(self, creature_score, goal):
        return math.log10(1 + abs(goal - creature_score))


class LogarithmicMeanDeckEvaluator(BaseEvaluator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def _evaluate_fitness(self, score_a, goal_a, score_b, goal_b):
        fitness_a = self._evaluate_fitness_a(score_a, goal_a)
        fitness_b = self._evaluate_fitness_b(score_b, goal_b)
        return (fitness_a + fitness_b) / 2

    def _evaluate_fitness_a(self, creature_score, goal):
        return math.log10(1 + abs(goal - creature_score))

    def _evaluate_fitness_b(self, creature_score, goal):
        if goal == 0:
            if creature_score == 0:
                fitness = 0
            else:
                fitness = creature_score
        else:
            if creature_score == 0:
                fitness = abs(math.log10(0.5 / goal))
            else:
                fitness = abs(math.log10(creature_score / goal))

        return fitness
