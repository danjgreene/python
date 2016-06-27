def count_things(lst):
	"""
	count where string length is two or more and the first
	and last char are same

	lst: list
	return: int

	Sample List:['abc', 'xyz', 'aba', '1221']
	Expected Result: 2
	"""
	for chunk in lst:
		if not isinstance(chunk, str):
			return "Please use strings only"

	hits = 0
	for chunk in lst:
		if len(chunk) >= 2:
			if chunk[0] == chunk[-1]:
				hits += 1
	return hits

print count_things(['abc', 'xyz', 'aba', '1221', 'a'])
