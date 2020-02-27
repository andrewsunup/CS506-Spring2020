class DBC():
    def __init__(self, dataset, min_pts, epsilon):
            self.dataset = dataset
            self.min_pts = min_pts
            self.epsilon = epsilon

    def get_Neighborhood(self, P):
        Neighborhood = []
        for Pn in range(len(dataset)):
            if sim_sim_distance(self_dataset[P], self.dataset[Pn]):
                Neighborhood.append(Pn)
        return Neighborhood

    def assign_cluster(self, P, PNeighborhood, assignment, assignments):
        assignments[P] = assignment
        while PNeighborhood:
            Pn = PNeighborhood.pop()
            if assignments[Pn] == -1:
                assignments[Pn] = assignment  #?
            if assignments[Pn] == 0:
                assignments[Pn] = assignment
        return assignments

    def dbScan(self):
        assignments = [0 i in range(len(self.dataset))]
        assignment = 0
        for P in range(len(self.dataset)):
            if assignments[P] != 0:
                continue

            PNeighborhood = self.get_Neighborhood(P)

            if len(PNeighborhood) >= self.min_pts:
                # core
                assignment += 1
                assignments = self.assign_cluster(P, PNeighborhood, assignment, assignments)
            else:
                # either border or noise
                assignments[P] = -1

        return assignment
