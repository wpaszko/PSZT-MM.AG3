class DeckCreature:
    def __init__(self, genotype):
        self._genotype = genotype

    def get_stack(self, stack_value):  # returns list of cards that are on given stack
        return [index + 1 for index, stack in enumerate(self._genotype) if stack == stack_value]

    def get_stack_len(self, stack_value):  # returns number of cards that are on given stack
        return len(self.get_stack(stack_value))

    def get_genotype(self):
        return self._genotype

    def get_genotype_length(self):
        return len(self._genotype)
