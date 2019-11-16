import random


class SinglePointCrossover:
    def __init__(self, creature_class, division_factor):
        self._creature_class = creature_class
        self._division_factor = division_factor

    def cross(self, creature_a, creature_b):
        division_point = int(self._division_factor * creature_a.get_cards_length())

        first_parts = (creature_a.get_genome()[:division_point], creature_b.get_genome()[:division_point])
        second_parts = (creature_b.get_genome()[division_point:], creature_a.get_genome()[division_point:])

        return (self._creature_class(first_parts[0] + second_parts[0]),
                self._creature_class(first_parts[1] + second_parts[1]))


