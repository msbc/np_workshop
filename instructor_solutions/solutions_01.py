import numpy as np


def exercise_1(n=None, quiet=False):
    """
    Prove that given `n`, two `n x n` matrices `A` and `B` of random
    values and verify (A + B)^T = A^T + B^T.

    Parameters
    ----------
    n : int, optional, size of the square matrices
    quiet : bool, optional, if True, suppress print statements
    """
    # ^ this is a docstring, it is a string that describes what the function does

    n = n or np.random.randint(1, 10)  # Randomly select n if not provided
    mat_a = np.random.rand(n, n)  # Random `n x n` matrix A
    mat_b = np.random.rand(n, n)  # Random `n x n` matrix B

    if not quiet:
        print(f"Matrix A:\n{mat_a}\n")
        print(f"Matrix B:\n{mat_b}\n")
        print(f"Matrix (A + B).T:\n{(mat_a + mat_b).T}\n")
        print(f"Matrix A.T + B.T:\n{mat_a.T + mat_b.T}\n")

    return np.allclose((mat_a + mat_b).T, mat_a.T + mat_b.T)


def exercise_2():
    """
    Validate that the following operations work copy-free.
    """

    A = np.arange(12)

    A4x3 = A.reshape(4, 3)
    Arow = A.reshape(1, 12)
    print(Arow, Arow.ndim)

    Acol = A.reshape(12, 1)
    print(Acol, Acol.ndim)

    print(A4x3.ravel())      # Makes array 1D
    print(Acol.squeeze())    # Eliminates any axes of length 1
    print(A4x3.T)            # Transpose
    print(A.view(np.int32))  # Reinterpret the bytes as 32-bit integers rather than 64-bit

    arrays = {"A4x3": A4x3, "Arow": Arow, "Acol": Acol, "A4x3.ravel()": A4x3.ravel(),
              "Acol.squeeze()": Acol.squeeze(), "A4x3.T": A4x3.T,
              "A.view(np.int32)": A.view(np.int32),
              }

    out = True
    for name, array in arrays.items():
        out &= np.shares_memory(A, array)  # out = out and np.shares_memory(A, array)
        print(f"{name} shares memory with A: {np.shares_memory(A, array)}")

    if out:
        print("All operations are copy-free.")
    else:
        print("Some operations are not copy-free.")

    return out
