#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
# import tsp
# import mlrose_solver
from opt import TSP
import time
import itertools
import numpy as np
from tqdm import tqdm
Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return np.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    indexs = {}
    points = []
    edges = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))
        indexs[Point(float(parts[0]), float(parts[1]))] = i - 1

    # all_combinations = itertools.combinations(points, 2)
    # for p in tqdm(all_combinations):
    #     edges.append((p[0], p[1], length(p[0], p[1])))

    if nodeCount < 10000:
        for p in range(len(points) - 1):
            for p2 in range(p + 1, len(points)):
                w = length(points[p], points[p2])
                edges.append((points[p], points[p2], w))
                edges.append((points[p2], points[p], w))

        edges.append((points[-1], points[0], length(points[-1], points[0])))
        edges.append((points[0], points[-1], length(points[-1], points[0])))
        tsp = TSP(points, edges)

        tour, _ = tsp.greedyTour(startnode=None, randomized=False)
    else:
        tsp = TSP(points, edges)
        tour = points
    solution, obj = tsp.threeOPT(tour)

    # tsp.main(points)
    # build a trivial solution
    # visit the nodes in the order they appear in the file
    # solution = range(0, nodeCount)
    #
    # # calculate the length of the tour
    # obj = length(points[solution[-1]], points[solution[0]])
    # for index in range(0, nodeCount-1):
    #     obj += length(points[solution[index]], points[solution[index+1]])
    # solution, obj = mlrose_solver.solve(points, nodeCount)
    # prepare the solution in the specified output format
    output_data = '%.2f' % obj + ' ' + str(0) + '\n'
    output_data += ' '.join(map(lambda x: str(indexs[x]), solution[:-1]))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')

