import random


class FromTheLowestFitnessesSelection:
    def select(self, population, fitnesses, size):
        best = [x for _, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]
        return best[:size]


class SwapRandomSelection:
    def __init__(self, probability, rng=random.Random()):
        self._probability = probability
        self._rng = rng

    def select(self, population, fitnesses, size):
        best = [(y, x) for y, x in sorted(zip(fitnesses, population), key=lambda x: x[0])]
        return [x for _, x in sorted(self._swap(best, size), key=lambda x: x[0])]

    def _swap(self, best, size):
        half_index = int(len(best) / 2)
        left_half = best[:half_index]
        right_half = best[half_index:]
        for current_id, x in enumerate(left_half):
            if self._rng.random() < self._probability:
                id = self._rng.randint(half_index, len(best)-1)
                best[current_id], best[id] = best[id], best[current_id]
        return best[:size]

