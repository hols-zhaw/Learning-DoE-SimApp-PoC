import streamlit as st
from simulation import simulate_yogurt_production
from analysis import analyze_data
from ui import display_ui, display_results


def main():
    design, factor_values = display_ui()

    if st.sidebar.button("Run Simulation"):
        df, factors, responses = simulate_yogurt_production(design, factor_values)
        analysis_results = analyze_data(df, factors, responses, design["alpha"])
        display_results(df, analysis_results, factors)


if __name__ == "__main__":
    main()
