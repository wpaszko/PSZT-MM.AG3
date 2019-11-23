import random


class RandomIndependentSwitchMutator:
    def __init__(self, creature_class, probability, rng=random.Random()):
        self._creature_class = creature_class
        self._probability = probability
        self._rng = rng

    def mutate(self, creature):  # for every locus flip a coin and negate it if draw
        new_genome = [not locus if self._rng.random() < self._probability else locus
                      for locus in creature.get_genome()]
        return self._creature_class(new_genome)


class RandomIndependentSwapMutator:
    def __init__(self, creature_class, probability, rng=random.Random()):
        self._creature_class = creature_class
        self._probability = probability
        self._rng = rng

    def mutate(self, creature):  # for every locus flip a coin and swap it with random locus if draw
        new_genome = list(creature.get_genome())
        idx = range(creature.get_genome_length())

        for current_id in idx:
            if self._rng.random() < self._probability:
                random_id = self._rng.choice(idx)

                # swap values
                new_genome[current_id], new_genome[random_id] = new_genome[random_id], new_genome[current_id]

        return self._creature_class(new_genome)
