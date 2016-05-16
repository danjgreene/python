# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

def round(number):
	"""
	>>> round(3.14159)
	3
	>>> round(27.63)
	28
	>>> round(3.5)
	4
	"""
	new_number = str(number + 0.5)
	return int(new_number[0:new_number.find('.')])

#assert round(3.14159) == 3
#assert round(27.63) == 28
#assert round(3.5) == 4
#assert round(28.878787) == 29
# print round(float(raw_input("Enter a number:")))

if __name__ == "__main__":
	import doctest
	doctest.testmod()

#ENTER CODE BELOW HERE















