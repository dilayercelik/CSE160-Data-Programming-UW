# Practice


# This problem will only make sense after reading the HW3 writeup.
# Return the sum of all the values in the given pixel_grid.
# The pixel_grid will always contain at least one value.

# Examples:
## sum_grid([[5, 2, 3], [1, 5, 4]]) → 20
## sum_grid([[1, 3], [3, 4], [15, 16], [9, 2]]) → 53
## sum_grid([[100, 50]]) → 150


# Answer

def sum_grid(pixel_grid):

    sum_all = 0

    for row in pixel_grid:
        for indv_pixel in row:
            sum_all += indv_pixel

    return sum_all


# Tests
print(sum_grid([[5, 2, 3], [1, 5, 4]]))               # correct output
print(sum_grid([[1, 3], [3, 4], [15, 16], [9, 2]]))   # correct output
print(sum_grid([[100, 50]]))                          # correct output
