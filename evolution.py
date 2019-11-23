import itertools


class Evolution:
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
            children = self._make_children()  # make new population R from current population P
            tmp_population = self._population + children  # combine T = P + R

            fitnesses = self._evaluate(tmp_population)  # evaluate T
            self._population = self._selector.select(tmp_population, fitnesses,
                                            len(self._population))  # select from T and replace P

            self._log(logger)

        return self._get_best_creature()

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
            logger.log(self._evaluate(self._population))

    def _get_best_creature(self):
        return self._selector.select(self._population, self._evaluate(self._population), 1)[0]
