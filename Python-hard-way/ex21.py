def add(a, b):
  print "Adding %d + %d" % (a, b)
  return a + b

def substract(a, b):
  print "Subsctracting %d - %d" % (a, b)
  return a - b

def multiply(a, b):
  print "Multiply %d * %d" % (a, b)
  return a * b

def divide(a, b):
  print "Divide %d / %d" % (a, b)
  return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide (200, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d," % (age, height, weight, iq)

# A puzzle for the exta credit, type it anyway.

print "Here is a puzzle"

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand ?"

#180 * 50 = 500 + 400 = 900
#74 - 900 = -826
#35 + -826 = -791
