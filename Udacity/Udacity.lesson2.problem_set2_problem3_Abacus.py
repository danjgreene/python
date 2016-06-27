#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
    #num9 = '|0   0000*****|'
    #num8 = '|00   000*****|'
    #num7 = '|000   00*****|'
    #num6 = '|0000   0*****|'
    #num5 = '|00000   *****|'
    #num4 = '|00000*   ****|'
    #num3 = '|00000**   ***|'
    #num2 = '|00000***   **|'
    #num1 = '|00000****   *|'
    #num0 = '|00000*****   |'
    #pos = len(str(value)) - 1
    ab_row_zero = '|00000*****   |'
    ab_row_nine = '|0   0000*****|'
    new_value = '0'* (10 - len(str(value))) + str(value)
    pos = 0
    while pos < 10:
        row_val = (new_value)[pos]
        print ab_row_zero[:(11 - int(row_val))] + '   ' + ab_row_nine[(14 - int(row_val)):]
        pos += 1
       #highest_factor = len(str(value))
       #Count the number of zeroes to get 10^(len(str(value)) - 1)
       #'|00000*****   |' is 0; |0   0000*****| is nine
       # '0' * abs(x - 4)

###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|