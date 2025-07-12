# conway-gol

A simple implementation of Conway's Game of Life in Python.

## Running

The program expects Life 1.06 formatted input on `stdin` and prints the
state after ten generations:

```bash
python3 gol.py < pattern.life
```

An example pattern file, `pattern.life`, is included in the repository and
contains a small glider that can be used to try out the program.

## Tests

Run the unit tests with:

```bash
python3 -m unittest discover -v
```
