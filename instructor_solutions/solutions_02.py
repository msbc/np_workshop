import numpy as np


def exercise_1(n=None, quiet=False):
    """
    Show that mutiplying a matrix by the identity matrix results in the original matrix.
    """

    n = n or np.random.randint(1, 10)  # Randomly select n if not provided
    mat_a = np.random.rand(n, n)  # Random `n x n` matrix A
    mat_i = np.eye(n)  # Identity matrix `n x n`

    # Multiply matrix A by the identity matrix
    mat_b = np.dot(mat_a, mat_i)

    if not quiet:
        print("Matrix A:")
        print(mat_a)
        print("\nIdentity Matrix:")
        print(mat_i)
        print("\nMatrix B (A * I):")
        print(mat_b)
        print("\nMatrix A == Matrix B:")
        print(np.all(mat_a == mat_b))

    return np.all(mat_a == mat_b)


def exercise_2(array=None, n=100_000):
    """
    Write a one-line statement that returns `True` if an array is a monotonically
    increasing sequence, or `False` otherwise.
    """

    array = array or np.random.rand(n)  # Random array if not provided
    return _exercise_2c(array)


# Bonus exercise see which one is faster, or maybe you can come up with a faster
# solution. You can use the `timeit` module or `%timeit` magic to compare the
# performance of these. Also, which solution is fastest might depend on the size
# or content of the array. Maybe some solutions are faster to return `False` than
# `True`, or vice versa.

def _exercise_2a(array):
    """
    First attempt at solving exercise 2. Easily readable.
    """
    return np.all(np.diff(array) >= 0)


def _exercise_2b(array):
    """
    If you know about "short-circuiting", you might think of this solution,
    but np.any does not short-circuit, so it's both slower and less readable.
    """
    return not np.any(np.diff(array) < 0)


def _exercise_2c(array):
    """
    This is a faster solution, but it's not as readable as the first one.
    It's faster because np.diff can do a lot of things, but we only need to know
    if all the differences are positive, so we can skip some steps.
    """
    return np.all(array[1:] >= array[:-1])


def exercise_3(array=None, seed=1234, plot=False):
    """
    Peak finding algorithm. Ignores the first and last elements of the array.

    Parameters
    ----------
    array : np.ndarray, optional
        1-dimensional array of numbers. If not provided, a random array is generated.
    seed : int, optional
        Random seed for generating the array.
    plot : bool, optional
        If True, plot the array and the peaks.
    """
    if array is None:
        np.random.seed(seed)
        array = np.random.rand(100)
    else:
        array = np.atleast_1d(array)
        try:
            assert array.ndim == 1
        except AssertionError:
            raise ValueError("Input array must be 1-dimensional.")

    loc = np.where((array[1:-1] > array[:-2]) & (array[1:-1] > array[2:]))[0] + 1

    if plot:
        try:
            import matplotlib as mpl
            import matplotlib.pyplot as plt

            # Plot the array and the peaks
            plt.plot(array)
            plt.plot(loc, array[loc], "x", color="black")
            # Add labels and title
            plt.xlabel("Index")
            plt.ylabel("Value")
            plt.title("Peak Finding Algorithm")

            # These are my personal preferences for plots
            ax = plt.gca()
            ax.xaxis.set_ticks_position('both')
            ax.yaxis.set_ticks_position('both')
            ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator())
            ax.yaxis.set_minor_locator(mpl.ticker.AutoMinorLocator())
            ax.tick_params(axis='both', which='both', direction='in')
        except ImportError:
            print("Plotting failed. Matplotlib not found.")

    return loc
