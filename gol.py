"""Conway's Game of Life implementation."""

from __future__ import annotations

from typing import Iterable, Set, Tuple

import sys


def parse_life(lines: Iterable[str]) -> Set[Tuple[int, int]]:
    """Parse Life 1.06 formatted lines into a set of live cell coordinates."""
    iterator = iter(lines)
    header = next(iterator, '').strip()
    if header != '#Life 1.06':
        raise ValueError('Input must start with #Life 1.06')
    live_cells: Set[Tuple[int, int]] = set()
    for line in iterator:
        line = line.strip()
        if not line:
            continue
        x_str, y_str = line.split()
        live_cells.add((int(x_str), int(y_str)))
    return live_cells


def evolve(live_cells: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    """Return the next generation of live cells."""
    neighbor_counts: dict[Tuple[int, int], int] = {}
    for x, y in live_cells:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                neighbor = (x + dx, y + dy)
                neighbor_counts[neighbor] = neighbor_counts.get(neighbor, 0) + 1

    new_live: Set[Tuple[int, int]] = set()
    for cell, count in neighbor_counts.items():
        if count == 3 or (count == 2 and cell in live_cells):
            new_live.add(cell)
    return new_live


def main() -> None:
    """Run the Game of Life for ten generations and print the result."""

    live_cells = parse_life(sys.stdin)
    for _ in range(10):
        live_cells = evolve(live_cells)

    print('#Life 1.06')
    for x, y in sorted(live_cells):
        print(f'{x} {y}')


if __name__ == '__main__':
    main()
