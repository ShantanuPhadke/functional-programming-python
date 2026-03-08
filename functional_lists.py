from __future__ import annotations
from dataclasses import dataclass
from typing import Union, Callable, Any

@dataclass
class Nil:
    pass

@dataclass
class Cons:
    head: int
    tail: Union[Cons, Nil]


FunctionalList = Union[Cons, Nil]

def sum_list(ints: FunctionalList) -> int:
    match ints:
        case Nil():
            return 0
        case Cons(x, xs):
            return x + sum_list(xs)

# Usage
my_list = Cons(1, Cons(2, Cons(3, Nil())))
assert sum_list(my_list) == 6, "Summing fails!"

def tail(ints: FunctionalList) -> FunctionalList:
    match ints:
        case Nil():
            return None
        case Cons(x, xs):
            return xs

assert tail(my_list) == Cons(2, Cons(3, Nil())), "Tails once fails!"
assert tail(tail(my_list)) == Cons(3, Nil()), "Tails multiple times fails!"
assert tail(tail(tail(my_list))) == Nil(), "Tails on end of the list fails!"

def setHead(ints: FunctionalList, newVal: int) -> FunctionalList:
    match ints:
        case Nil():
            return Cons(newVal, Nil())
        case Cons(x, xs):
            return Cons(newVal, Cons(x, xs))


assert setHead(my_list, 0) == Cons(0, Cons(1, Cons(2, Cons(3, Nil())))), "Failed to setHead on a non-empty List!"
assert setHead(Nil(), 1) == Cons(1, Nil()), "Failed to set head on an empty list!"

# Drops the first n elements of the inputted list
def drop(l: FunctionalList, n: int) -> FunctionalList:
    match n:
        case 0:
            return l
    match l:
        case Nil():
            return None
        case Cons(x, xs):
            return drop(xs, n-1)

assert drop(my_list, 2) == Cons(3, Nil())

# Drops the elements in a list if they meet some criteria
def dropWhile(l: FunctionalList, f: Callable[[int], bool]):
    match l:
        case Nil():
            return l
        case Cons(x, xs):
            match f(x):
                case True:
                    return dropWhile(xs, f)
                case False:
                    return l

assert dropWhile(my_list, lambda a: a < 2) == Cons(2, Cons(3, Nil())), "DropWhile is failing!"

# Return a list with all elements but the last of the inputted list
# Cons(1, Cons(2, Cons(3, Cons(4, Nil())))) -> x = 1, y = 2, xs = Cons(3, Cons(4, Nil()))
# Cons(2, Cons(3, Cons(4, Nil()))) -> x = 2, y = 3, xs = Cons(4, Nil())
# Cons(3, Cons(4, Nil())) -> x = 3, y = 4, xs = Nil() -> return 3
def init(l: FunctionalList) -> FunctionalList:
    match l:
        case Nil():
            return l
        case Cons(x, Cons(y, xs)):
            match xs:
                case Nil():
                    return Cons(x, Nil())
                case Cons(b, bs):
                    return Cons(x, init(Cons(y, xs)))

assert init(Cons(1, Cons(2, Cons(3, Cons(4, Nil()))))) == Cons(1, Cons(2, Cons(3, Nil()))), "Failed to get rid of the last element!"


# Note from Exercise 3.10: This version has non tail position recursive calls, meaning that
# there is additional work to be done even once the call returns. This results in StackOverflow
# errors for very large inputs, which, in our case, are very large lists.
def foldRight(l: FunctionalList, z: Any, f: Callable[[int, Any], Any], short_circuiting_value = None) -> Any:
    match l:
        case Nil():
            return z
        case Cons(x, xs):
            if short_circuiting_value and x == short_circuiting_value:
                return short_circuiting_value
            return f(x, foldRight(xs, z, f))

# Some sample functions for testing out foldRight from above
def sum2(ns: FunctionalList) -> Any:
    return foldRight(ns, 0, lambda x, y: x + y)

def product2(ns: FunctionalList) -> Any:
    return foldRight(ns, 1.0, lambda x,y: x * y)

my_sample_functional_list = Cons(0, Cons(1, Cons(2, Cons(3, Nil()))))
assert sum2(my_sample_functional_list) == 6
assert product2(my_sample_functional_list) == 0

# Exercise 3.7
def product_short_circuiting(ns: FunctionalList) -> Any:
    return foldRight(ns, 1.0, lambda x,y: x * y, short_circuiting_value=0)
assert product_short_circuiting(my_sample_functional_list) == 0

# Exercise 3.9
def length(ns:FunctionalList) -> int:
    return foldRight(ns, 0, lambda _,y: y+1)
assert length(my_sample_functional_list) == 4

# Exercise 3.10 - a tail position recursive call version to handle very large inputs.
def foldLeft(l: FunctionalList, z: Any, f: Callable[[int, Any], Any]) -> Any:
    match l:
        case Nil(): return z
        case Cons(x, xs):
            return foldLeft(xs, f(x, z), f)

def sum2Efficient(ns: FunctionalList) -> Any:
    return foldLeft(ns, 0, lambda x, y: x + y)

assert sum2Efficient(my_sample_functional_list) == 6

def lengthEfficient(ns:FunctionalList) -> int:
    return foldLeft(ns, 0, lambda _,y: y+1)

assert lengthEfficient(my_sample_functional_list) == 4