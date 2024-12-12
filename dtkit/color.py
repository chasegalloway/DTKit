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

    def __repr__(self):
        return f"Color(RGB={self.red}, {self.green}, {self.blue})"
