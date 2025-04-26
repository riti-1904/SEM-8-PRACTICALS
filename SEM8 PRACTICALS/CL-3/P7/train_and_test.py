# train_and_test.py

from data_generator import generate_dummy_data
from airs import AIRS
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Generate Data
X, y = generate_dummy_data(samples=200, features=10)

# Step 2: Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the AIRS model
airs = AIRS(num_detectors=20, hypermutation_rate=0.1)
airs.train(X_train, y_train)

# Step 4: Predict
y_pred = airs.predict(X_test)
from visualize_results import visualize_predictions
visualize_predictions(y_test, y_pred)


# Step 5: Accuracy Evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
