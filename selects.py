def select_half_best(population, fitnesses):
    return population[: int(len(population) / 2)]  # TODO: return half of the creatures that have the best fitnesses
