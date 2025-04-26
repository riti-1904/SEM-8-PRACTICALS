
from genetic_config import toolbox
from deap import algorithms

def run_deap_optimization(generations=20, pop_size=50):
    population = toolbox.population(n=pop_size)

    for gen in range(generations):
        
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
        fits = toolbox.map(toolbox.evaluate, offspring)
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
        population = toolbox.select(offspring, k=len(population))
    return population