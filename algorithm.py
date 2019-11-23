import creators
import creatures
import crossovers
import evaluators
import evolution
import mutators
import selects

import sys

a = sys.argv[1]
b = sys.argv[2]

creature_class = creatures.DeckCreature
creator = creators.RandomCreator(creature_class)
evaluator = evaluators.SimpleDeckEvaluator(a, b)
select = selects.select_n_best
crossover = crossovers.SinglePointCrossover(creature_class, 0.5)
mutator = mutators.RandomIndependentSwitchMutator(creature_class, 0.01)
population_size = 100

evolution = evolution.Evolution(creator,
                                evaluator,
                                select,
                                crossover,
                                mutator,
                                population_size)

best = evolution.evolve_n_generations(100)

print("Best creature:")
print("A: ", best.get_stack(True))
print("B: ", best.get_stack(False))
