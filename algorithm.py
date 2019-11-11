import creators
import creatures
import crossovers
import evaluators
import evolution
import mutations
import selects

a = 1
b = 1

creature_class = creatures.DeckCreature
creator = creators.RandomCreator(creature_class)
evaluator = evaluators.SimpleDeckEvaluator(a, b)
select = selects.select_half_best
crossover = crossovers.HalfCrossover(creature_class)
mutation = mutations.random_one_swap_mutate
population_size = 100

evolution = evolution.Evolution(creator,
                                evaluator,
                                select,
                                crossover,
                                mutation,
                                population_size)

final_population = evolution.evolve_n_generations(100)

print(final_population)
