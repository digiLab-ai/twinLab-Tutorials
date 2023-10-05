# Standard imports
import os

# Third-party imports
import numpy as np
import pandas as pd

# Parameters
n = 10
seed = 123

# Seed random number generator
np.random.seed(seed)

# Generate data for evaluation
# This creates samples from the posterior given some external dataset
# The posterior is assumed to be a independent normal distributions
# Covariance ignored for simplicity
E1 = np.random.normal(0.81, 0.01, n)
E2 = np.random.normal(0.95, 0.01, n)
E3 = np.random.normal(1.45, 0.03, n)
n1 = np.random.normal(0.001, 0.0001, n)
n2 = np.random.normal(0.0008, 0.0001, n)
df = pd.DataFrame(
    np.column_stack((E1, E2, E3, n1, n2)), columns=["E1", "E2", "E3", "n1", "n2"]
)

# Save data to CSV file
campaign_dir = os.path.join("campaigns", "ukaea")
file = os.path.join(campaign_dir, "post.csv")
df.to_csv(file, index=False)
