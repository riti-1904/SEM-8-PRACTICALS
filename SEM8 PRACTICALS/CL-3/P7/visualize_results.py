# visualize_results.py

import matplotlib.pyplot as plt

def visualize_predictions(y_true, y_pred):
    plt.figure(figsize=(8, 4))
    plt.plot(y_true, 'o-', label="Actual")
    plt.plot(y_pred, 'x--', label="Predicted")
    plt.title("Structural Damage Classification (AIRS)")
    plt.xlabel("Sample Index")
    plt.ylabel("Label (0 = Healthy, 1 = Damaged)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
