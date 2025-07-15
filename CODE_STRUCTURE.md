# 🧭 CODE_STRUCTURE.md

This document outlines the structure of the `gol.py` implementation for Conway's Game of Life (64-bit version), aiding contributors and reviewers in understanding key components and control flow.

---

## 📂 File Overview

- `gol.py`: Main execution script.
  - Handles input parsing (Life 1.06 format) via `parse_life()`
  - Executes a configurable number of generations (default 10)
  - Optionally renders each generation as ASCII art
  - Writes final board state in Life 1.06 format
- `test_gol.py` *(optional)*: Unit tests using the `unittest` framework.
- `examples/`: Sample `.life` files for reference and validation.

---

## 🔧 Key Functions (in `gol.py`)

### `parse_life(input_stream: TextIO) -> Set[Tuple[int, int]]`
Parses Life 1.06 formatted data from any text stream into a set of live cell coordinates.

### `evolve(live_cells: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]`
Applies Conway's rules to the current generation and returns the new generation.
- Operates only on live cells and their neighbors.
- Uses `collections.Counter` for neighbor counting.

### `render_ascii_with_axes(cells: Set[Tuple[int, int]], pad: int = 1)`
Renders the grid to the terminal with labeled axes when the `--ascii` option is enabled.

### `print_output(live_cells: Set[Tuple[int, int]])`
Prints the final state of the board in Life 1.06 format to `stdout`.

### `main()`
- Parses command-line arguments
- Reads input via `parse_life()`
- Evolves the pattern for the requested number of steps
- Optionally displays each generation in ASCII
- Outputs the final board state

---

## 🔄 Control Flow

input stream/file --> parse_life() --> [evolve() repeated for N steps] --> optional ASCII --> print_output() --> stdout

---

## 📦 Data Structures

- `Coord = Tuple[int, int]`: Type alias for board coordinates.
- `Set[Coord]`: To store current live cells.
- `Counter[Coord]`: To count neighbors per cell across the grid.

---

## 🧼 Design Notes

- Modular and testable: `evolve()` is pure and stateless.
- Sparse-safe: No grid allocation; space unbounded.
- Spec-compliant: Life 1.06 format respected throughout.

---

## 🔗 Related Files

- `README.md`: Overview, objectives, usage
- `TEST_PLAN.md`: Strategy and test scenarios
