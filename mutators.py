import random


class RandomSwapMutator:
    def __init__(self, creature_class, probability):
        self._creature_class = creature_class
        self._probability = probability

    def mutate(self, creature):
        new_genome = [not locus if random.random() < self._probability else locus
                      for locus in creature.get_genome()]
        return self._creature_class(new_genome)
