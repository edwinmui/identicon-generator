import argparse, os
from utils.identicon_utils import IdenticonUtils
from PIL import Image


class Identicon:
    identicon: Image = None

    def __init__(self, name: str, grid_size: int):
        self.name = name
        self.grid_size = grid_size

    def generate_identicon(self):
        self.identicon = IdenticonUtils.draw_identicon(self.name, self.grid_size)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(script_dir, "..", "identicon.png")

        self.identicon.save(save_path)


def main():
    parser = argparse.ArgumentParser(description="Generate Identicon images")
    parser.add_argument("--grid-size", type=int, default=50, help="Size of the grid")

    args = parser.parse_args()
    if args.grid_size < 7:
        raise Exception("Please provide a grid_size >= 7")

    NAME_INPUT = "Enter your username: "
    name = input(NAME_INPUT)

    identicon = Identicon(name=name, grid_size=args.grid_size)
    identicon.generate_identicon()


if __name__ == "__main__":
    main()
