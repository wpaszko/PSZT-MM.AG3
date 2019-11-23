import random


class RandomCreator:
    def __init__(self, creature_class, n, rng=random.Random()):
        self._creature_class = creature_class
        self._n = n
        self._rng = rng

    def create(self, size):
        return [self._creature_class([self._rng.choice([True, False]) for i in range(self._n)]) for i in range(size)]
