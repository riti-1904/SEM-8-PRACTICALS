
def eval_func(individual):
    """Evaluation function to minimize: Sphere function (sum of squares)."""
    return sum(x ** 2 for x in individual),
