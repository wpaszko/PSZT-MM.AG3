class RandomCreator:
    def __init__(self, creature_class):
        self._creature_class = creature_class

    def create(self, size):
        return [self._creature_class([]) for i in range(size)]  # TODO: return population of given size
