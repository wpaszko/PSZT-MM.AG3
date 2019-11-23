class FromLowToHighFitnessesSelection:
    def select(self, population, fitnesses, size):
        best = [x for _, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]
        return best[:size]