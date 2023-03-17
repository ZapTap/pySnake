from operator import sub, mul
from functools import reduce

def sum_tuple(t1, t2):
	return tuple(reduce(sub, i) for i in zip(t1, t2))

def mul_tuple(t1, t2):
	return (reduce(mul, i) for i in zip(t1, t2))

print(*mul_tuple((0,1), (1, 0)))
print(mul_tuple((7,1), (3, 0)))
print(mul_tuple((453,1), (1, 0)))
print(mul_tuple((0,1), (1, 23456)))