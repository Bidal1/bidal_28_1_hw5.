ten = list(map(lambda x: x, range(1, 11)))
print(ten)
ten = list(range(1, 11))
evens = list(map(lambda x: x*2, filter(lambda x: x%2==0, ten)))
print(evens)
ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
squares = list(map(lambda x: x ** 2, evens))
print(squares)