from math import sqrt


def solve_quadratic_equation(a, b, c):
    try:
        if a != 0 and b != 0:
            xa = (-b + sqrt((b ** 2) - ((4 * a) * c))) / (2 * a)
            xb = (-b - (sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
            return xa, xb
        elif b == 0 and a != 0:
            xa = sqrt(-c / a)
            return xa, None
        elif a == 0 and b != 0:
            xa = -c / b
            return xa, None
    except ValueError:
        print("Your inputs have not real solutions.")
        return None, None


a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
xa, xb = solve_quadratic_equation(a, b, c)
print(xa if xa is not None else "", xb if xb is not None else "")
