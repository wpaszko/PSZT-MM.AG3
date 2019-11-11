class HalfCrossover:
    def __init__(self, creature_class):
        self._creature_class = creature_class

    def cross(self, creature_a, creature_b):
        return self._creature_class(
            [])  # TODO: return new creature that has half of genes from creature a and half from creature b
