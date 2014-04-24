def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Party !"

print "We can just give the fucntion numbers directly"
cheese_and_crackers(20, 10)

print "Ok but we can use vairables from our script aswell"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do some math inside"
cheese_and_crackers(10 + 20, 50 / 5)

print "And we can combine the two, vairables and some math"
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers * 2)
