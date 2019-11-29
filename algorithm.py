import sys

import creators
import creatures
import crossovers
import evaluators
import evolution
import mutators
import satisfaction
import selects

a = int(sys.argv[1])
b = int(sys.argv[2])
n = int(sys.argv[3])
s = float(sys.argv[4])

creature_class = creatures.DeckCreature
creator = creators.RandomCreator(creature_class, n)
evaluator = evaluators.DistanceSumDeckEvaluator(a, b)
selector = selects.FromTheLowestFitnessesSelection()
crossover = crossovers.RandomMultiPointCrossover(creature_class, 3)
mutator = mutators.RandomIndependentSwitchMutator(creature_class, 0.5)
satisfaction_evaluator = satisfaction.ExponentialDistanceBasedSatisfactionEvaluator(n)
population_size = 100

evol = evolution.Evolution(creator,
                           evaluator,
                           selector,
                           crossover,
                           mutator,
                           population_size)

best = evol.evolve_until_satisfied(satisfaction_evaluator, s)

print("Best creature:")
print("A: ", best.get_stack(True), ", sum: ", evaluators.get_sum_of_list(best.get_stack(True)))
print("B: ", best.get_stack(False), ", product: ", evaluators.get_product_of_list(best.get_stack(False)))
