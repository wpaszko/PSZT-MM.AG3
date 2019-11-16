class RandomOneSwapMutator:
    def __init__(self, probability):
        self._probability = probability

    def mutate(self, creature):
        return creature  # TODO: if draw (with given probability), swap one card and return mutated creature
