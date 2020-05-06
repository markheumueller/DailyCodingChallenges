
def is_palindrome(number: int) -> bool:
	tmp = number
	rev = 0
	while (number > 0):
	    dig = number % 10
	    rev = rev * 10 + dig
	    number = number // 10
	return tmp == rev

def to_binary_int(number: int) -> int:
	return int('{0:b}'.format(number))

def double_base_palindrome(number: int) -> (bool, int, int):
	binary_int = to_binary_int(number)
	return is_palindrome(number) and is_palindrome(binary_int), number, binary_int

if __name__ == '__main__':
	sum = 0
	for x in range(1000000):
		double, number, binary = double_base_palindrome(x)
		if double:
			sum += number
	print('Sum: {}'.format(sum))
