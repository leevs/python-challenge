#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r\narg2: %r" % (arg1, arg2)

#is *args actually needed ? we can jsut do it like this
def print_two_better(arg1, arg2):
    print "arg1: %r\narg2: %r" % (arg1, arg2)

#This just take one argument
def print_one(arg1):
    print "arg1: %r" % (arg1)

# this one take no arguments
def print_none():
    print "I got nothin."

print "\nFirst fuction:"
print_two("First","Second")

print "\nSecond function:"
print_two_better("1st", "2nd")

print "\nThird fucntion:"
print_one("1")

print "\nFourth function:"
print_none()
