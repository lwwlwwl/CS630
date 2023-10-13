def weighted_median(coords, weights):
  # sort the coordinates and weights by the coordinates
  sorted_coords_weights = sorted(zip(coords, weights), key=lambda x: x[0])
  coords, weights = zip(*sorted_coords_weights)

  # calculate the cumulative weights
  weight_sum = 0
  for x in weights:
    weight_sum += x
    if weight_sum >= 0.5:
      return coords[weights.index(x)]
  # if the cumulative weights never reach 0.5, return the last coordinate
  # this should never happen in this problem
  return coords[-1]

def best_position(points, weights):
  '''
  points: List of tuples, each tuple contains two float elements corresponds to the x and y location of a point.
  weights: List of floats.

  Return: a tuple (x,y) that represents the location of the point that minimizes the weighted distance sum.
  '''
  if len(points) != len(weights):
    raise ValueError("The length of points and weights must be the same.")
  
  x_coords = [point[0] for point in points]
  y_coords = [point[1] for point in points]
  # let x be the weighted median of x_coords
  x = weighted_median(x_coords, weights)
  y = weighted_median(y_coords, weights)
  return (x,y)
