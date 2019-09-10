class Rectangle:

    # Construct self with center (x, y), width w, and height h.
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._width = w
        self._height = h

    # Return the area of self.
    def area(self):
        return self._width * self._height

    # Return the perimeter of self.
    def perimeter(self):
        return [[self._x - self._width / 2, self._y + self._height / 2], # top left
                [self._x + self._width / 2, self._y + self._height / 2], # top right
                [self._x - self._width / 2, self._y - self._height / 2], # bottom left
                [self._x + self._width / 2, self._y - self._height / 2]] # bottom right

    # Return True if self intersects other, and False otherwise.
    def intersects(self, other):
        perimeterSelf = self.perimeter()
        perimeterOther = other.perimeter()

        # Left side
        if perimeterSelf[0][0] <= perimeterOther[0][0] and perimeterOther[0][0] <= perimeterSelf[1][0] and \
                (perimeterSelf[0][1] <= perimeterOther[0][1] and perimeterOther[2][1] <= perimeterSelf[0][1] or \
                        perimeterOther[2][1] <= perimeterSelf[2][1] and perimeterSelf[2][1] <= perimeterOther[0][1]):
            return True

        # Right side

        # Top side

        # Bottom side

        # # Top left of other is inside self
        # if perimeterSelf[0][0] <= perimeterOther[0][0] and perimeterOther[0][0] <= perimeterSelf[1][0] and \
        #         perimeterSelf[2][1] <= perimeterOther[0][1] and perimeterOther[0][1] <= perimeterSelf[0][1]:
        #     return True
        # # Top right of other is inside self
        # elif perimeterSelf[0][0] <= perimeterOther[1][0] and perimeterOther[1][0] <= perimeterSelf[1][0] and \
        #         perimeterSelf[2][1] <= perimeterOther[1][1] and perimeterOther[1][1] <= perimeterSelf[0][1]:
        #     return True
        # # Bottom left of other is inside self
        # elif perimeterSelf[0][0] <= perimeterOther[2][0] and perimeterOther[2][0] <= perimeterSelf[1][0] and \
        #         perimeterSelf[2][1] <= perimeterOther[2][1] and perimeterOther[2][1] <= perimeterSelf[0][1]:
        #     return True
        # # Bottom right of other is inside self
        # elif perimeterSelf[0][0] <= perimeterOther[3][0] and perimeterOther[3][0] <= perimeterSelf[1][0] and \
        #         perimeterSelf[2][1] <= perimeterOther[3][1] and perimeterOther[3][1] <= perimeterSelf[0][1]:
        #     return True
        # # No corners of other is inside self, but two sides intersect
        # elif perimeterSelf[0][0] <= perimeterOther[0][0] and perimeterOther[1][0] <= perimeterSelf[1][0] and \
        #         perimeterSelf[0][1] <= perimeterOther[0][1] and perimeterOther[2][1] <= perimeterSelf[0][1]:
        #     return True
        else:
            return False

    # Return True if other is completely inside of self, and False
    # otherwise.
    def contains(self, other):
        perimeterSelf = self.perimeter()
        perimeterOther = other.perimeter()

        # Top left of other is inside self
        if not(perimeterSelf[0][0] <= perimeterOther[0][0] and perimeterOther[0][0] <= perimeterSelf[1][0] and \
                perimeterSelf[2][1] <= perimeterOther[0][1] and perimeterOther[0][1] <= perimeterSelf[0][1]):
            return False
        # Top right of other is inside self
        elif not(perimeterSelf[0][0] <= perimeterOther[1][0] and perimeterOther[1][0] <= perimeterSelf[1][0] and \
                perimeterSelf[2][1] <= perimeterOther[1][1] and perimeterOther[1][1] <= perimeterSelf[0][1]):
            return False
        # Bottom left of other is inside self
        elif not(perimeterSelf[0][0] <= perimeterOther[2][0] and perimeterOther[2][0] <= perimeterSelf[1][0] and \
                perimeterSelf[2][1] <= perimeterOther[2][1] and perimeterOther[2][1] <= perimeterSelf[0][1]):
            return False
        # Bottom right of other is inside self
        elif not(perimeterSelf[0][0] <= perimeterOther[3][0] and perimeterOther[3][0] <= perimeterSelf[1][0] and \
                perimeterSelf[2][1] <= perimeterOther[3][1] and perimeterOther[3][1] <= perimeterSelf[0][1]):
            return False
        else:
            return True

    # # Draw self on stddraw.
    # def draw(self):
    #     ...