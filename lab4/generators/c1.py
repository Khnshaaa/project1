#Create a generator that generates the squares of numbers up to some number N.
def generate_squares(N):
    for num in range(1, N+1):
        yield num * num 

N = int(input())
square_gen = generate_squares(N)

for square in square_gen:
    print(square)
