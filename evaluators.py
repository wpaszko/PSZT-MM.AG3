class DistanceSumDeckEvaluator:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_sum_on_stack(self, creature, stack_value):
        return sum(creature.get_stack(stack_value))

    def get_product_on_stack(self, creature, stack_value):
        stack = creature.get_stack(stack_value)
        product = 1
        for x in stack:
            product = product * x
        return product

    def evaluate(self, creature):
        fitness_a = abs(self._a - self.get_sum_on_stack(creature, True))
        fitness_b = abs(self._b - self.get_product_on_stack(creature, False))

        return fitness_a+fitness_b
