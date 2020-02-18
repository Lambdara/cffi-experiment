# CFFI-Experiment

This is a simple attempt at using the Python CFFI.

For the most part, it follows [this guide](https://cffi.readthedocs.io/en/latest/overview.html#main-mode-of-usage).

To run, use `main.sh`. It calls `build.py` and then `run.py`.

The `lib` directory contains simple code for approximating pi monte-carlo style, by seeing how many random points within [0,1]x[0,1] fall within the top-right quadrant of the unit circle.

`build.py` uses the Python CFFI as instructed by the guide to create a library from the contents of `lib` that can be imported into Python scripts.

`run.py` uses the library to approximate pi for the user using their specified number of iterations.

## Dependencies

This script was written in Python 3.8, and uses the `cffi` package.
