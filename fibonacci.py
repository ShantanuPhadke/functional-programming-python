def fib(n: int) -> int:
	def go(num: int, acc1: int, acc2: int) -> int:
		if num >= n:
			return acc2
		else:
			return go(num+1, acc2, acc1+acc2)
	return go(2, 0, 1)

# fib(6) => go(2, 0, 1) => go(3, 1, 1) => go(4, 1, 2)


if __name__ == "__main__":
    # This code only runs if the file is executed directly
    print('1st Fib = ' + str(fib(1)))
    print('6th Fib = ' + str(fib(6)))
    print('7th Fib = ' + str(fib(7)))