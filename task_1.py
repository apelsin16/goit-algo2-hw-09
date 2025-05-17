import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Генерація випадкової точки у заданих межах
def random_point(bounds):
    return [random.uniform(low, high) for low, high in bounds]


# Обмеження координат в межах bounds
def clip(point, bounds):
    return [max(min(x, bounds[i][1]), bounds[i][0]) for i, x in enumerate(point)]


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6, step_size=0.1):
    current = random_point(bounds)
    current_value = func(current)

    for _ in range(iterations):
        # Створюємо сусідню точку
        neighbor = [xi + random.uniform(-step_size, step_size) for xi in current]
        neighbor = clip(neighbor, bounds)
        neighbor_value = func(neighbor)

        if abs(current_value - neighbor_value) < epsilon:
            break

        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value

    return current, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best = random_point(bounds)
    best_value = func(best)

    for _ in range(iterations):
        candidate = random_point(bounds)
        candidate_value = func(candidate)

        if abs(best_value - candidate_value) < epsilon:
            break

        if candidate_value < best_value:
            best, best_value = candidate, candidate_value

    return best, best_value


# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current = random_point(bounds)
    current_value = func(current)
    best = current
    best_value = current_value

    for _ in range(iterations):
        if temp < epsilon:
            break

        candidate = [xi + random.uniform(-1, 1) for xi in current]
        candidate = clip(candidate, bounds)
        candidate_value = func(candidate)

        delta = candidate_value - current_value

        if delta < 0 or random.random() < math.exp(-delta / temp):
            current, current_value = candidate, candidate_value

            if current_value < best_value:
                best, best_value = current, current_value

        temp *= cooling_rate

    return best, best_value


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]  # Можна розширити для більшої розмірності

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
