def multiple_3_5(max_range: int) -> int:
	return sum([num for num in range(max_range) if num % 3 == 0 or num % 5 == 0])


if __name__ == '__main__':
	print(multiple_3_5(1000))