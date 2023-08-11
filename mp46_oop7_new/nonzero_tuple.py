class NonZeroTuple(tuple):

    def __init__(self, values):
        """Only keep nonzero values."""
        values = [v for v in values if v]
        super().__init__(values)

my_tuple = NonZeroTuple((1, 2, 0, 3, 5, 0))
print(my_tuple)