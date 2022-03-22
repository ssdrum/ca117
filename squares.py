#!/usr/bin/env python3

#def even_squares(numbers):
    #squares = []
    #for n in numbers:
        #if n % 2 == 0:
            #squares.append(n * n)
    #return squares

def even_squares_odd_cubes(numbers):
    squares_n_cubes = [n * n if n % 2 == 0for n in numbers ]
    return squares_n_cubes

print(even_squares_odd_cubes([1,2,3,4,5]))
