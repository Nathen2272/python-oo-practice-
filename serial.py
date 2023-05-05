class SerialGenerator:
   
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

    def __init__(self, start=0):
        """Make a new generator, starting at start."""

        self.start = self.next = start

    def __repr__(self):
    

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        


