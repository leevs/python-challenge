print "Let's practice everything."
print 'You \'d need to know \' bout escapes with \\ that do \n newlines and \t tabls.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\t where there is none.
"""

print "-------------"
print poem
print "-------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s " % five

def secret_formula(started):
  beans = started * 500
  jars = beans / 1000
  crates = jars / 100
  return beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
