def gcd(x, y):
	start_num = 0
	if x < y:
		start_num = x
	else:
		start_num = y

	while start_num > 1:
		if ((x % start_num == 0) and (y % start_num == 0)):
			return start_num

		start_num -= 1
	return 1

print(gcd(160, 180))