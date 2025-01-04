class Rectangle:
    def __init__(self):
        self.length = int(input("Enter the length: "))
        self.width = int(input("Enter the width: "))

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

rectangle = Rectangle()
print("\nIterating over the Rectangle:")
for dimension in rectangle:
    print(dimension)