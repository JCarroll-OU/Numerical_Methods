import numpy as np

def newtons_method(f, f_prime, x_init, tol, maxIter, useApproxDydx):
    iterations = 0
    x = x_init
    error = tol + 1
    prevSol = 0
    lowestError = error
    iterLowError = iterations
    while (error > tol):
        dydx = f_prime(x)
        if (useApproxDydx):
            dydx = approximate_derivative(f, x, 0.01)
        f_approx = f(x)
        x = x - (f_approx / dydx)
        if (iterations >= maxIter):
            print("Maximum iterations exceeded!")
            return x
        iterations = iterations + 1
        if (prevSol != 0):
            error = abs((x - prevSol) / prevSol)
        if (error < lowestError):
            lowestError = error
            iterLowError = iterations
        if (abs(error) == np.inf):
            print("Runaway error!")
            return x
        prevSol = x

        print("Iteration ", iterations)
        print("x_approx = ", x)
        print("F(x_approx) = ", f_approx)
        print("Error: ", error)
        print("Lowest Error: ", lowestError, "at iteration", iterLowError)
        print(" ")
    print("Error within tolerance!")
    return x

def approximate_derivative(f, x_init, step_size):
    return (f(x_init + step_size) - f(x_init)) / step_size

# f(x)
#f = lambda x: ((np.e ** (-0.5 * x)) * (4 - x)) - 2
# f'(x) = dy/dx (hard-coded derivative) [if unknown, 
# enter True as the final parameter]
#f_prime = lambda x: (np.e ** (-0.5 * x)) * ((0.5 * x) - 3)
f = lambda x: x - (2 * (np.e ** (-x)))
f_prime = lambda x: (2 * (np.e ** (-x))) + 1
newtons_method(f, f_prime, 1, 1e-20, 5, False)