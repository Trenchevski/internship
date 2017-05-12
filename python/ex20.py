from sys import argv

script, input_file = argv
# Defining a function that prints all content of file
def print_all(f):
    print f.read()
# Positioning back at the start of file using seek
def rewind(f):
    f.seek(0)
# Defining a function that prints only one line
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line+=1
print_a_line(current_line, current_file)

current_line+=1
print_a_line(current_line, current_file)

current_line+=1
print_a_line(current_line, current_file)
