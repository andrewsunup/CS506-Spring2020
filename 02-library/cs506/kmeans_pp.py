from collections import defaultdict
from math import inf
import random
import csv
import math
#import numpy as np

"""
# import data, used in .pynb file
def import_data(path):
    with open(path, "r") as file:
        temp = file.readlines()
        rowCount = len(temp)
        file.seek(0)
        temp = file.readline().split(',')
        featureCount = len(temp)
        file.seek(0)
        X = np.empty((rowCount, featureCount))
        for i in range(rowCount):
            oneLine = file.readline().split(',')
            for j in range(len(oneLine)):
                if oneLine[j] == '?':
                    oneLine[j] = np.nan
                if isinstance(oneLine[j], str):
                    oneLine[j] = float(oneLine[j])
            X[i] = oneLine
    return X
"""

def point_avg(points):
    #n = len(points)
    #x = sum([p[0] for p in points]) / n
    #y = sum([p[1] for p in points]) / n
    #return [x, y]
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)

    Returns a new point which is the center of all the points.
    """

    if isinstance(points, int):
        temp = []
        temp.append(points)
        return temp
        #raise ValueError("input should be a list")

    if len(points) == 0:
        raise ValueError("input cannot be empty")

    dim = len(points[0])
    avgList = []
    for j in range(dim):
        sum = 0
        for i in range(len(points)):
            sum = sum + points[i][j]
        oneAvg = sum/len(points)
        avgList.append(oneAvg)
    return avgList


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    """
    k = max(assignments) + 1
    clusters = [[] for i in range(k)]
    for pointIndex, pointAssignment in enumerate(assignments):
        clusters[pointAssignment].append(dataset[pointIndex])

    new_centers = []
    for cluster in clusters:
        new_centers.append(point_avg(cluster))

    return new_centers
    """
    # list to store new generated centers
    centerList = []
    # by len(centerNum), find out the number of centers, since input parameteres don't contain K
    centerNum = []
    for i in range(len(assignments)):
        if assignments[i] not in centerNum:
            centerNum.append(assignments[i])
    k = len(centerNum)

    pointsList = convertArrayToList(dataset)
    for i in range(k):
        clusterList = []
        for j in range(len(pointsList)):
            if assignments[j] == i:
                clusterList.append(pointsList[j])
        centerList.append(point_avg(clusterList))
    return centerList

def assign_points(data_points, centers):
    """
    Given data points and k centers, assign these data points to k clusters defined by these k centers
    return clusters
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
    #return sum([(a - b) ** 2 for a, b in zip(a, b)]) ** 0.5
    dim = len(a)
    squareSum = 0
    for i in range(dim):
        squareSum = squareSum + math.pow((a[i] - b[i]), 2)
    distance = math.pow(squareSum, 0.5)
    #raise NotImplementedError()
    return distance

def distance_squared(a, b):
    return distance(a, b) ** 2


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    #return random.sample(dataset, k)
    indexList = []
    pointsList = []
    count = 0
    while count < k:
        randIndex = random.randint(0, len(dataset)-1)
        if randIndex not in indexList:
            indexList.append(randIndex)
            count = count + 1
    for i in indexList:
        pointsList.append(dataset[i])
    return pointsList

def cost_function(clustering):
#def cost_function(assignments, dataset):

    cost = 0
    for idx in clustering:
        center = point_avg(clustering[idx])
        cost += sum([distance_squared(center, p) for p in clustering[idx]])

    return cost


    """
    # by len(centerNum), find out the number of centers, since input parameteres don't contain K
    centerNum = []
    for i in range(len(assignments)):
        if assignments[i] not in centerNum:
            centerNum.append(assignments[i])
    k = len(centerNum)

    cost = 0
    pointsList = convertArrayToList(dataset)
    for i in range(k):
        clusterList = []
        for j in range(len(pointsList)):
            if assignments[j] == i:
                clusterList.append(pointsList[j])
        center = point_avg(clusterList)
        partialCost = sum([distance_squared(center, p) for p in clusterList])
        cost += partialCost
    return cost
    """

def generate_k_pp(dataset, k):
    center = random.choice(dataset)
    k_points = [center]

    while len(k_points) < k:
        prob = []
        for point in dataset:
            prob.append(distance_squared(center, point))

        prob = [p/sum(prob) for p in prob]
        center = random.choices(dataset, prob)[0]

        k_points.append(center)

    return k_points


def _do_lloyds_algo(dataset, k_points):
    """
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
    """
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    #clustering = defaultdict(list)
    #for assignment, point in zip(assignments, dataset):
        #clustering[assignment].append(point)
    return assignments


def k_means(dataset, k):
    # step 1: generate k points
    # step 2: do converge
    """
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
    """
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k(dataset, k)
    tempAssignments = _do_lloyds_algo(dataset, k_points)
    clustering = defaultdict(list)
    for assignment, point in zip(tempAssignments, dataset):
        tempPoint = []
        for i in range(len(point)):
            tempPoint.append(point[i])
        #tempPoint.append(point[0])
        #tempPoint.append(point[1])
        clustering[assignment].append(tempPoint)
    return clustering


def k_means_pp(dataset, k):
    # step 1: generate k points
    # step 2: do converge
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    tempAssignments = _do_lloyds_algo(dataset, k_points)
    clustering = defaultdict(list)
    for assignment, point in zip(tempAssignments, dataset):
        tempPoint = []
        for i in range(len(point)):
            tempPoint.append(point[i])
        #tempPoint.append(point[0])
        #tempPoint.append(point[1])
        clustering[assignment].append(tempPoint)
    return clustering
    #return _do_lloyds_algo(dataset, k_points)


# helper function 1: convert array to list
def convertArrayToList(dataset):
    outList = []
    for i in range(len(dataset)):
        tempList = []
        for j in range(len(dataset[0])):
            tempList.append(dataset[i][j])
        outList.append(tempList)
    return outList


#end
