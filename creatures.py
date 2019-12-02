"""
Module with creatures classes for genetic algorithm

Creature is defined by its genotype passed to the constructor

Creature is intended to be immutable
"""


class DeckCreature:
    """
    Deck Creature

    Represents placements of cards on stacks

    The genotype is a list of values.
    If elements on index i has a value v, it means that card i+1 is on stack represented by v

    Example:
    genotype[4] = True

    Card 5 is on stack represented by True
    """

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
