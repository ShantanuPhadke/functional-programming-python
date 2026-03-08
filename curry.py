from typing import Callable
from functools import partial

def curry(f: Callable[[int, int], int]) -> Callable[[int], [[int], int]]:
	def curried_f(a: int) -> Callable[[int], int]:
		def inner_f(b: int) -> int:
			return f(a,b)
		return inner_f
	return curried_f


def uncurry(f: Callable[[int], Callable[[int], int]]) -> Callable[[int, int], int]:
	def re_curry_f(a: int, b: int) -> int:
		return f(a)(b)
	return re_curry_f


if __name__ == "__main__":
	f = lambda a, b: a * b
	curried_f = curry(f)
	assert curried_f(4)(5) == 20, "Currying fails!"
	assert uncurry(curried_f)(4,5) == 20, "Uncurrying fails!"
