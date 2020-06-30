def recursive_list_sum(data_list):
	list_sum = 0
	for i in data_list:
		if type(i) is list:
			list_sum += recursive_list_sum(i)
		else:
			list_sum += i
	return list_sum

print('The sum of a list is ', recursive_list_sum([1, 2, [3,4],[5,6], [7, 8, 9]]))