from typing import Callable

def compose(f: Callable[[int], int], g: Callable[[int], int]) -> Callable[[int], int]:
	def composed_func(a: int) -> int:
		return f(g(a))
	return composed_func

if __name__ == "__main__":
	f = lambda b: b + 3
	g = lambda a: 2 * a
	assert compose(f, g)(2) == 7, "Compose fails!"