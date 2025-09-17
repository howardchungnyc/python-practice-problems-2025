# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# Input:
# data type: integers

# Output
# data type: integers

# Examples
# value1 = 2
# value2 = 3

# Conditions (if)

# Iteration (loop)

def minimum_value(value1, value2):
    if value1 == value2:
        return value1
    else:
        return min(value1, value2)

value1 = 2
value2 = 3
value1_two = 1
value2_two = 1

result = minimum_value(value1, value2)
result2 = minimum_value(value1_two, value2_two)
print(f"result is: {result}")
print(f"result2 is: {result2}")
