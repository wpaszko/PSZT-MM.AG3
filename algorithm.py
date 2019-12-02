import argparse

import creators
import creatures
import crossovers
import evaluators
import evolution
import mutators
import selects

DEF_POPULATION_SIZE = 100
DEF_SATISFACTORY_MATCHING = 1.0


def perform(n, a, b, s=DEF_SATISFACTORY_MATCHING, population_size=DEF_POPULATION_SIZE):
    creature_class = creatures.DeckCreature
    creator = creators.RandomCreator(creature_class, n)
    evaluator = evaluators.DistanceSumDeckEvaluator(a, b)
    selector = selects.ConsecutiveSelection()
    crossover = crossovers.RandomMultiPointCrossover(creature_class, 3)
    mutator = mutators.RandomIndependentSwitchMutator(creature_class, 0.5)

    evol = evolution.Evolution(creator,
                               evaluator,
                               selector,
                               crossover,
                               mutator,
                               population_size)

    best = evol.evolve_until_satisfied(s)

    print("Best creature:")
    print("A: ", best.get_stack(True), ", sum: ", evaluators.get_sum_of_list(best.get_stack(True)))
    print("B: ", best.get_stack(False), ", product: ", evaluators.get_product_of_list(best.get_stack(False)))


if __name__ == '__main__':
    def parse_args(parser):
        args = parser.parse_args()

        if not args.N >= 1:
            parser.error("Minimum card number is 1")
        if not args.A >= 0:
            parser.error("A can't be negative")
        if not args.B >= 0:
            parser.error("B can't be negative")
        if not (0.0 <= args.s <= 1.0):
            parser.error("Satisfactory matching level has to be between 0.0 and 1.0")
        if not args.p >= 2:
            parser.error("Minimum population size is 2")

        return args


    parser = argparse.ArgumentParser(description="divide N cards into two stacks, "
                                                 "where sum of cards on first stack is closest to A "
                                                 "and product of cards on second stack is closest to B, "
                                                 "using genetic algorithm")
    parser.add_argument("N", type=int, help="number of cards")
    parser.add_argument("A", type=int, help="goal of first stack")
    parser.add_argument("B", type=int, help="goal of second stack")
    parser.add_argument("-s", type=float, default=DEF_SATISFACTORY_MATCHING, help="satisfactory matching level (0.0 - 1.0)")
    parser.add_argument("-p", type=int, default=DEF_POPULATION_SIZE, help="population size")
    args = parse_args(parser)

    perform(args.N, args.A, args.B, args.s, args.p)
