import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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
