class Color:
    def __init__(self, red, green, blue):
        self.red = self._clamp(red)
        self.green = self._clamp(green)
        self.blue = self._clamp(blue)

    @staticmethod
    def _clamp(value):
        if not (0 <= value <= 255):
            raise ValueError("Color values must be between 0 and 255")
        return int(value)

    def to_hex(self):
        return f"#{self.red:02x}{self.green:02x}{self.blue:02x}".upper()

    @staticmethod
    def from_hex(hex_color):
        if hex_color.startswith("#"):
            hex_color = hex_color[1:]
        if len(hex_color) != 6:
            raise ValueError("HEXcode must be 6 characters long")
        red = int(hex_color[0:2], 16)
        green = int(hex_color[2:4], 16)
        blue = int(hex_color[4:6], 16)
        return Color(red, green, blue)

    def to_hsl(self):
        r, g, b = self.red / 255, self.green / 255, self.blue / 255
        max_color, min_color = max(r, g, b), min(r, g, b)
        delta = max_color - min_color
        lightness = (max_color + min_color) / 2

        if delta == 0:
            hue = saturation = 0
        else:
            saturation = delta / (1 - abs(2 * lightness - 1))
            if max_color == r:
                hue = ((g - b) / delta) % 6
            elif max_color == g:
                hue = (b - r) / delta + 2
            elif max_color == b:
                hue = (r - g) / delta + 4
            hue *= 60
        return round(hue, 2), round(saturation * 100, 2), round(lightness * 100, 2)

    @staticmethod
    def range(start_color, end_color, steps):
        if not isinstance(start_color, Color) or not isinstance(end_color, Color):
            raise TypeError("start_color and end_color must be instances of Color")

        if steps < 2:
            raise ValueError("There must be at least 2 steps to create a range")

        color_range = []
        for i in range(steps):
            ratio = i / (steps - 1)
            r = round(start_color.red * (1 - ratio) + end_color.red * ratio)
            g = round(start_color.green * (1 - ratio) + end_color.green * ratio)
            b = round(start_color.blue * (1 - ratio) + end_color.blue * ratio)
            color_range.append(Color(r, g, b))
        return color_range

    def blend(self, other, ratio=0.5):
        if not isinstance(other, Color):
            raise TypeError("Can only blend with another Color")
        r = round(self.red * (1 - ratio) + other.red * ratio)
        g = round(self.green * (1 - ratio) + other.green * ratio)
        b = round(self.blue * (1 - ratio) + other.blue * ratio)
        return Color(r, g, b)

    def invert(self):
        return Color(255 - self.red, 255 - self.green, 255 - self.blue)

    def brightness(self):
        return round((0.299 * self.red + 0.587 * self.green + 0.114 * self.blue), 2)
    
    def __repr__(self):
        return f"rgb({self.red}, {self.green}, {self.blue})"
