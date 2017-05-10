# Assigning variable with four string formatters
formatter = "%r %r %r %r"
# Printing numbers 1-4 on the assigned formatter places
print formatter % (1, 2, 3, 4)
# Printing strings on the assigned formatter places
print formatter % ("one", "two", "three", "four")
# Printing boolean values on the assigned formatter places
print formatter % (True, False, False, True)
# Printing the string value of variable formatter
print formatter % (formatter, formatter, formatter, formatter)
# Printing string values on the assigned formatter places
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
