def get_squares():
    """Return a list of square numbers."""
    return [x**2 for x in range(50_000_000)]

def get_sum(squares):
    """Return the sum of all squares."""
    sum = 0
    for square in squares:
        sum += square

    return sum

squares = get_squares()
sum = get_sum(squares)
print(f"Sum: {sum:,}")