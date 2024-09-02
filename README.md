# Numerical Methods for Engineering Computation in Python
Collection of Python scripts used in AME-3723: Numerical Methods for Engineering Computation for obtaining and/or validating homework answers. 

## Supported methods for approximating the root(s) of an equation:
Bracketing Methods: (Slower but always converge assuming f(x) = 0 is bounded by a and b)
- Bisection method (Requires an initial range to search for a root within, f(x) = 0 must be bounded by a and b)
- False Position (Linear interpolation) method (Requires an initial range to search for a root within, f(x) = 0 must be bounded by a and b)

Open Methods: (Faster but do not always converge)
- Newton-Raphson method: (Requires the derivative to be known or approximated and an inital guess must be made)
- Secant method: (Does not require a derivative but does require two inital guesses)

## Usage
Replace the 'f' parameter at the end of each script with the function you are attempting to find the root of. Replace all other parameters as necessary.
