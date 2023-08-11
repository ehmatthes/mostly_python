class NonZeroList(list):

    def __init__(self, values):
        """Only keep nonzero values."""
        values = [v for v in values if v]
        super().__init__(values)

my_list = NonZeroList((1, 2, 0, 3, 5, 0))
print(my_list)

print(type(my_list))
help(my_list)
