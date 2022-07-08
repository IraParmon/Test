from math import pi

#def is_correct(r):
  #  if r <0:
  #      raise Exception("Радиус круга < 0")
def get_square(r):
    if r <= 0:
        raise Exception("Радиус круга < 0")
    else:
        return pi * (r **2)

