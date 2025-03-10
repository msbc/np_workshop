import numpy as np


def exercise_1(arr):
    # Create a new array with the same shape as the input array
    out = np.empty_like(arr)
    # Make a mask for x > 1
    mask = arr > 1
    # Perform log(x) + 1 for x > 1
    out[mask] = np.log(arr[mask]) + 1
    # Make a mask -1 < x <= 1 (uses the ~ operator to invert our last mask)
    mask = ~mask & (arr > -1)
    # Perform sign(x) * sqrt(|x|) for -1 < x <= 1
    out[mask] = np.sign(arr[mask]) * np.sqrt(np.abs(arr[mask]))
    # Make a mask for x <= -1
    mask = arr <= -1
    # Perform -x^2 for x <= -1
    out[mask] = - arr[mask]**2
    return out


def exercise_2(points):
    x = points[:, 0]  # X values, shape (n, 1)
    y = points[:, 1]  # Y values, shape (n, 1)

    # I just learned about the sparse option below which uses broadcasting in
    # the background and makes this fast. It's off by default.
    x, y = np.meshgrid(x, y, sparse=True)

    return np.sqrt((x - x.T)**2 + (y - y.T)**2)


def _exercise_2a(points):
    # more or less the same as exercise_2, but doing the broadcasting manually
    x = points[:, 0][:, np.newaxis]  # X values, shape (n, 1)
    y = points[:, 1][:, np.newaxis]  # Y values, shape (n, 1)

    # Use broadcasting to calculate the distance between all points
    return np.sqrt((x - x.T) ** 2 + (y - y.T) ** 2)


def _exercise_2b(points):
    # use np.linalg.norm, relatively slow for this case
    return np.linalg.norm(points[:, np.newaxis] - points, axis=-1)


def _exercise_2c(points):
    x = points[:, 0]  # X values, shape (n, 1)
    y = points[:, 1]  # Y values, shape (n, 1)

    x, y = np.meshgrid(x, y)  # no sparse option, slower
    return np.sqrt((x - x.T)**2 + (y - y.T)**2)


def _exercise_2d(points):
    return np.sqrt(np.sum((points[:, None] - points)**2, axis=-1))


def _exercise_2e(points):
    # use einsum, relatively slow for this case, but can be very fast for some
    # problems
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    return np.sqrt(np.einsum('ijk,ijk->ij', diff, diff))


# Part of optimizing is trying different solutions and comparing them. I
# compared these solutions using the following code in a Jupyter notebook:
#
# from instructor_solutions import solutions_05 as sol
# %timeit sol.exercise_2(points)
# %timeit sol._exercise_2a(points)
# %timeit sol._exercise_2b(points)
# %timeit sol._exercise_2c(points)
# %timeit sol._exercise_2d(points)
# %timeit sol._exercise_2e(points)
#
# My results were that exercise_2 was the fastest, followed by _exercise_2a:
# 2.46 ms ± 48 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 2.96 ms ± 181 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 12.9 ms ± 139 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 4.96 ms ± 124 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 12.9 ms ± 270 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 10.5 ms ± 236 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
