"""Conway's Game of Life implementation."""

from collections import Counter
import sys
from typing import Set, Tuple

Coord = Tuple[int, int]

def parse_life() -> Set[Coord]:
    """Parse Life 1.06 format input from stdin.

    Returns:
        Set[Tuple[int, int]]: Set of live cell coordinates parsed from input.
    """
    live_cells = set()
    for line in sys.stdin:
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

def render_ascii(cells, pad=1):
    if not cells:
        print("(empty)")
        return
    xs, ys = zip(*cells)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    for y in range(min_y - pad, max_y + pad + 1):
        row = ''
        for x in range(min_x - pad, max_x + pad + 1):
            row += '*' if (x, y) in cells else '·'
        print(row)

def print_output(live_cells: Set[Coord]) -> None:
    """Print the current state of live cells in Life 1.06 format to stdout.

    Args:
        live_cells (Set[Tuple[int, int]]): Final generation's live cell coordinates.
    """
    print("#Life 1.06")
    for x, y in sorted(live_cells):
        print(f"{x} {y}")

def main() -> None:
    """Run the Game of Life simulation for 10 generations.

    Reads Life 1.06 input from stdin, applies 10 iterations of Conway's rules,
    and prints the final state to stdout.
    """
    live_cells = parse_life()
    for idx in range(10):
        live_cells = evolve(live_cells)
        print(f"Gen {idx+1}")
        render_ascii(live_cells)
    print_output(live_cells)

if __name__ == "__main__":
    main()
