# Practice

# This problem will only make sense after reading the HW3 writeup.
# Return the value of the pixel on the last row in the last column of the given pixel_grid.
# The pixel_grid will always contain at least one value.


# Examples:
## get_last_pixel([[5, 2, 3], [1, 5, 4]]) → 4
## get_last_pixel([[1, 3], [3, 4], [15, 16], [9, 2]]) → 2
## get_last_pixel([[100, 50]]) → 50


# Answer

def get_last_pixel(pixel_grid):

    return pixel_grid[-1][-1]


# Tests
print(get_last_pixel([[5, 2, 3], [1, 5, 4]]))              # correct output
print(get_last_pixel([[1, 3], [3, 4], [15, 16], [9, 2]]))  # correct output
print(get_last_pixel([[100, 50]]))                         # correct output
