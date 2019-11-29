import itertools
import random


class SinglePointCrossover:
    def __init__(self, creature_class, division_factor):
        self._creature_class = creature_class
        self._division_factor = division_factor

    def cross(self, creature_a, creature_b):
        division_point = int(
            self._division_factor * creature_a.get_genotype_length())  # find a point based on given factor

        first_parts = (creature_a.get_genotype()[:division_point], creature_b.get_genotype()[:division_point])
        second_parts = (creature_b.get_genotype()[division_point:], creature_a.get_genotype()[division_point:])

        return (self._creature_class(first_parts[0] + second_parts[0]),
                self._creature_class(first_parts[1] + second_parts[1]))


class RandomSinglePointCrossover(SinglePointCrossover):
    def __init__(self, creature_class, rng=random.Random()):
        super().__init__(creature_class, 0.0)
        self._rng = rng

    def cross(self, creature_a, creature_b):
        self._division_factor = self._rng.random()  # random division factor (so random division point)
        return super().cross(creature_a, creature_b)


class MultiPointCrossover:
    def __init__(self, creature_class, division_factors):
        self._creature_class = creature_class
        self._division_factors = division_factors

    def cross(self, creature_a, creature_b):
        division_points = self._make_division_points(
            creature_a.get_genotype_length())  # find multiple division points based on division factors
        split_parts = self._split_into_parts(creature_a.get_genotype(), creature_b.get_genotype(),
                                             division_points)  # list of tuples with parts

        parts_a, parts_b = self._get_parts(split_parts)  # convert list of tuples into two lists

        return (self._creature_class(parts_a),
                self._creature_class(parts_b))

    def _make_division_points(self, cards_length):
        division_points = [0]  # from start to first division point
        division_points.extend([int(div * cards_length) for div in self._division_factors])
        division_points.append(cards_length + 1)  # from last division point till the end (index is out of bounds)
        return division_points

    def _split_into_parts(self, genotype_a, genotype_b, division_points):
        parts = [(genotype_a[start:end], genotype_b[start:end])
                 for start, end in zip(division_points[:-1], division_points[1:])]  # for pairs of division points
        parts = [reversed(parts[i]) if i % 2 else parts[i]
                 for i in range(len(parts))]  # reverse every odd tuple (to alternate between genotypes)
        return parts

    def _get_parts(self, splitted_parts):
        parts_a, parts_b = zip(*splitted_parts)

        # flatten lists
        parts_a = list(itertools.chain.from_iterable(parts_a))
        parts_b = list(itertools.chain.from_iterable(parts_b))

        return parts_a, parts_b


class RandomMultiPointCrossover(MultiPointCrossover):
    def __init__(self, creature_class, number_of_points, rng=random.Random()):
        self._number_of_points = number_of_points
        super().__init__(creature_class, [])
        self._rng = rng

    def cross(self, creature_a, creature_b):
        self._division_factors = sorted(
            [self._rng.random() for i in range(self._number_of_points)])  # random division factors
        return super().cross(creature_a, creature_b)


class RandomIndependentCrossover:
    def __init__(self, creature_class, rng=random.Random()):
        self._creature_class = creature_class
        self._rng = rng

    def cross(self, creature_a, creature_b):
        new_genotype_a = []
        new_genotype_b = []

        for gene_a, gene_b in zip(creature_a.get_genotype(), creature_b.get_genotype()):
            if self._rng.random() < 0.5:  # for every gene flip a coin and swap if draw
                gene_a, gene_b = gene_b, gene_a

            new_genotype_a.append(gene_a)
            new_genotype_b.append(gene_b)

        return (self._creature_class(new_genotype_a),
                self._creature_class(new_genotype_b))


class RandomRespectfulCrossover:
    def __init__(self, creature_class, rng=random.Random()):
        self._creature_class = creature_class
        self._rng = rng

    def cross(self, creature_a, creature_b):
        new_genotype_a = []
        new_genotype_b = []

        for gene_a, gene_b in zip(creature_a.get_genotype(), creature_b.get_genotype()):
            if gene_a != gene_b and self._rng.random() < 0.5:  # if genes are the same, don't change anything, otherwise pick random
                gene_a, gene_b = gene_b, gene_a

            new_genotype_a.append(gene_a)
            new_genotype_b.append(gene_b)

        return (self._creature_class(new_genotype_a),
                self._creature_class(new_genotype_b))
