import itertools


class Evolution:
    def __init__(self, creator, evaluator, select, crossover, mutator, population_size):
        self._creator = creator
        self._evaluator = evaluator
        self._select = select
        self._crossover = crossover
        self._mutator = mutator
        self._population = self._creator.create(population_size)

    def evolve_n_generations(self, n, logger=None):
        for i in range(n):
            children = [self._crossover.cross(a, b) for a, b in zip(self._population, self._population[1:] + self._population[:1])]
            children = list(itertools.chain.from_iterable(children))
            children = [self._mutator.mutate(child) for child in children]
            tmp_population = self._population + children
            fitnesses = [self._evaluator.evaluate(creature) for creature in tmp_population]
            self._population = self._select(tmp_population, fitnesses, len(self._population))

        return self._population  # TODO: clean this mess up
