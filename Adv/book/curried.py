def curried_power(a):
  def h(b):
    return pow(b, a)
  return h

def map_to_range(start, end, f):
  while start < end:
    r = f(start)
    print(r)
    start += 1


