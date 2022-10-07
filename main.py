# Convex Hull
from Point import Point
from gift_wrapping import gift_wrapping
from quick_hull import quick_hull
from timeit import default_timer as timer
from helper import generate_random_points

list_of_points = [(0.4, 0.2), (1, 4), (3, 3), (3, 1), (7, 0), (5, 5), (9, 6),
                  (5, 2)]
list_of_points = [Point(x, y) for x, y in list_of_points]

start = timer()
smallest_number=-5000
amount = 1000000
biggest_number = 5000
list_of_points = generate_random_points(smallest_number, biggest_number, amount)
end = timer()
print(f"Generated {amount} random numbers between {smallest_number} and {biggest_number} in {round(end - start, 3)} seconds.")
start = timer()
convex_hull1 = quick_hull(list_of_points)
end = timer()
print(f"Calculated the convex hull with QuickHull in {round(end - start, 3)} seconds. {len(convex_hull1)} points are on the hull.")
start = timer()
convex_hull2 = gift_wrapping(list_of_points)
end = timer()
print(f"Calculated the convex hull with Gift Wrapping in {round(end - start, 3)} seconds. {len(convex_hull2)} points are on the hull.")


print(f"\nQuick Hull: {len(convex_hull1)}")
for point in convex_hull1:
  print(point)

print(f"\n Gift Wrapping: {len(convex_hull2)}")
for point in convex_hull2:
  print(point)