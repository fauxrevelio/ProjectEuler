squares = []

def sum_of_square(x):
    for i in range (x):
        sq = (i**2)
        while i < x :
            squares.append(sq)
            break
    return sum(squares)

def square_of_sum(y):
    sum = 0
    for i in range (y):
        sum+=i
    return sum**2

print(square_of_sum(101)-sum_of_square(101))