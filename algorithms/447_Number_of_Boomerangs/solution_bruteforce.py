class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        def _distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        num_boomerangs = 0
        for idx1, p1 in enumerate(points):
            neighbors = dict()
            for idx2, p2 in enumerate(points):
                d = _distance(p1, p2)
                neighbors[d] = neighbors.get(d, 0) + 1
            for d in neighbors:
                num_boomerangs += neighbors[d] * (neighbors[d] - 1)
        return num_boomerangs
