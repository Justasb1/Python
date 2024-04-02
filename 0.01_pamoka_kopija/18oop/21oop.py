def rgb_to_hex(r, g, b):
    return '#{0:02X}{1:02X}{2:02X}'.format(r, g, b)

class Colors:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def toHex(self):
        return rgb_to_hex(self.red, self.green, self.blue)

class ColorsAlpha(Colors):
    def __init__(self, red, green, blue, alpha):
        super().__init__(red, green, blue)
        self.alpha = alpha
        
    def alphaToHex(self):
        return '{:02X}'.format(int(self.alpha * 255))

    def toHexAlpha(self):
        return f'{self.toHex()} {self.alphaToHex()}'

    def display(self):
         return self.toHexAlpha()

# (0.2 * 255) --> hexadecimal
grayA = ColorsAlpha(128, 127, 126, 0.2)
print(grayA.display())  # Output: #807F7E 33
