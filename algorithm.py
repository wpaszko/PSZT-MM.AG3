import creators
import creatures
import crossovers
import evaluators
import evolution
import mutators
import selects

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
n = int(sys.argv[3])

creature_class = creatures.DeckCreature
creator = creators.RandomCreator(creature_class, n)
evaluator = evaluators.DistanceSumDeckEvaluator(a, b)
selector = selects.FromLowToHighFitnessesSelection()
crossover = crossovers.RandomMultiPointCrossover(creature_class, 3)
mutator = mutators.RandomIndependentSwitchMutator(creature_class, 0.5)
population_size = 100

evol = evolution.Evolution(creator,
                           evaluator,
                           selector,
                           crossover,
                           mutator,
                           population_size)

best = evol.evolve_n_generations(100)

print("Best creature:")
print("A: ", best.get_stack(True), ", sum: ", evaluator.get_sum_on_stack(best, True))
print("B: ", best.get_stack(False), ", product: ", evaluator.get_product_on_stack(best, False))
