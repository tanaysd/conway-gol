# 🧭 REVIEW\_GUIDE.md

This guide is intended to help two distinct audiences navigate and evaluate the project:

1. **Reviewers** — evaluating correctness, structure, and design
2. **Users** — running simulations or modifying inputs to explore Conway’s Game of Life

---

## 👀 For Reviewers

### 🔍 What to Focus On

| Area                 | Questions to Ask                                                     |
| -------------------- | -------------------------------------------------------------------- |
| Correctness          | Does `evolve()` apply Conway’s rules accurately across all cases?    |
| Input/output parsing | Is Life 1.06 format parsed and printed correctly?                    |
| Edge handling        | Are very large coordinates (±2^63) and empty states safely handled?  |
| Sparse optimization  | Does the implementation avoid grid allocations and scale well?       |
| Code readability     | Are functions clearly named, typed, and documented?                  |
| Test coverage        | Do tests cover canonical patterns (block, blinker, glider, diehard)? |
| Modularity           | Can the logic be reused or tested independently of I/O?              |
| Consistency          | Is Google-style docstring formatting followed throughout?            |

### ✅ Review Checklist

* [ ] Run `test_gol.py` and validate all tests pass
* [ ] Read `glider_diff_log.md` and verify state transitions align
* [ ] Manually inspect `gol.py` for type safety and deterministic logic
* [ ] Try running an example: `python3 gol.py < examples/glider.life`
* [ ] Confirm `examples/` output matches known pattern behaviors

---

## 🧑‍💻 For Users

### 🔧 Getting Started

1. Clone the repository:

```bash
git clone git@github.com:tanaysd/conway-gol.git
cd conway-gol
```

2. Run a sample simulation:

```bash
python3 gol.py < examples/glider.life
```

3. Modify or create your own `.life` file:

```text
#Life 1.06
0 0
1 0
2 0
```

4. Pipe into the simulator:

```bash
python3 gol.py < your_pattern.life
```

5. Output will be in Life 1.06 format:

```text
#Life 1.06
...
```

### 📎 File Index

| File                 | Purpose                                          |
| -------------------- | ------------------------------------------------ |
| `gol.py`             | Main simulation kernel                           |
| `test_gol.py`        | Unit tests for core logic                        |
| `examples/`          | Canonical input/output samples                   |
| `glider_diff_log.md` | Visual + tabular walkthrough of glider evolution |
| `ELI5.md`            | Friendly introduction using LEGO-style analogy   |
| `TEST_PLAN.md`       | Complete test strategy including edge cases      |
| `CODE_STRUCTURE.md`  | High-level function-level organization overview  |
| `REVIEW_GUIDE.md`    | (You are here) Review and usage instructions     |

---

### 🧠 Want to Explore More?

* Try running `diehard.life` for a longer simulation (130 steps)
* Build your own pattern using Life 1.06 spec
* Fork and add animation or visualization

Let us know if you want an interactive notebook or HTML explorer added.
