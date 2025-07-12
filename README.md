# conway-gol

A simple implementation of Conway's Game of Life in Python.

## Running

The program expects Life 1.06 formatted input on `stdin` and prints the
state after ten generations:

```bash
python3 gol.py < pattern.life
```

## Tests

Run the unit tests with:

```bash
python3 -m unittest discover -v
```
