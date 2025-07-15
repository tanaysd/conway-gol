"""Conway's Game of Life implementation."""

from collections import Counter
import sys
import argparse
from typing import Set, Tuple, TextIO

Coord = Tuple[int, int]

def parse_life(input_stream: TextIO) -> Set[Coord]:
    """Parse Life 1.06 format input from a given stream.

    Args:
        input_stream (TextIO): The stream to read from (e.g., sys.stdin or a file).

    Returns:
        Set[Tuple[int, int]]: Set of live cell coordinates parsed from input.
    """
    live_cells = set()
    for line in input_stream:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        x_str, y_str = line.split()
        live_cells.add((int(x_str), int(y_str)))
    return live_cells

def evolve(live_cells: Set[Coord]) -> Set[Coord]:
    """Compute the next generation of live cells using Conway's Game of Life rules.

    Args:
        live_cells (Set[Tuple[int, int]]): Current set of live cell coordinates.

    Returns:
        Set[Tuple[int, int]]: Set of coordinates representing the next generation.
    """
    neighbor_counts = Counter()

    for x, y in live_cells:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx != 0 or dy != 0:
                    neighbor_counts[(x + dx, y + dy)] += 1

    return {
        cell for cell, count in neighbor_counts.items()
        if count == 3 or (count == 2 and cell in live_cells)
    }

def render_ascii_with_axes(cells: set[tuple[int, int]], pad: int = 1) -> None:
    """
    Renders the Game of Life grid as ASCII art with labeled axes.
    Life 1.06 format: (x, y), with y increasing upward.

    Args:
        cells: Set of (x, y) live cell positions.
        pad: Padding added around the bounding box.
    """
    if not cells:
        print("(empty)")
        return

    xs, ys = zip(*cells)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    x_range = range(min_x - pad, max_x + pad + 1)
    y_range = range(min_y - pad, max_y + pad + 1)

    x_axis = '     ' + ''.join(f'{x:3}' for x in x_range)
    print(x_axis)

    for y in reversed(y_range):
        row = f'{y:3} |'
        for x in x_range:
            row += ' @ ' if (x, y) in cells else ' · '
        print(row)

    print()

def print_output(live_cells: Set[Coord]) -> None:
    """Print the current state of live cells in Life 1.06 format to stdout.

    Args:
        live_cells (Set[Tuple[int, int]]): Final generation's live cell coordinates.
    """
    print("#Life 1.06")
    for x, y in sorted(live_cells):
        print(f"{x} {y}")

def main() -> None:
    """Run the Game of Life simulation."""
    parser = argparse.ArgumentParser(
        description="Conway's Game of Life Simulator.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'input_file',
        nargs='?',
        type=argparse.FileType('r'),
        default=sys.stdin,
        help='Path to the input file (e.g., examples/glider.life).\n'
             'If not provided, reads from standard input.'
    )
    parser.add_argument(
        '--ascii',
        action='store_true',
        help='Render each generation as ASCII art.'
    )
    parser.add_argument(
        '--steps',
        type=int,
        default=10,
        help='Number of generations to evolve (default: 10).'
    )
    args = parser.parse_args()

    # The argparse.FileType handles opening the file or using stdin.
    # We just need to ensure the stream is closed if it's a file.
    with args.input_file as stream:
        live_cells = parse_life(stream)

    for i in range(args.steps):
        if args.ascii:
            print(f"\n🧬 Generation {i}")
            render_ascii_with_axes(live_cells)
        live_cells = evolve(live_cells)

    if args.ascii:
        print(f"\n🧬 Final Generation ({args.steps})")
        render_ascii_with_axes(live_cells)
    
    # Print the final state in Life 1.06 format
    print_output(live_cells)

if __name__ == "__main__":
    main()
