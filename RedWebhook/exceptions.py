class ColourNotInRangeException(Exception):
    """
    A valid color must take an integer value between 0 and 16777216 inclusive
    
    This Exception will be raised when a color is not in that range
    """
    
    def __init__(self, color):
        self.color = color
        
    def __str__(self):
        return repr(
            f'"{self.color}" is not in valid range of colors. The valid ranges of colors are 0 to 16777216 inclusive (INTEGERS) and 0 to FFFFFF inclusive (HEXADECIMAL)'
        )