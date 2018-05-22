class Rectangle:
    """ Rectangle class
    """

    def __init__(self, lower_left, width, height):
        """Init of Rectangle object

        Args:
            lower_left: Lower left point of rectangle 
            width: Width of rectangle
            height: Height of rectangle
        """
        assert isinstance(lower_left, tuple)
        assert len(lower_left) == 2
        assert lower_left[0] >= 0
        assert lower_left[1] >= 0
        self.lower_left = lower_left
        assert isinstance(height, int)
        assert height > 0
        self.height = height
        assert isinstance(width, int)
        assert width > 0
        self.width = width

    def __repr__(self):
        """String representation of rectangle
        """
        return "Lower left coordinate: %s \nWidth: %s \nHeight: %s\n" % (self.lower_left, self.width, self.height)

    def __eq__(self, other):
        """Rectangles are equal if lower left coordinate, width, and height are the same
        """
        assert isinstance(other, Rectangle)
        if self.lower_left == other.lower_left:
            if self.height == other.height:
                if self.width == other.width:
                    return True
        return False

    def __lt__(self,other):
        """Returns true if the rectangle's left border is to the left of the other rectangle's left border
        """
        assert isinstance(other, Rectangle)
        return self.lower_left[0] < other.lower_left[0]

    def __gt__(self,other):
        """Returns true if the rectangle's right border is to the right of the other rectangle's right border
        """
        assert isinstance(other, Rectangle)
        return self.lower_left[0] + self.width > other.lower_left[0] + other.width

    def __le__(self,other):
        """Returns true if the rectangle's lower border is lower than the other rectangle's lower border
        """
        assert isinstance(other, Rectangle)
        return self.lower_left[1] < other.lower_left[1]

    def __ge__(self,other):
        """Returns true if the rectangle's upper border is higher than the other rectangle's upper border
        """
        assert isinstance(other, Rectangle)
        return self.lower_left[1] + self.height > other.lower_left[1] + other.height


    def overlap(self,other):
        """Returns true if the two rectangles are overlapping each other
        """
        assert isinstance(other, Rectangle)
        if ((self.lower_left[0]+self.width) <= other.lower_left[0]) or (self.lower_left[0] >= (other.lower_left[0]+other.width)) or (self.lower_left[1] >= (other.lower_left[1]+other.height)) or ((self.lower_left[1]+self.height) <= other.lower_left[1]):
            return False
        return True