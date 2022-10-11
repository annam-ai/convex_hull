from helper import direction

def gift_wrapping(points):
  """
  Calculate the convex hull using the Gift Wrapping Algorithm or
  Jarvis' March. 
  Find the left most point and then each point that is counter-clockwise.
  If the orientation is colinear calculate the farthest point. 
  :param points: list of Point objects
  :return: list of Point objects on Convex Hull
  """
  left_most_point = min(points, key=lambda point: point.x)
  index = points.index(left_most_point)

  left_index = index
  result = []
  result.append(left_most_point)
  while (True):
    next_in_list = (left_index + 1) % len(points)
    for i in range(len(points)):
      if i == left_index:
        continue
      orientation = direction(points[left_index], points[i],
                              points[next_in_list])
      if orientation > 0:
        next_in_list = i
    left_index = next_in_list
    if left_index == index:
      break
    result.append(points[next_in_list])
  return result
