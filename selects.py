def select_n_best(population, fitnesses, size):
    best = [x for _, x in sorted(zip(fitnesses, population), key=lambda x: x[0], reverse=True)]
    return best[:size]