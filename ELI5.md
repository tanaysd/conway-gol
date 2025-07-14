## 🧸 ELI5: What Is Conway’s Game of Life?
Imagine a giant LEGO table where each stud (dot) can hold a single LEGO block. These blocks represent “live cells.”

Every time we ring a bell (say, every second), the blocks look at their 8 surrounding neighbors—the blocks to their left, right, top, bottom, and diagonals—and decide if they want to stay, die, or have a new block appear.

### 🧠 The Rules (Lego Edition)
- 🟢 A block (cell) stays alive if it has 2 or 3 neighbors. It's like being in a cozy neighborhood.

- 🔴 A block dies (is removed) if it has too few (lonely) or too many (overcrowded) neighbors.

- 🟡 An empty spot gets a new block only if it has exactly 3 neighbors—the perfect recipe to "give birth" to life.

You only update the board after checking everything, so all changes happen at once.

### 📏 But There’s No Board?
> Right! In our case, the LEGO table is infinite. There’s no edge. You can build anywhere—even at position 9,876,543,210,123 or −1,000,000,000,000. So instead of drawing the whole table, we just remember where blocks exist, and update only those and their neighbors.

### 🧬 Why It’s Cool
This little system:

- Is completely deterministic—no randomness.
- Can produce amazing behavior like:
- Gliders that walk across the board,
- Oscillators that flip back and forth,
- Still lifes that never change.
- Is Turing complete—in theory, you could build a computer out of it.
