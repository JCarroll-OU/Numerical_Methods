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

## Ti-nspire library usage:
- Load the '*.tns' file onto your calculator via the Ti-nspire student software.
- Click 'menu', '1: Actions', '7: Library', "1: Refresh Libraries", and wait for this to complete
- Click the book icon (below the delete key) then click 6 to open the user-defined library tab
- Scroll down to 'numericalmethods'
  
## Ti-nspire library examples:
### Bisection Method:
- bisectionmethod(4.998*10^(−8)*x^(2)-1.157*10^(−13)*x^(4)-2.999*10^(−3),200,300,5)
- First parameter is F(x) that you want to find the root(s) of
- Second parameter is a, the lower bounds containing the solution
- Third parameter is b, the upper bounds containing the solution
- Fourth parameter is the number of iterations to complete
### False Position Method:
- falseposmethod(cos(x)-0.8*x^(2),0.5,1.5,5)
- First parameter is F(x) that you want to find the root(s) of
- Second parameter is a, the lower bounds containing the solution
- Third parameter is b, the upper bounds containing the solution
- Fourth parameter is the number of iterations to complete
### Newton's Method:
- newtonsmethod(e^(−0.5*x)*(4-x)-2,2,5)
- First parameter is F(x) that you want to find the root(s) of
  -- Derivatives will be calculated automatically (requires CAS)
- Second parameter is the inital guess
- Third parameter is the number of iterations to complete
### Secant Method:
- secantmethod(x-(2*e^(−x)),0,1,5)
- First parameter is F(x) that you want to find the root(s) of
- Second parameter is x_1, the first guess
- Third parameter is x_2, the second guess
- Fourth parameter is the number of iterations to complete
