def debug(func):
	def wrapper(*args, **kwargs):
		return_value = func(*args, **kwargs)
		str1 = ""
		str1 += func.__name__
		str1 += "("
		for ind, argument in enumerate(args):
			str1 += str(argument)
			if ind != len(args)-1:
				str1 += ", "
		str1 += ") was called and returned "
		str1 += str(return_value)
		print(str1)
		return return_value

	return wrapper

@debug
def add(a, b, c):
    return a + b + c

add(3, 4, 5)