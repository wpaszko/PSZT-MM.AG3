class DeckCreature:
    def __init__(self, genome):
        self._genome = genome

    def get_stack(self, stack_value):  # returns list of cards that are on given stack
        return [index + 1 for index, stack in enumerate(self._genome) if stack == stack_value]

    def get_stack_len(self, stack_value):  # returns number of cards that are on given stack
        return len(self.get_stack(stack_value))

    def get_genome(self):
        return self._genome

    def get_genome_length(self):
        return len(self._genome)
