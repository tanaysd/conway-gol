# Conway's Game of Life

This is a Python-based simulator for Conway's Game of Life. It is designed to be simple, efficient, and capable of handling very large patterns on a conceptually infinite grid.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/tutorials/python_quickstart.ipynb)

---

## 📂 Project Documentation

This project is extensively documented to help users, reviewers, and contributors.

* **[ELI5.md](ELI5.md)**: A simple, non-technical introduction to the Game of Life.
* **[CODE_STRUCTURE.md](CODE_STRUCTURE.md)**: A high-level overview of the Python code.
* **[TEST_PLAN.md](tests/TEST_PLAN.md)**: Describes the testing strategy and test cases.
* **[REVIEW_GUIDE.md](REVIEW_GUIDE.md)**: A guide for those who want to review or contribute to the project.

---

## 🤔 What is Conway's Game of Life?

For a simple and fun introduction to the concept, check out our **[ELI5 (Explain Like I'm 5) guide](ELI5.md)**.

---

## 룰 The Rules of the Game

The universe of the Game of Life is an infinite, two-dimensional grid of square *cells*, each of which is in one of two possible states, *live* or *dead*. Every cell interacts with its eight *neighbours*, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1.  **Underpopulation**: Any live cell with fewer than two live neighbours dies.
2.  **Survival**: Any live cell with two or three live neighbours lives on to the next generation.
3.  **Overpopulation**: Any live cell with more than three live neighbours dies.
4.  **Reproduction**: Any dead cell with exactly three live neighbours becomes a live cell.

---

## 🧠 How It Works

This simulator is designed to be highly efficient by avoiding the creation of a large, 2D grid in memory. Here are the core principles:

* **Sparse Representation**: We only keep track of the coordinates of live cells in a Python `set`.
* **Localized Simulation**: The simulation only considers the neighbors of currently live cells, making it fast even on a conceptually infinite grid.
* **64-bit Coordinates**: The program can handle extremely large coordinate values, allowing for vast patterns.

For a deeper dive into the code, see the **[CODE_STRUCTURE.md](CODE_STRUCTURE.md)**.

---

## 🚀 Running the Simulator

You can run the simulator from the command line.

**To run a simulation from a file:**

```bash
python gol.py --input examples/glider.life --ascii
```
```bash
python gol.py --input examples/glider.life --generations 100
```
```bash
python gol.py --help
```

### Examples

The `examples` folder contains several interesting patterns to get you started:

* `glider.life`: A classic pattern that moves across the grid.
* `block.life`: A stable, non-changing pattern.
* `blinker.life`: A simple oscillator.
* `diehard.life`: A pattern that runs for 130 generations before disappearing.

You can find more details in the `examples/README.md`.
