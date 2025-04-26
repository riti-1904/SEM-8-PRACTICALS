import random

class GeneticAlgorithm:
    def __init__(self, fitness_function, parameter_ranges, generations=10):
        self.fitness_function = fitness_function
        self.parameter_ranges = parameter_ranges
        self.generations = generations

    def random_param(self, param_range):
        if isinstance(param_range[0], int):
            return random.randint(*param_range)
        else:
            return random.uniform(*param_range)

    def optimize(self, population_size=5):
        best_score = float('inf')
        best_params = {}

        for _ in range(self.generations):
            population = []
            for _ in range(population_size):
                individual = {
                    'population_size': self.random_param(self.parameter_ranges['population_size']),
                    'crossover_rate': self.random_param(self.parameter_ranges['crossover_rate']),
                    'mutation_rate': self.random_param(self.parameter_ranges['mutation_rate'])
                }
                score = self.fitness_function(individual)
                population.append((individual, score))

                if score < best_score:
                    best_score = score
                    best_params = individual

        return best_params
