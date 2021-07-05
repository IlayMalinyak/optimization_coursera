import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def solve(points, length):
    fitness_coords = mlrose.TravellingSales(coords=points)
    problem_fit = mlrose.TSPOpt(length=length, fitness_fn=fitness_coords,
                                       maximize=False)
    best_state, best_fitness = mlrose.random_hill_climb(problem_fit)
    return best_state, best_fitness