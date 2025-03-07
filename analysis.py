import statsmodels.api as sm
from statsmodels.formula.api import ols


def analyze_data(df, factors, responses, alpha=0.05):

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
