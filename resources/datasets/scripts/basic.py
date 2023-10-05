# Standard imports
import os

# Third-party imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Define function
def f(x):
    return np.sin(2.0 * np.pi * x)


# Parameters
noise = 0.1
n = 10
datasets_dir = "datasets"
campaign_dir = os.path.join("campaigns", "basic")
train_file = os.path.join(datasets_dir, "basic.csv")
eval_file = os.path.join(campaign_dir, "eval.csv")
seed = 123

# Calculations
np.random.seed(seed)

# Create data
x_data = np.random.uniform(0.0, 1.0, n)
y_data = f(x_data) + np.random.randn(n) * noise

# Save data to csv
df = pd.DataFrame({"x": x_data, "y": y_data})
df.to_csv(train_file, index=False)
print("Dataframe:\n", df)

# Save ... data to csv
x_eval = np.linspace(0.0, 1.0, 128)
df = pd.DataFrame({"x": x_eval})
df.to_csv(eval_file, index=False)

# Plot data
plt.plot(x_data, y_data, "o", color="C0", label="data")
plt.plot(x_eval, f(x_eval), "-", color="C0", label="truth")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
