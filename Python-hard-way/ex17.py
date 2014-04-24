from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s " % (from_file, to_file)

# we could do theese two on one line too , but how ?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file even exist ? %r" % exists(to_file)
raw_input("Ready ? Hit the RETURN key to continue, otherwise CTRL-C to abort")

out_file = open(to_file, 'w')
out_file.write(indata)

print "alright we are done and ready to close everything"

out_file.close()
in_file.close()
