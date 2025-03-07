import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols


def simulate(design, factors, seed=123456789):
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




def analyze(df, factors, responses, alpha=0.05):

    # factors_str = " + ".join(f"C({f})" for f in factors)
    factors_str = " + ".join(factors)

    # Perform ANOVA for each response variable
    results = {}
    for response in responses:
        model_str = f"{response} ~{factors_str}"
        model = ols(model_str, data=df).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        
        
        # Calculate Mean Square (MS)
        anova_table['MS'] = anova_table['sum_sq'] / anova_table['df']
        
        # Calculate Eta-Squared (eta_sq)
        anova_table['eta_sq'] = anova_table['sum_sq'] / anova_table['sum_sq'].sum()

        
        # anova_table.rename(columns={"PR(>F)": "p-value"}, inplace=True)
        
        # Reorder columns to include MS and eta_sq
        anova_table = anova_table[['sum_sq', 'df', 'MS', 'F', 'PR(>F)', 'eta_sq']]

        anova_table["significant"] = anova_table["PR(>F)"] < alpha
        
        # Round p-value to 2 more digits than alpha
        anova_table["PR(>F)"] = anova_table["PR(>F)"].round(len(str(alpha).split(".")[1]) + 3)

        results[response] = anova_table

    return results


def display_ui():
    st.title("Yogurt Production Experiment")

    st.sidebar.header("Experimental Design")
    design = {
        "n_replications": st.sidebar.number_input(
            "Number of Replications", min_value=1, max_value=100, value=3
        ),
        "n_samples": st.sidebar.number_input(
            "Number of Samples", min_value=1, max_value=100, value=5
        ),
        "alpha": st.sidebar.number_input(
            "Significance Level", min_value=0.0, max_value=1.0, value=0.05
        ),
    }

    st.sidebar.header("Factors")
    factor_values = {
        "Milk_Fat_Content": st.sidebar.multiselect(
            "Milk Fat Content (%)", options=[1.5, 3.5], default=[1.5, 3.5]
        ),
        "Fermentation_Time": st.sidebar.multiselect(
            "Fermentation Time (hours)", options=[6, 8, 10], default=[6, 8, 10]
        ),
        "Temperature": st.sidebar.multiselect(
            "Temperature (°C)", options=[37, 42], default=[37, 42]
        ),
    }

    return design, factor_values


def display_results(df, analysis_results, factors):
    st.header("Simulated Data")
    st.write(df)

    st.header("ANOVA Results")

    for response, anova_table in analysis_results.items():
        response_label = str.replace(response, "_", " ")
        st.subheader(response_label)
        st.write(anova_table)

        fig, ax = plt.subplots()
        df.boxplot(column=response, by=factors, ax=ax, rot=45)
        plt.ylabel(response_label)
        plt.title("")
        plt.suptitle("")
        st.pyplot(fig)

def main():
    design, factor_values = display_ui()

    if st.sidebar.button("Run Simulation"):
        df, factors, responses = simulate(design, factor_values)
        analysis_results = analyze(df, factors, responses, design["alpha"])
        display_results(df, analysis_results, factors)


if __name__ == "__main__":
    main()
