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
    def _init_(self, start=100):
        """
        start the serial generator with a start value of 100.
        """
        self.start = start
        self.current = start

    def __repr__(self):
        """
        Provide a string representation of the SerialGenerator instance.
        
        Returns:
            str: A string representation of the instance.
        """
        return f"SerialGenerator(start={self.start}, current={self.current})"


    def generate(self):
        """generating the next serial number."""
        current_serial = self.current
        self.current += 1
        return current_serial
    
    def reset(self):
        """reset the serial number to the original start value."""
        self.current = self.start

