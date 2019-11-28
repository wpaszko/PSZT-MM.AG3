def get_sum_of_list(l):
    return sum(l)


def get_product_of_list(l):
    if not l:
        return 0

    product = 1
    for x in l:
        product = product * x
    return product


class DistanceSumDeckEvaluator:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def evaluate(self, creature):
        fitness_a = abs(self._a - self.get_sum_on_stack(creature, True))
        fitness_b = abs(self._b - self.get_product_on_stack(creature, False))

        return fitness_a + fitness_b

    def get_sum_on_stack(self, creature, stack_value):
        return get_sum_of_list(creature.get_stack(stack_value))

    def get_product_on_stack(self, creature, stack_value):
        return get_product_of_list(creature.get_stack(stack_value))
