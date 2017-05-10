# Defining x with string value
x = "There are %d types of people." % 10
# Binary variable gets string value with same name
binary = "binary"
# Putting string value to "don't"
do_not = "don't"
# Defining value of y variable using formatters
y = "Those who know %s and those who %s." % (binary, do_not)
# Printing value of x
print x
# Printing value of y
print y
# Printing value of x using formatters
print "I said: %r." % x
# Printing value of y using formatters
print "I also said: '%s'." % y
# Boolean with value False
hilarious = False
# Variable joke_evaluation gets string value
joke_evaluation = "Isn't that joke so funny?! %r"
# Printing mod of two previous variables
print joke_evaluation % hilarious
# Putting string value to w and e variables
w = "This is the left side of..."
e = "a string with a right side."
# Printing them one after another
print w + e
