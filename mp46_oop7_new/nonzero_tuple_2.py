class NonZeroTuple(tuple):

    def __new__(cls, *values):
        """Only keep nonzero values."""
        values = [v for v in values if v]
        return super().__new__(cls, values)

my_tuple = NonZeroTuple(1, 2, 0, 3, 5, 0)
print(my_tuple)