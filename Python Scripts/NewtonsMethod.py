import numpy as np

def newtons_method(f, f_prime, x_init, tol, maxIter):
    iteration = 0
    x = x_init
    error = tol + 1
    while (error > tol):
        dydx = f_prime(x)
        f_approx = f(x) 
        # newtons method implementation
        x = x - (f_approx / dydx)

        if (iteration >= maxIter):
            print("Maximum iterations exceeded!")
            return x
        iteration = iteration + 1
        error = abs(f_approx)
        # check if failed to converge
        if (abs(error) == np.inf):
            print("Runaway error!")
            return x
        
        print("Iteration:", iteration)
        print("F(x_{}) = F({}) =".format(iteration, x), f_approx)
        print("Error:", error)
        print(" ")
    print("Error within tolerance!")
    return x

#f = lambda x: ((np.e ** (-0.5 * x)) * (4 - x)) - 2
#f_prime = lambda x: ((np.e ** (-0.5 * x)) * ((2 * x) - 4)) - (2 * x)
f = lambda x: x - (2 * (np.e ** (-x)))
f_prime = lambda x: (2 * (np.e ** (-x))) + 1
newtons_method(f, f_prime, -3, 1e-5, 16)