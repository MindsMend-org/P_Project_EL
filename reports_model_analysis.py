# PRIVATE AND CONFIDENTIAL [Intellectual Property Of Brett Palmer mince@foldingcircles.co.uk]
# [No Copying Or Reading Or Use Permitted !]
"""
Copyright (c) 2023, Brett Palmer (Mince@foldingcircles.co.uk)

All rights reserved. No permission is granted for anyone, except the software owner, Brett Palmer, to use, copy, modify,
distribute, sublicense, or otherwise deal with the software in any manner.

Any unauthorized use, copying, or distribution of this software without the explicit written consent of the software
owner is strictly prohibited.

For permission requests, please contact the software owner, Brett Palmer, at Mince@foldingcircles.co.uk.
"""

# FoldingCircles Making The Unknown Known
import pandas as pd
import glob
import matplotlib.pyplot as plt

__version__ = "0.0.004"
print(f'reports_model_analysis.py {__version__}')

# Step 1: Load CSV Files
file_paths = glob.glob('reports/report_history_*.csv')

# List to hold individual DataFrames
data_frames = []

# Load each CSV file into a DataFrame and append to the list
for file_path in file_paths:
    df = pd.read_csv(file_path)
    data_frames.append(df)

# Step 2: Combine DataFrames
combined_df = pd.concat(data_frames, ignore_index=True)

# Step 3: Perform Data Analysis or Processing
# Example: Displaying the first few rows of the combined DataFrame
print(combined_df.head())

# If you want to save the combined DataFrame to a new CSV file
combined_df.to_csv('reports/combined_report_history.csv', index=False)


def count_predictions_and_matches(df):
    """
    Counts the number of predictions and matches for each model.

    Args:
    df (pd.DataFrame): Combined DataFrame containing all predictions and results.

    Returns:
    pd.DataFrame: DataFrame with the counts of predictions and matches for each model.
    """

    def count_matches(row):
        predicted = set(row['indices'])
        actual = set(row['label'])
        return len(predicted & actual)

    df['matches'] = df.apply(count_matches, axis=1)

    model_stats = df.groupby('el_model').agg(
        predictions=('indices', 'count'),
        matches=('matches', 'sum')
    ).reset_index()

    return model_stats


def calculate_statistics(df):
    """
    Calculates accuracy and standard deviation for each model.

    Args:
    df (pd.DataFrame): DataFrame with counts of predictions and matches for each model.

    Returns:
    pd.DataFrame: DataFrame with accuracy and standard deviation for each model.
    """
    df['accuracy'] = df['matches'] / df['predictions']
    df['std_deviation'] = df['accuracy'].std()

    return df


def plot_performance(df):
    """
    Plots the performance of each model.

    Args:
    df (pd.DataFrame): DataFrame with accuracy and standard deviation for each model.
    """
    plt.figure(figsize=(10, 6))

    plt.bar(df['el_model'], df['accuracy'], yerr=df['std_deviation'], capsize=5)
    plt.xlabel('Model Name')
    plt.ylabel('Accuracy')
    plt.title('Model Performance: Accuracy and Standard Deviation')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig('reports/model_performance.png')
    plt.show()


def plot_full_lottery_percent(df):
    """
    Plots the full 7 lottery number percentage for each model over time.

    Args:
    df (pd.DataFrame): Combined DataFrame with all predictions and results.
    """

    def calculate_full_lottery_percent(row):
        predicted = set(row['indices'])
        actual = set(row['label'])
        intersection_count = len(predicted & actual)
        return (intersection_count / min(len(predicted), 7)) * 100

    # Ensure the indices and label columns are treated as lists
    df['indices'] = df['indices'].apply(lambda x: eval(x) if isinstance(x, str) else x)
    df['label'] = df['label'].apply(lambda x: eval(x) if isinstance(x, str) else x)

    df['full_lottery_percent'] = df.apply(calculate_full_lottery_percent, axis=1)

    # Clip percentages to a maximum of 100
    df['full_lottery_percent'] = df['full_lottery_percent'].clip(upper=100)

    models = df['el_model'].unique()

    plt.figure(figsize=(12, 8))

    for model in models:
        model_df = df[df['el_model'] == model]
        plt.plot(model_df.index, model_df['full_lottery_percent'], marker='o', label=model)

    plt.xlabel('Prediction Instance')
    plt.ylabel('Full 7 Lottery Number %')
    plt.title('Full 7 Lottery Number % Over Time')
    plt.legend(title='Model')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('reports/full_lottery_percent.png')
    plt.show()


def plot_model_prediction_percent(df):
    """
    Plots each model's prediction percentage for each prediction over time.

    Args:
    df (pd.DataFrame): Combined DataFrame with all predictions and results.
    """
    df['model_prediction_percent'] = df.apply(
        lambda row: (len(set(row['indices']) & set(row['label'])) / len(row['indices'])) * 100, axis=1)

    models = df['el_model'].unique()

    plt.figure(figsize=(12, 8))

    for model in models:
        model_df = df[df['el_model'] == model]
        plt.plot(model_df.index, model_df['model_prediction_percent'], marker='o', label=model)

    plt.xlabel('Prediction Instance')
    plt.ylabel('Model Prediction %')
    plt.title('Model Prediction % Over Time')
    plt.legend(title='Model')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('reports/model_prediction_percent.png')
    plt.show()


# df has the necessary columns: 'el_model', 'indices', 'label'
model_stats_df = count_predictions_and_matches(combined_df)
model_performance_df = calculate_statistics(model_stats_df)
plot_performance(model_performance_df)
plot_full_lottery_percent(combined_df)
plot_model_prediction_percent(combined_df)
