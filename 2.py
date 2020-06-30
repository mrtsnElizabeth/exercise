def sec_smallest(numbers):
    """
    :param numbers: list[int]
    :return: int    
    """
    
    int1, int = float('inf'), float('inf')
    for x in numbers:
    	# if x <= int1:
    	# 	int1, int = x, int1
    	if x < int:
    		int = x


    # int1, int = numbers[:2]
    # if int<int1: int1, int = int, int1

    # for x in numbers[2:]:
    #     if x <= int1:
    #         int1, int = x, int1
    #     elif x < int:
    #         int = x
    return int

print('Sec_smallest:', sec_smallest([1, 2, -8, -8, -2, 0]))