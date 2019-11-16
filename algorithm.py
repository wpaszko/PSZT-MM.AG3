import creators
import creatures
import crossovers
import evaluators
import evolution
import mutators
import selects

a = 1
b = 1

creature_class = creatures.DeckCreature
creator = creators.RandomCreator(creature_class)
evaluator = evaluators.SimpleDeckEvaluator(a, b)
select = selects.select_half_best
crossover = crossovers.HalfCrossover(creature_class)
mutator = mutators.RandomSwapMutator(0.01)
population_size = 100

evolution = evolution.Evolution(creator,
                                evaluator,
                                select,
                                crossover,
                                mutator,
                                population_size)

final_population = evolution.evolve_n_generations(100)

print(final_population)
