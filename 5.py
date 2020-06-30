def max_sum_index(tuples):
	max_sum = float("-inf")
	index = 0
	tuple_index = 0
	for tpl in tuples:
		x = 0
		for elem_tpl in tpl:
			x += elem_tpl

		if x > max_sum:
			max_sum = x
			index = tuple_index
		tuple_index += 1
	return index

print(max_sum_index([(10, 20), (40, 32), (30, 25)]))