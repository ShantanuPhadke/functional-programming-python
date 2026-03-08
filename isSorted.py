from typing import Callable

def isSorted(a: list[int], ordered: Callable[[int, int], bool]) -> bool:
	def loop(index: int) -> bool:
		if index >= len(a)-1:
			return True
		elif not ordered(a[index], a[index+1]):
			return False
		else:
			return loop(index+1)
	return loop(0)

def isOrdered(elem1: int, elem2: int) -> bool:
	return elem2 >= elem1

if __name__ == "__main__":
	a = [1,2,3,4]
	b = [4,3,2,1]

	print("Is [1,2,3,4] sorted? " + str(isSorted(a, isOrdered)))
	print("Is [4,3,2,1] sorted? " + str(isSorted(b, isOrdered)))