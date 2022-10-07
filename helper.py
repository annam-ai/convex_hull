from Point import Point
import random

def distance_sq(point1, point2):
  return (point1.x - point2.x)**2 + (point1.y - point2.y)**2


def cross_product(point1, point2):
  return point1.x * point2.y - point2.x * point1.y


def direction(point1, point2, point3):
  direction = cross_product(point3.subtract(point1), point2.subtract(point1))
  return direction


def generate_random_points(smallest_number=0, biggest_number=300, amount=50):
  list_of_points = []

  for i in range(amount):
    list_of_points.append(
      Point(random.randint(smallest_number, biggest_number),
            random.randint(smallest_number, biggest_number)))

  return list_of_points


def calculate_distance(p1, p2, p3):
  return abs(direction(p1, p2, p3))