def reverser(firstname, lastname):
	return firstname[::-1] + " " + lastname[::-1]

# print reverser("Dan", "Greene")

# file[start:stop:increment]
# file = hello_world.java
# ==> java
# file[12::] --> java
# 12 --> Location ONE after the period
# file[1 + location of period::]

def extension(filestring):
	index = 0
	for letter in filestring:
		# CODE GOES HERE
		# print(index, letter)
		if letter == ".":
			final_index = index
		index += 1
	return filestring[1 + final_index::]

		
			
print extension("blank.exe")