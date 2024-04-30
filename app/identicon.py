import argparse
from utils.identicon_utils import IdenticonUtils


class Identicon:
    grid: list[list[str]] = None

    def __init__(self, name: str, grid_size: int):
        self.name = name
        self.grid_size = grid_size

    """
    Generates an indenticon based on provided string.
    """

    def generate_identicon(self):
        self.grid = IdenticonUtils.generate_grid(self.grid_size)
        self.grid = IdenticonUtils.draw_identicon(self.name, self.grid)
        IdenticonUtils.save_identicon(self.grid)


def main():
    parser = argparse.ArgumentParser(description="Generate Identicon images")
    parser.add_argument("--grid-size", type=int, default=5, help="Size of the grid")
    args = parser.parse_args()

    NAME_INPUT = "Enter your username: "
    name = input(NAME_INPUT)

    identicon = Identicon(name=name, grid_size=args.grid_size)
    identicon.generate_identicon()


if __name__ == "__main__":
    main()
