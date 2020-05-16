# Practice

# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).

# Examples:
## missing_char('kitten', 1) → 'ktten'
## missing_char('kitten', 0) → 'itten'
## missing_char('kitten', 4) → 'kittn'


# Answer

def missing_char(str, n):

    new_word = str.replace(str[n], '')

    return new_word

# Tests
print(missing_char('kitten', 1)) # correct output
print(missing_char('kitten', 0)) # correct output
print(missing_char('kitten', 4)) # correct output
