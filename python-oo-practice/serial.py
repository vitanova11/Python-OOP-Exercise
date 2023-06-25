"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.current = start

    def generate(self):
        current_value = self.current
        self.current += 1
        return current_value

    def reset(self):
        self.current = self.start


serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.start)
serial.reset()
print(serial.generate())
