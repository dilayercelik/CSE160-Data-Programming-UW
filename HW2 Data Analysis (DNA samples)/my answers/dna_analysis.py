# Name: Dilay Fidan Ercelik
# CSE 160
# Homework 2: DNA analysis

# This program reads in DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq
#
# For teaching purposes, a few more comments than normal have been added in
# to explain in detail what some Python constructs are doing.

# The sys module supports reading files, command-line arguments, etc.
import sys

# Function to convert the contents of dna_filename into a string of nucleotides
def filename_to_string(dna_filename):
    """
    dna_filename - the name of a file in expected file format
    Expected file format is: Starting with the second line of the file,
    every fourth line contains nucleotides.
    The function will read in all lines from the file containing nucleotides,
    concatenate them all into a single string, and return that string.
    """

    # YOU DO NOT NEED TO MODIFY THIS FUNCTION.

    # Creates a file object from which data can be read.
    inputfile = open(dna_filename)

    # String containing all nucleotides that have been read from the file so far.
    seq = ""

    # The current line number (= the number of lines read so far).
    linenum = 0

    for line in inputfile:
        linenum = linenum + 1
        # if we are on the 2nd, 6th, 10th line...
        if linenum % 4 == 2:
            # Remove the newline characters from the end of the line
            line = line.rstrip()
            # Concatenate this line to the end of the current string
            seq = seq + line
    return seq

# Function to return GC Classification   # Problem 8
def classify(gc_content):
    """
    gc_content - a number representing the GC content
    Returns a string representing GC Classification. Must return one of
    these: "low", "moderate", or "high"
    """
    if gc_content > 0.6:
        classification = 'high GC content'

    elif gc_content < 0.4:
        classification = 'low GC content'

    else:
        classification = 'moderate GC content'

    return classification

###########################################################################
### Main program begins here
###

# Check if the user provided an argument
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)

# Save the 1st argument provided by the user, as a string.
# Note: sys.argv[0] is the name of the program itself (dna_analysis.py)
filename = sys.argv[1]

# Open the file and read in all nucleotides into a single string of letters
nucleotides = filename_to_string(filename)

###
### Compute statistics
###

# YOUR CODE GOES BELOW THIS POINT

# Total nucleotides seen so far.
total_count = 0

# Number of G and C nucleotides seen so far.
# Number of A and T nucleotides seen so far. # Problem 4
gc_count = 0
at_count = 0

for base in nucleotides:
    total_count = total_count + 1

    if base == 'C' or base == 'G':
        gc_count = gc_count + 1

    elif base == 'A' or base == 'T':
        at_count = at_count + 1

gc_content = gc_count / total_count
at_content = at_count / total_count

print('GC-content:', gc_content)
print('AT-content:', at_content)

# Number of A, T, C and G nucleotides: # Problem 5
A_count = 0
T_count = 0
C_count = 0
G_count = 0

for base in nucleotides:
    if base == 'A':
        A_count += 1
    elif base == 'T':
        T_count += 1
    elif base == 'C':
        C_count += 1
    elif base == 'G':
        G_count += 1

print('The number of A nucleotides:', A_count)
print('The number of T nucleotides:', T_count)
print('The number of C nucleotides:', C_count)
print('The number of G nucleotides:', G_count)

# Problem 6:

# 1
sum_counts = A_count + T_count + C_count + G_count
print('The sum of all 4 counts is:', sum_counts)

# 2
print('The total number of nucleotides, total_count, is:', total_count)

# 3
print('The length of the nucleotides string variable is:', len(nucleotides))


# Problem 7

at_gc_ratio = (A_count + T_count) / (C_count + G_count)
print('The AT/GC ratio is:', at_gc_ratio)

# Problem 8 Testing the classify function:

print(classify(gc_content))

# You can add more assertions here to check properties that you think
# should be true about your results. If the condition listed is false,
# then the given message will be printed.
assert total_count == len(nucleotides), "total_count != length of nucleotides"
