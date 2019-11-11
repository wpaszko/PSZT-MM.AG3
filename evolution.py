class Evolution:
    def __init__(self, creator, evaluator, select, crossover, mutate, population_size):
        self._creator = creator
        self._evaluator = evaluator
        self._select = select
        self._crossover = crossover
        self._mutate = mutate
        self._population = self._creator.create(population_size)

    def evolve_n_generations(self, n, logger=None):
        for i in range(n):
            fitnesses = [self._evaluator.evaluate(creature) for creature in self._population]
            best = self._select(self._population, fitnesses)
            children = [self._crossover.cross(a, b) for a, b in zip(best, best[1:] + best[:1])]
            children = [self._mutate(child) for child in children]

        return self._population  # TODO: clean this mess up
