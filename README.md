## 🧬 Conway’s Game of Life — 64-bit Infinite Grid (Life 1.06)
This repository contains a sparse, high-performance implementation of Conway’s Game of Life that operates over an unbounded 2D space of 64-bit signed integer coordinates. The simulator is compliant with the Life 1.06 file format, and supports arbitrary large or negative coordinates without assuming any grid bounds.

## 🎯 Objective
Simulate 10 iterations of Conway's Game of Life, given an initial configuration of live cells as input in Life 1.06 format. The program reads from standard input, processes the evolution, and writes the final state (after 10 generations) to standard output—again in Life 1.06 format.

## 📜 Rules of the Game
The Game of Life is a cellular automaton devised by mathematician John Conway. It evolves based on simple local rules applied to a 2D grid of cells, each of which is either alive or dead:

**Survival**: A live cell with 2 or 3 live neighbors stays alive.

**Death** by underpopulation or overpopulation: A live cell with fewer than 2 or more than 3 neighbors dies.

**Birth**: A dead cell with exactly 3 live neighbors becomes alive.

The 8 surrounding positions around a cell constitute its Moore neighborhood.

## 🧠 Design Considerations
📏 Infinite Space (64-bit Integers)
Coordinates can span the full signed 64-bit integer range:
[-2⁶³, 2⁶³ - 1]

The grid is conceptually infinite and extremely sparse.

⚠️ Constraints
- The simulation cannot use a 2D array or matrix.
- Coordinates must be handled as native Python integers but semantically treated as 64-bit safe.
- The algorithm must only simulate neighborhoods around currently live or potentially live cells to remain efficient.

## 🧱 Core Design Principles
| Principle                     | Description |
| ----------------------------- | --------------------------------------------------------------- |
| **Sparse Representation**     | Store live cells in a `set` of `(x, y)` tuples. |
| **Local Update Logic**        | Examine neighborhoods only around live cells. |
| **Deterministic & Stateless** | Each generation depends solely on the previous grid state. |
| **Composable Kernel**         | Encapsulate rules in an `evolve()` function. |
| **Minimal, Spec-Compliant I/O** | I/O follows the Life 1.06 spec. |
| **64-bit Integer Compliance** | Coordinates treated as 64‑bit signed values. |

## Running

The program expects Life 1.06 formatted input on `stdin` and prints the
state after ten generations:

```bash
python3 gol.py < examples/glider.life --ascii
python3 gol.py < examples/glider.life --ascii --steps 15
```

An example pattern file, `pattern.life`, is included in the repository and
contains a small glider that can be used to try out the program.

## Tests

Run the unit tests with:

```bash
python3 -m unittest discover -v
```
## 📂 Project Documentation Structure

The following artifacts are recommended to ensure the project is self-explanatory, review-ready, and reproducible. This suite of documents supports contributors, maintainers, and reviewers.

| Addition               | Purpose|
| ---------------------- | -----------------------------------------------------|
| README.md              | Project overview, usage, and objectives.|
| CODE_STRUCTURE.md      | High-level summary of code organization.|
| Inline docstrings      | Self-documenting core functions.|
| examples/ folder       | Sample input and output references.|
| TEST_PLAN.md           | Test cases and strategy.|
| REVIEW_GUIDE.md (opt.) | Reviewer checklist and evaluation focus.|
| ELI5.md                | Conceptual introduction via analogy.|
