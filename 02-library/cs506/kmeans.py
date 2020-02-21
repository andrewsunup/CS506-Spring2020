from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)

    Returns a new point which is the center of all the points.
    """
    raise NotImplementedError()


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    raise NotImplementedError()


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    raise NotImplementedError()


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    raise NotImplementedError()

def generate_k_pp(dataset, k):
    # generate k points for k_mean_pp
    return 1


def cost_function(clustering):
    raise NotImplementedError()


def k_means(dataset, k):
    # step 1: generate k points
    # step 2: do converge
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering

def k_mean_pp(data_set, k):
    # step 1: generate k points
    # step 2: do converge
    return 1
