from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you want to do that, hit RETURN key"

raw_input("?")

print "Opening the file %r " % filename
target = open(filename, 'w')

print "Trucating the file, it's going to be empty"
target.truncate()

print "Now I,m going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these lines to the file."
print "This is an overview of your lines:"
print "%s\n%s\n%s" % (line1, line2, line3)

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close the file."
target.close()
