"""
Module with evaluator classes for genetic algorithm

Evaluators take a creature and return its fitness score (evaluated according to evaluator's rule)

Also each evaluator can return a matching score based on given fitness (how close it is to a solution)

Usage example:
fitness = evaluator.evaluate(creature)
matching = evaluator.evaluate_matching(fitness)
"""

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
    """
    Base Evaluator

    "Abstract" base class to eliminate code duplication

    Attributes:
        a - goal of sum of cards on first stack
        b - goal of product of cards on second stack
        match_ref_point - value that can be referenced by matching evaluation, fitness value that can be considered 60 % matching

    Default match_ref_point is fitness of 110% of a and 2 times b,
    which means that sum that is 10% more than goal and product that is 2 times more than goal are 60% matching
    """

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
    """
    Sum of Distances on Deck Evaluator

    Fitness is distance from goal a plus distance from goal b

    Most basic evaluator.
    Given that product of cards on second stack can be enormously bigger than sum of cards on first stack,
    it tends to prefer satisfying the second stack. Also it's hard to find any relations with such nonlinear values.
    """

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
    """
    Sum of Normalized Distances on Deck Evaluator

    Fitness is distance from goal a divided by a plus distance from goal b divided by b

    Similar to DistanceSumDeckEvaluator, but distances are divided by goals which should make then more sane,
    but still not linear
    """

    def __init__(self, a, b):
        super().__init__(a, b)

    def _evaluate_fitness(self, score_a, goal_a, score_b, goal_b):
        fitness_a = self._evaluate_fitness_a(score_a, goal_a)
        fitness_b = self._evaluate_fitness_b(score_b, goal_b)
        return fitness_a + fitness_b

    def _evaluate_fitness_a(self, creature_score, goal):
        if goal == 0:
            fitness = creature_score  # special case: when goal is 0, can't divide by it, so set fitness to score
        else:
            fitness = abs(goal - creature_score) / goal

        return fitness

    def _evaluate_fitness_b(self, creature_score, goal):
        if goal == 0:
            fitness = creature_score  # special case: when goal is 0, can't divide by it, so set fitness to score
        else:
            fitness = abs(goal - creature_score) / goal

        return fitness


class NormalizedMeanDeckEvaluator(BaseEvaluator):
    """
    Mean of Normalized Distances on Deck Evaluator

    Fitness on a is square root of distance
    Fitness on b is common logarithm of distance
    Resultant fitness is mean of fitness a and b

    Premise:
    Sum of cards is growing like sum of natural number series which is quadratic. We can make it linear by square rooting
    Product of cards is growing like a factorial. We can make it closer to linear by applying logarithm

    Tests showed that it works better than just absolute distance
    """

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
    """
    Mean of Normalized Distances on Deck Evaluator

    Fitness on a is common logarithm of distance
    Fitness on b is common logarithm of quotient
    Resultant fitness is mean of fitness a and b

    Premise:
    Distance 10^n from a should have a fitness equal to n, so distance 1000 scores 3
    Quotient 10^n of b should have a fitness equal to b, so 1000 times more than b scores 3

    Tests showed that it competes with NormalizedMeanDeckEvaluator and has the most linear scores
    """

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
            fitness = creature_score  # special case: when goal is 0, can't divide by it, so set fitness to score
        else:
            if creature_score == 0:
                # special case: when score is 0, can't divide by it
                # so set fitness as if score was 0.5 (which is less than lowest possible value)
                fitness = abs(math.log10(0.5 / goal))
            else:
                fitness = abs(math.log10(creature_score / goal))

        return fitness
