# Convex Hull

The convex hull is the smallest polygon that contains all points in a 2d area. 
The calculation of the convex hull is not trivial and there are several different approaches.

Our group chose **Gift Wrapping** (or **Jarvis' March**) and **QuickHull**. 

## Group 14 | A
| Name | ID |
|:----| :--: |
| Anna Majewski | ai22m049 |
| Christina Sturath | ai22m032 |


## Usage 
Basic Usage: simple mode with 10000 randomly generated numbers between -5000 and 5000.
```py
python3 main.py
```
Arguments
```sh
usage: Convex Hull [-h] [-f FILE] [-m MODE] [-r RANDOM [RANDOM ...]]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Choose a text file, first line amount of numbers, comma
                        separated float pairs on all other lines
  -m MODE, --mode MODE  Choose between 'interactive' and 'simple', default: simple
  -r RANDOM [RANDOM ...], --random RANDOM [RANDOM ...]
                        Generate random points: n max min [default: 100 1000 0]
```
Example output for simple mode:
```
Calculating 10000 numbers between -2000 and 2000. This may take a while.
Number generation: 0.087 seconds.
Calculating the convex hull of 10000 points.
QuickHull: 0.383 seconds. 20 points are on the hull.
Gift Wrapping: 1.591 seconds. 21 points are on the hull.
```

In interactive mode the hull is created via the user's mouse click.