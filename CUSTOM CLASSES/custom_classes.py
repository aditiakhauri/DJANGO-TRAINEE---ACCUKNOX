class Rectangle:
    def __init__(self):
        
        self._length = self._get_positive_integer("Enter the length of the rectangle: ")
        self._width = self._get_positive_integer("Enter the width of the rectangle: ")

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def __iter__(self):
        
        return RectangleIterator(self)

    def __repr__(self):
        return f"Rectangle(length={self._length}, width={self._width})"

    @staticmethod
    def _get_positive_integer(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    raise ValueError("The value must be a positive integer.")
                return value
            except ValueError as e:
                print(e)


class RectangleIterator:
    def __init__(self, rectangle):
        self.rectangle = rectangle
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            self.index += 1
            return {'length': self.rectangle.length}
        elif self.index == 1:
            self.index += 1
            return {'width': self.rectangle.width}
        else:
            raise StopIteration


rectangle = Rectangle()


print(rectangle)


for attribute in rectangle:
    print(attribute)
