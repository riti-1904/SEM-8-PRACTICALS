
from deap_optimizer import run_deap_optimization
from deap import tools
if __name__ == "__main__":
    generations = 20
    population = run_deap_optimization(generations=generations, pop_size=50)

    # Best result
    best_ind = tools.selBest(population, k=1)[0]
    print("Best individual:", best_ind)
    print("Best fitness:", best_ind.fitness.values[0])