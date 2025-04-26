from hybrid_ga_nn import *
from simple_genetic_algorithm import GeneticAlgorithm

# Sample data - Normally this would be real experimental coconut milk data
X = np.random.rand(100, 5)   # 100 samples, 5 features
y = np.random.rand(100)      # 100 target values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def fitness_function(params):
    pop_size = params['population_size']
    crossover = params['crossover_rate']
    mutation = params['mutation_rate']

    # Simulate that GA tunes NN hyperparameters indirectly
    nn_model = MLPRegressor(hidden_layer_sizes=(50,), activation='relu', solver='adam', max_iter=300)
    nn_model.fit(X_train, y_train)
    y_pred = nn_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse

param_ranges = {
    'population_size': (50, 100),
    'crossover_rate': (0.6, 0.9),
    'mutation_rate': (0.01, 0.1)
}

ga = GeneticAlgorithm(fitness_function, param_ranges, generations=10)
best_params = ga.optimize()

print("Best Parameters Found:", best_params)
