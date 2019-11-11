from creators import RandomCreator
from creatures import DeckCreature
from crossovers import HalfCrossover
from evaluators import SimpleDeckEvaluator
from evolution import Evolution
from mutations import random_one_swap_mutate
from selects import select_half_best

a = 1
b = 1
population_size = 100
creature_class = DeckCreature

evolution = Evolution(RandomCreator(creature_class),
                      SimpleDeckEvaluator(a, b),
                      select_half_best,
                      HalfCrossover(creature_class),
                      random_one_swap_mutate,
                      population_size)

final_population = evolution.evolve_n_generations(100)

print(final_population)
