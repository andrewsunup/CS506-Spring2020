
def euclidean_dist(x, y):
    """
    Calculate the euclidean distance between x and y
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")

    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2

    return res**(1/2)

def manhattan_dist(x, y):
    """
    Calculate the manhattan distance between x and y
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")

    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])

    return res

def jaccard_dist(x, y):
    """
    Calculate the jaccard distance between x and y
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    x_set = set(x)
    y_set = set(y)
    intersection = len(x_set.intersection(y_set))
    union = len(x_set.union(y_set))
    return 1 - intersection/union

def cosine_sim(x, y):
    """
    Calculate the cosine similarity between x and y
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    dot = 0
    x_magnitude = 0
    y_magnitude = 0
    for i in range(len(x)):
        dot += x[i] * y[i]
        x_magnitude += x[i]**2
        y_magnitude += y[i]**2
    x_magnitude = x_magnitude**(1/2)
    y_magnitude = y_magnitude**(1/2)
    return dot / (x_magnitude * y_magnitude)
