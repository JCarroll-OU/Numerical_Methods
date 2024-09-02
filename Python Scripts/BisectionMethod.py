import numpy as np

def bisection_method(f, a, b, tol, maxIter): 
    # approximates a root, R, of f bounded 
    # by a and b to within tolerance 
    # | f(m) | < tol with m the midpoint 
    
    iteration = 0
    error = tol + 1
    prevSol = 0
    while (error > tol):
        x_approx = (a + b) / 2
        f_approx = f(x_approx)
        f_bounds_low = f(a)
        f_bounds_high = f(b)

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
        print("F(x_approx) = ", f_approx)
        print("F(b) = ", f_bounds_high)
        print("New bounds [", a, ",", b, "]")
        print("Error: ", error)
        print(" ")
    return a, b
    
f = lambda x: ((4.998E-8) * (x**2)) - ((1.157E-13) * (x ** 4)) - (2.999E-3)
bisection_method(f, 200, 300, 0.001, 4)