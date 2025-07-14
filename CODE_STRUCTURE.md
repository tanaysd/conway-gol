# 🧭 CODE_STRUCTURE.md

This document outlines the structure of the `gol.py` implementation for Conway's Game of Life (64-bit version), aiding contributors and reviewers in understanding key components and control flow.

---

## 📂 File Overview

- `gol.py`: Main execution script.
  - Handles input parsing (Life 1.06 format)
  - Executes 10 iterations of Game of Life logic
  - Writes output in Life 1.06 format
- `test_gol.py` *(optional)*: Unit tests using the `unittest` framework.
- `examples/`: Sample `.life` files for reference and validation.
- `glider_diff_log.md`: Visual + tabular step-by-step trace of a glider pattern. #TODO

---

## 🔧 Key Functions (in `gol.py`)

### `parse_input() -> Set[Tuple[int, int]]`
Parses Life 1.06 format from `stdin` into a set of live cell coordinates.

### `evolve(live_cells: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]`
Applies Conway's rules to the current generation and returns the new generation.
- Operates only on live cells and their neighbors.
- Uses `collections.Counter` for neighbor counting.

### `print_output(live_cells: Set[Tuple[int, int]])`
Prints the final state of the board in Life 1.06 format to `stdout`.

### `main()`
- Invokes input parser
- Runs evolution loop 10 times
- Outputs final board state

---

## 🔄 Control Flow

stdin --> parse_input() --> 10 × evolve() --> print_output() --> stdout

---

## 📦 Data Structures

- `Set[Tuple[int, int]]`: To store current live cells.
- `Counter[Tuple[int, int]]`: To count neighbors per cell across the grid.

---

## 🧼 Design Notes

- Modular and testable: `evolve()` is pure and stateless.
- Sparse-safe: No grid allocation; space unbounded.
- Spec-compliant: Life 1.06 format respected throughout.

---

## 🔗 Related Files

- `README.md`: Overview, objectives, usage
- `TEST_PLAN.md`: Strategy and test scenarios
