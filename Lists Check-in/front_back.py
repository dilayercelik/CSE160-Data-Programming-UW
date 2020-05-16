# Practice


# Given a string, return a new string where the first and last chars have been exchanged.

# Examples:
## front_back('code') → 'eodc'
## front_back('a') → 'a'
## front_back('ab') → 'ba'


# Answer
def front_back(str):

    if len(str) > 1:
        new_string = str[-1] + str[1:-1] + str[0]

    else:
        new_string = str

    return new_string

# Tests
print(front_back('code')) # correct output
print(front_back('a'))    # correct output
print(front_back('ab'))   # correct output
