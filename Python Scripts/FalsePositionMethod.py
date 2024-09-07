import numpy as np

def false_position_method(f, a, b, tol, maxIter):
    iteration = 0
    error = tol + 1
    while (error > tol):
        f_bounds_low = f(a)
        f_bounds_high = f(b)
        # False position method implementation
        x_approx = ((a * f_bounds_high) - (b * f_bounds_low)) / (f_bounds_high - f_bounds_low)
        f_approx = f(x_approx)

        # check if a and b bound a root
        if np.sign(f_bounds_low) == np.sign(f_bounds_high):
            raise Exception("The scalars a and b do not bound a root")

        if (f_approx * f_bounds_low) < 0:
            b = x_approx
        else:
            a = x_approx

        if (iteration >= maxIter):
             return a, b
        iteration = iteration + 1
        error = abs(f_approx)

        print("Iteration:", iteration)
        print("x = [{}, {}]".format(a, b))
        print("F(a_{}) = F({}) =".format(iteration, a), f_bounds_low)
        print("F(x_{}) = F({}) =".format(iteration, x_approx), f_approx)
        print("F(b_{}) = F({}) =".format(iteration, b), f_bounds_high)
        print("Error:", error)
        print(" ")
    return a, b
    
f = lambda x: np.cos(x) - (0.8 * (x**2))
false_position_method(f, 0.5, 1.5, 1e-20, 5)