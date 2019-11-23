import random


class RandomCreator:
    def __init__(self, creature_class, n):
        self._creature_class = creature_class
        self._n = n

    def create(self, size):
        return [self._creature_class([random.choice([True, False]) for i in range(self._n)]) for i in range(size)]
