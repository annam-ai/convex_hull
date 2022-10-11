from Point import Point
import random
from timeit import default_timer as timer


def cross_product(point1, point2):
  return point1.x * point2.y - point2.x * point1.y


def direction(point1, point2, point3):
  direction = cross_product(point3.subtract(point1), point2.subtract(point1))
  return direction


def generate_random_points(min=0, max=300, amount=50):
  list_of_points = []
  print(f"Calculating {amount} numbers between {min} and {max}. This may take a while.")
  start = timer()
  for i in range(amount):
    list_of_points.append(
      Point(random.randint(min, max),
            random.randint(min, max)))
  end = timer()
  print(f"Number generation: {round(end - start, 3)} seconds.")
  return list_of_points


def calculate_distance(point1, point2, point3):
  return abs(direction(point1, point2, point3))


def read_file(file):
  point_list = []
  with open(file, 'r') as f:
    for index, line in enumerate(f.readlines()):
      if index != 0:
        x, y = line.split(',')
        x, y = float(x), float(y)
        point_list.append(Point(x, y))
  return point_list

def handle_random_arg(argument_list):
  min = 0
  max = 1000
  n = 100
  argument_length = len(argument_list)
  if argument_length == 1:
    n = int(args.random[0])
  if argument_length == 2:
    n, max = [int(value) for value in args.random]
  if argument_length == 3:
    n, min, max = [int(value) for value in args.random]
  if argument_length > 3:
    exit("Too many values provided, a max of 3 values is allowed: n max min")
  
  list_of_points = generate_random_points(amount=n, min=min, max=max)
  
  return list_of_points
