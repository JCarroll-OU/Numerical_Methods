import numpy as np

def secant_method(f, x_1, x_2, tol, maxIter):
    x_prev = x_1
    x_curr = x_2
    x_next = 0 # pre-defined so it can be returned later
    iterations = 0
    error = tol + 1
    lowestError = error
    iterLowError = iterations
    # x_next is x_{3 + iterations}
    while (error > tol):
        # secant method implementation
        x_next = x_curr - ((f(x_curr) * (x_prev - x_curr)) 
                           / (f(x_prev) - f(x_curr)))
        f_approx = f(x_next) # get f(x_guess)

        # update the error
        if (x_curr != 0):
            error = abs((x_next - x_curr) / x_curr)
        # track lowest error
        if (error < lowestError):
            lowestError = error
            iterLowError = iterations
        # check if failed to converge 
        if (abs(error) == np.inf):
            print("Runaway error!")
            return x_next
        
        # update x-values for next iteration
        x_prev = x_curr
        x_curr = x_next

        # display some information for the current iteration
        print("Iteration:", 3 + iterations)
        print("x_{} =".format(3 + iterations), x_next)
        print("F(x_{}) =".format(3 + iterations), f_approx)
        print("Error: ", error)
        print("Lowest Error: ", lowestError, "at iteration", 3 + iterLowError)
        print(" ")

        # incremement in the most barbaric way possible
        if ((3 + iterations) >= maxIter):
            print("Maximum iterations exceeded!")
            return x_next
        iterations = iterations + 1
    print("Error within tolerance!")
    return x_next

# f(x)
f = lambda x: x - (2 * (np.e ** (-x)))
secant_method(f, 0, 1, 1e-20, 8)