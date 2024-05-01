import random, statistics
from hashlib import md5
from PIL import Image


class IdenticonUtils:
    @staticmethod
    def generate_hash(name: str):
        # Make input case insensitive
        name = name.casefold()
        hash_object = md5(str.encode(name))

        return hash_object.hexdigest()

    @staticmethod
    def get_random_color(hex_string: str) -> tuple[int, int, int, int]:
        # Decrease hex to 6 chars to generate rgb
        hex_string = hex_string[:6]

        r = int(hex_string[:2], 16)
        g = int(hex_string[2:4], 16)
        b = int(hex_string[4:6], 16)

        # If deviation of colors are low, high potential for greyish color
        # Use stdev to recalculate colors to avoid greyish colors
        stdev = statistics.stdev([r, g, b])
        MIN_STDEV = 30
        MULTIPLIER = 100
        if stdev < MIN_STDEV:
            r = random.randint(0, min(r + MULTIPLIER, 255))
            g = random.randint(0, min(g + MULTIPLIER, 255))
            b = random.randint(0, min(b + MULTIPLIER, 255))

        color = (r, g, b, 255)

        return color

    @staticmethod
    def draw_identicon(
        name: str,
        grid_size: int,
    ) -> Image:
        MODE = "RGB"
        LOFI_RESOLUTION = (7, 7)
        BACKGROUND_COLOR = (255, 255, 255, 255)
        image = Image.new(MODE, LOFI_RESOLUTION, BACKGROUND_COLOR)

        hex_str = IdenticonUtils.generate_hash(name)
        rand_color = IdenticonUtils.get_random_color(hex_str)

        lower_x = 1
        lower_y = 1
        upper_x = int(LOFI_RESOLUTION[0] / 2) + 1
        upper_y = LOFI_RESOLUTION[1] - 1
        limit_x = LOFI_RESOLUTION[0] - 1
        index = 0

        # Uses first half of calculated hex to randomly place pixels on grid
        # Placed pixels in first half of grid, then mirrors it to the other side
        first_half_hex = hex_str[6:]
        for x in range(lower_x, upper_x):
            for y in range(lower_y, upper_y):
                rand_int = int(first_half_hex[index], 16)
                if rand_int % 2 == 0:
                    image.putpixel((x, y), rand_color)
                    image.putpixel((limit_x - x, y), rand_color)

                index = index + 1

        # Scales identicon to size provided by user
        FINAL_RESOLUTION = (grid_size, grid_size)
        image = image.resize(FINAL_RESOLUTION, 0)

        return image
