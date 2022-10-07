from helper import direction, calculate_distance

def quick_hull(points):
    hull = []
    left_most_point = min(points, key=lambda point: point.x)
    right_most_point = max(points, key=lambda point: point.x)
    hull.append(left_most_point)
    hull.append(right_most_point)
    
    S1 = [] # left side
    S2 = [] # right side

    for x in points:
      if (direction(left_most_point, right_most_point, x) < 0):
        S1.append(x)
      if (direction(left_most_point, right_most_point, x) > 0):    
        S2.append(x)
                
    findHull(S1, left_most_point, right_most_point, hull)
    findHull(S2, right_most_point, left_most_point, hull)
    return hull
  
def findHull(Sk, P, Q, hull):
    if(len(Sk) == 0): return hull
    furthestPoint = Sk[0]
    maxDist = 0
  
    for x in Sk:      
        dist = calculate_distance(P, Q, x)
        if(dist > maxDist): 
            maxDist = dist
            furthestPoint = x

    Sk.remove(furthestPoint)
    hull.append(furthestPoint)

    S1 = []
    S2 = []
    
    for x in Sk:
      if direction(P, furthestPoint, x) < 0:
        S1.append(x)
      elif direction(furthestPoint, Q, x) < 0:
        S2.append(x)
    findHull(S1, P, furthestPoint, hull);
    findHull(S2, furthestPoint, Q, hull);