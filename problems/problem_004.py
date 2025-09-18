# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# Inputs: three values
# Outputs:
# max value among three
# if two values are same, return either val
# if three vals are same, return any val


def max_of_three(value1, value2, value3):
    if value1 == value2 and value2 == value3:
        return value1
    elif value1 == value2 or value1 == value3:
        return value1
    elif value2 == value3:
        return value2
    else:
        return max(value1, value2, value3)


# Sample Inputs:
value1 = 1
value2 = 2
value3 = 3

value1_two_same = 4
value2_two_same = 4
value3_two_same = 5

value1_three_same = 6
value2_three_same = 6
value3_three_same = 6

# Function Invocation:
result_max = max_of_three(value1, value2, value3)
print(f"result_max: {result_max}")

result_two_same = max_of_three(value1_two_same, value2_two_same, value3_two_same)
print(f"result_two_same: {result_two_same}")

result_three_same = max_of_three(
    value1_three_same, value2_three_same, value3_three_same
)
print(f"result_three_same: {result_three_same}")
