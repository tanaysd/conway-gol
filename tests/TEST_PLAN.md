# ✅ TEST\_PLAN.md

This test plan outlines the strategy for verifying correctness, stability, and performance of the 64-bit Conway's Game of Life implementation. It focuses on unit-level accuracy, format compliance, and behavioral validation through canonical patterns.

---

## 🎯 Objectives

* Ensure core simulation logic (`evolve()`) conforms to Conway’s rules.
* Validate input/output parsing against Life 1.06 format.
* Confirm stable, oscillating, and dynamic behaviors match known patterns.
* Cover edge conditions including sparse extremes and empty states.

---

## 🔬 Unit Tests

### ✅ Core Logic Tests (`evolve()`)

| Test Case           | Description                                       |
| ------------------- | ------------------------------------------------- |
| Still life: block   | Verify unchanged state after multiple generations |
| Oscillator: blinker | Ensure 2-state oscillation over generations       |
| Glider              | Verify translational movement over 4–5 steps      |
| Empty input         | No live cells should remain after 1 generation    |
| Single cell         | Cell dies due to underpopulation                  |

### ✅ Format Parsing

| Test Case         | Description                                 |
| ----------------- | ------------------------------------------- |
| Header handling   | `#Life 1.06` must be skipped                |
| Mixed blank lines | Should be ignored                           |
| Large coordinate  | Support 64-bit signed range (e.g., ±2^63−1) |

---

## 🧪 Integration Tests

### ✅ Multi-step Validations

| Scenario       | Setup           | Expected Result                |
| -------------- | --------------- | ------------------------------ |
| `glider.life`  | 10 generations  | Matches `glider_after_10.life` |
| `block.life`   | 10 generations  | Output identical to input      |
| `diehard.life` | 130 generations | All cells dead by end          |

### ✅ Edge Conditions

| Condition                    | Test Description                      |
| ---------------------------- | ------------------------------------- |
| Very sparse grid             | Coordinates at (±1e12, ±1e12)         |
| Non-rectangular distribution | Clustered lines vs diagonal gliders   |
| Duplicate input coordinates  | Should be de-duplicated automatically |

---

## 🧪 Manual Tests (Optional)

* Visually inspect ASCII output of known oscillators (e.g., blinker, pulsar)
* Stress-test with 10k+ live cells in random locations

---

## 🧰 Running the Tests

```bash
python3 -m unittest discover -v
```

For visual tests:

```bash
python3 gol.py < examples/glider.life
```

---

## ✅ Coverage Summary

* Deterministic behavior: Yes
* Sparse-safe: Yes
* Life 1.06 compliant: Yes
* Edge-safe on coordinate scale: Yes

Let me know if you'd like these encoded as `.py` test cases under `tests/` or kept in this high-level verification document.
