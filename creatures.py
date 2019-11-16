class DeckCreature:
    def __init__(self, genome):
        self._genome = genome

    def get_stack(self, stack_value):
        return [index+1 for index, stack in enumerate(self._genome) if stack == stack_value]

    def get_stack_len(self, stack_value):
        return len(self.get_stack(stack_value))

    def get_genome(self):
        return self._genome

    def get_cards_length(self):
        return len(genome)
