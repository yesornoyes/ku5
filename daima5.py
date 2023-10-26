import numpy as np

def solve_linear_equation(coefficients, constants):
    try:
        solution = np.linalg.solve(coefficients, constants)
        return tuple(solution)
    except np.linalg.LinAlgError:
        return "无解"

# 示例方程：
# 2x + 3y + 4z = 10
# 5x + 6y + 7z = 20
# 8x + 9y + 10z = 30

coefficients = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
constants = np.array([10, 20, 30])

solution = solve_linear_equation(coefficients, constants)

if isinstance(solution, str):
    print(solution)
else:
    x, y, z = solution
    print("x =", x)
    print("y =", y)
    print("z =", z)
# ku5
