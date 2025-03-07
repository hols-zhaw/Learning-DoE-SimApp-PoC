# Learning-DoE-SimApp-PoC

A Proof of Concept for a Simulation-based Learning App for Design of Experiments

This Streamlit app simulates and analyzes yogurt production data to help students learn the basic concepts of Design of Experiments (DoE). The app allows users to specify the number of repetitions, measurements per sample, and various factors to simulate the data. It also provides data visualization and ANOVA analysis.

## Features

-   **Simulation Parameters**: Set the number of repetitions and measurements per sample.
-   **Factors**: Choose different levels for milk fat content, fermentation time, and temperature.
-   **Data Visualization**: View the simulated data and boxplots for each response variable.
-   **ANOVA Analysis**: Perform ANOVA to analyze the effects of different factors on the response variables.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.zhaw.ch/Digital-Labs-Production/Learning-DoE-SimApp-PoC
    cd Learning-DoE-SimApp-PoC
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```
2. Open your web browser and go to `http://localhost:8501` to view the app.

## Directory Structure

```
Learning-DoE-SimApp-PoC/
├── main.py
├── simulation.py
├── analysis.py
└── ui.py
```

## License

This project is licensed under the MIT License.
