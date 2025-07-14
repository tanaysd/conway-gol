# 🤖 AGENTS.md

This project allows automated tools to modify the code. Please observe the following guidelines when contributing or generating patches:

- **Tests**: Always run `python3 -m unittest discover -v` and ensure all tests pass before committing. Add new tests in `tests/` when fixing bugs or adding features.
- **Docstrings**: Document every function using Google-style docstrings so that intent and parameters are clear.
- **Dependencies**: Keep the implementation minimal and rely only on the Python standard library. External packages are unnecessary.
- **64-bit semantics**: Coordinates are conceptually 64-bit signed integers. Avoid logic that assumes smaller ranges or allocates a fixed grid.
- **Life 1.06 format**: Input and output must remain compliant with the Life 1.06 specification.
- **Deterministic design**: `evolve()` should remain stateless and purely derived from its input.

Following these rules helps maintain a simple, testable simulator that is easy for reviewers and automated agents to reason about.
