import random


class RandomIndependentSwitchMutator:
    def __init__(self, creature_class, probability, rng=random.Random()):
        self._creature_class = creature_class
        self._probability = probability
        self._rng = rng

    def mutate(self, creature):  # for every gene flip a coin and negate it if draw
        new_genotype = [not gene if self._rng.random() < self._probability else gene
                        for gene in creature.get_genotype()]
        return self._creature_class(new_genotype)


class RandomIndependentSwapMutator:
    def __init__(self, creature_class, probability, rng=random.Random()):
        self._creature_class = creature_class
        self._probability = probability
        self._rng = rng

    def mutate(self, creature):  # for every gene flip a coin and swap it with random gene if draw
        new_genotype = list(creature.get_genotype())
        idx = range(creature.get_genotype_length())

        for current_id in idx:
            if self._rng.random() < self._probability:
                random_id = self._rng.choice(idx)

                # swap values
                new_genotype[current_id], new_genotype[random_id] = new_genotype[random_id], new_genotype[current_id]

        return self._creature_class(new_genotype)
