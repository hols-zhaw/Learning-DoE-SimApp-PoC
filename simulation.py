import numpy as np
import pandas as pd


def simulate_yogurt_production(design, factors, seed=123456789):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(
        [
            {
                "Milk_Fat_Content": fat,
                "Fermentation_Time": time,
                "Temperature": temp,
                "Replication": rep,
                "Sample": sam,
                "pH_Value": (
                    4.5 + 0.1 * fat - 0.05 * time + 0.02 * temp + rng.normal(0, 0.1)
                ),
                "Consistency": (
                    10 + 0.5 * fat - 0.3 * time + 0.1 * temp + rng.normal(0, 1)
                ),
                "Taste_Score": (
                    7 + 0.2 * fat - 0.1 * time + 0.05 * temp + rng.normal(0, 0.5)
                ),
            }
            for fat in factors["Milk_Fat_Content"]
            for time in factors["Fermentation_Time"]
            for temp in factors["Temperature"]
            for rep in range(1, design["n_replications"] + 1)
            for sam in range(1, design["n_samples"] + 1)
        ]
    )

    factors = [key for key, val in factors.items() if len(val) > 1]
    responses = ["pH_Value", "Consistency", "Taste_Score"]

    return df, factors, responses
