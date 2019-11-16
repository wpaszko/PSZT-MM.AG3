import random


class RandomIndependentSwitchMutator:
    def __init__(self, creature_class, probability):
        self._creature_class = creature_class
        self._probability = probability

    def mutate(self, creature):
        new_genome = [not locus if random.random() < self._probability else locus
                      for locus in creature.get_genome()]
        return self._creature_class(new_genome)


class RandomIndependentSwapMutator:
    def __init__(self, creature_class, probability):
        self._creature_class = creature_class
        self._probability = probability

    def mutate(self, creature):
        new_genome = list(creature.get_genome())
        idx = range(creature.get_genome_length())

        for current_id in idx:
            if random.random() < self._probability:
                random_id = random.choice(idx)
                new_genome[current_id], new_genome[random_id] = new_genome[random_id], new_genome[current_id]

        return self._creature_class(new_genome)
