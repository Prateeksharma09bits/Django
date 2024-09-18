class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rectangle = Rectangle(5, 10)

# Iterating over the rectangle
for attribute in rectangle:
    print(attribute)

# Output:
# {'length': 5}
# {'width': 10}
