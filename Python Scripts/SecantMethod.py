import numpy as np

def secant_method(f, x_1, x_2, tol, maxIter):
    x_prev = x_1
    x_curr = x_2
    x_next = 0
    iterations = 0
    error = tol + 1
    # x_next is x_{3 + iterations}
    while (error > tol):
        # secant method implementation
        x_next = x_curr - ((f(x_curr) * (x_prev - x_curr)) 
                           / (f(x_prev) - f(x_curr)))
        f_approx = f(x_next)
        error = abs(f_approx)
        # check if failed to converge 
        if (abs(error) == np.inf):
            print("Runaway error!")
            return x_next
        # update x-values for next iteration
        x_prev = x_curr
        x_curr = x_next
        # display some information for the current iteration
        print("Iteration:", 3 + iterations)
        print("F(x_{}) = F({}) = ".format(3 + iterations, x_next), f_approx)
        print("Error:", error)
        print(" ")

        if ((3 + iterations) >= maxIter):
            print("Maximum iterations exceeded!")
            return x_next
        # incremement in the most barbaric way possible
        iterations = iterations + 1
    print("Error within tolerance!")
    return x_next

f = lambda x: x - (2 * (np.e ** (-x)))
secant_method(f, 0, 1, 1e-5, 8)