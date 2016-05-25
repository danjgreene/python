def multiples(limit):
	sum_ = 0
	num = 1
	for num in range(limit):
		if num % 3 == 0 or num % 5 == 0:
			sum_ += num
		num += 1
	return sum_


print multiples(10)

