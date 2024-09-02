import numpy as np

def false_position_method(f, a, b, tol, maxIter): 
    # approximates a root, R, of f bounded 
    # by a and b to within tolerance 
    # | f(m) | < tol with m = (a*f(b) - b*f(a)) / (f(b) - f(a))
    
    iteration = 1
    error = tol + 1
    prevSol = 0
    while (error > tol):
        f_bounds_low = f(a)
        f_bounds_high = f(b)
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


        if (prevSol != 0):
            error = abs((x_approx - prevSol) / prevSol)
        prevSol = x_approx

        print("Iteration ", iteration)
        print("F(a) = ", f_bounds_low)
        print("F(b) = ", f_bounds_high)
        print("F(x_approx) = ", f_approx)
        print("New bounds [", a, ",", b, "]")
        print("Error: ", error)
        print(" ")
    return a, b
    
f = lambda x: np.cos(x) - (0.8 * (x**2))
false_position_method(f, 0.5, 1.5, 0.001, 5)