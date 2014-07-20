# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxVertical(self, points):
        dic = {}
        for i in points:
            if i.x not in dic:
                dic[i.x] = 1
            else:
                dic[i.x] += 1
        if dic == {}:
            return 0
        else:
            return max(dic.values())
    
    def slope_intercept(self, p, q):
            slope = float(p.y-q.y)/(p.x-q.x)
            intercept = p.y - p.x * slope
            return (slope, intercept)
            
    def point_on_line(self, line, point):
        if point.x == 0:
            return point.y == line[0]
        else:
            return line[0] == float(point.y-line[1])/(point.x-0)    
        
    def maxPoints(self, points):
        maximum = self.maxVertical(points)
        lines = []
        for i in range(len(points)-1):
            for j in points[i:]:
                if points[i].x != j.x:
                    if self.slope_intercept(points[i], j) not in lines: lines.append(self.slope_intercept(points[i], j))
        for line in lines:
            counter = 0
            for point in points:
                if self.point_on_line(line,point):
                    counter += 1
            if counter > maximum: maximum = counter
        return maximum             