# 🧪 Examples

This folder contains test inputs in Life 1.06 format for validating the Game of Life simulator:

| File               | Description                                 |
|--------------------|---------------------------------------------|
| `glider.life`      | A glider pattern that moves diagonally      |
| `glider_after_10.life` | Expected output after 10 generations of glider |
| `block.life`       | A still life (unchanged after any number of steps) |
| `blinker.life`     | A simple oscillator with period 2           |
| `diehard.life`     | Dies out after 130 generations (for long-run test) |

Usage:
```bash
python3 gol.py < examples/glider.life
