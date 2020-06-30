def sec_smallest(numbers):
	num_max, num_min = float("inf"), float("inf")
	for x in numbers:
		if x < num_min:
			num_max = num_min
			num_min = x
		elif x < num_max and x > num_min:
			num_max = x

	return num_max

print('Sec_smallest:', sec_smallest([1, 2, -8, -8, -2, 0]))