"""Module that stores Evolution class"""

import itertools


class Evolution:
    """
    Evolution

    Main evolution logic

    On start of every generation there is a start population P
    Create new population R with crossing consecutive creatures (0 with 1, 1 with 2, 2 with 3, ...) and mutating children
    Evaluate P+R and pick new population P from them

    Has two modes:
    1. Evolving specified number of generations (evolve_n_generations)
    2. Evolving until matching is sufficient or maximum generations hit (evolve_until_satisfied)

    Returns best creature in final population
    """

    def __init__(self, creator, evaluator, selector, crossover, mutator,
                 population_size):  # pass configuration by constructor
        self._creator = creator
        self._evaluator = evaluator
        self._selector = selector
        self._crossover = crossover
        self._mutator = mutator
        self._population = self._creator.create(population_size)

    def evolve_n_generations(self, n, logger=None):
        self._log(logger)

        for i in range(n):
            self._population = self._make_new_generation()
            self._log(logger)

        return self._get_best_creature()

    def evolve_until_satisfied(self, satisfactory_matching=1.0, logger=None, max_gen=1000):
        self._log(logger)

        i = 0
        while self._get_current_matching() < satisfactory_matching and i < max_gen:
            self._population = self._make_new_generation()
            self._log(logger)
            i += 1

        return self._get_best_creature()

    def _make_new_generation(self):
        children = self._make_children()  # make new population R from current population P
        tmp_population = self._population + children  # combine T = P + R

        fitnesses = self._evaluate(tmp_population)  # evaluate T
        new_population = self._selector.select(tmp_population, fitnesses,
                                               len(self._population))  # select from T and replace P

        return new_population

    def _make_children(self):
        children = self._do_crossover()
        return self._mutate(children)

    def _do_crossover(self):
        children = [self._crossover.cross(a, b)
                    for a, b in
                    zip(self._population, self._population[1:] + self._population[:1])]  # cross pairs of population
        return list(itertools.chain.from_iterable(children))  # flatten list

    def _mutate(self, population):
        return [self._mutator.mutate(creature) for creature in population]

    def _evaluate(self, population):
        return [self._evaluator.evaluate(creature) for creature in population]

    def _log(self, logger):
        if logger:
            logger.log(self._evaluate(self._population), self._get_current_matching())

    def _get_best_creature(self):
        return self._get_best()[0]

    def _get_best_fitness(self):
        return self._get_best()[1]

    def _get_best(self):
        return min(zip(self._population, self._evaluate(self._population)), key=lambda x: x[1])

    def _get_current_matching(self):
        return self._evaluator.evaluate_matching(self._get_best_fitness())
