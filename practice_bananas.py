
# n + nn + nnn
# 5
# 5 + 55 + 555

def formula(n):
	#print 'n' + ' + ' + 'n' + 'n' + ' + ' + 'n' + 'n' +'n'
	nn = int(str(n) + str(n))
	nnn = int(str(n) + str(n) + str(n))
	return n + nn + nnn
	#return int(str(n)) + (int(str(n) + str(n))) + (int(str(n) + str(n) + str(n)))

print formula(5)