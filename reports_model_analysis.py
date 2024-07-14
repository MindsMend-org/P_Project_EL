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
import numpy as np

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

# Create prediction_instance column
combined_df['prediction_instance'] = combined_df.groupby('el_model').cumcount() + 1

# Step 3: Perform Data Analysis or Processing
# Example: Displaying the first few rows of the combined DataFrame
print(combined_df.head())

# ave the combined DataFrame to a new CSV file
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

def plot_performance(df, combined_df):
    """
    Plots the performance of each model including a random model.

    Args:
    df (pd.DataFrame): DataFrame with accuracy and standard deviation for each model.
    combined_df (pd.DataFrame): Combined DataFrame containing all predictions and results.
    """
    # Generate random predictions based on the actual count of prediction instances
    prediction_count = len(combined_df)
    np.random.seed(0)  # For reproducibility
    random_predictions = [np.random.choice(range(1, 50), size=5, replace=False) for _ in range(prediction_count)]

    # Create a DataFrame for the random model
    random_df = pd.DataFrame({
        'el_model': ['random'] * prediction_count,
        'indices': random_predictions,
        'label': combined_df['label'].tolist()
    })

    # Calculate matches and statistics for the random model
    random_df['matches'] = random_df.apply(lambda row: len(set(row['indices']) & set(row['label'])), axis=1)
    random_stats = pd.DataFrame({
        'el_model': ['random'],
        'predictions': [len(random_df)],
        'matches': [random_df['matches'].sum()]
    })
    random_stats['accuracy'] = random_stats['matches'] / random_stats['predictions']
    random_stats['std_deviation'] = random_df['matches'].std()

    # Append the random model stats to the original stats
    df = pd.concat([df, random_stats], ignore_index=True)

    # Plot the performance
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
    Plots the full 7 lottery number percentage for each model over the draw history.

    Args:
    df (pd.DataFrame): Combined DataFrame with all predictions and results.
    """

    def calculate_full_lottery_percent(row):
        predicted = set(row['indices'])
        actual = set(row['label'])
        intersection_count = len(predicted & actual)
        return (intersection_count / min(len(predicted), 7)) * 100

    df['indices'] = df['indices'].apply(lambda x: eval(x) if isinstance(x, str) else x)
    df['label'] = df['label'].apply(lambda x: eval(x) if isinstance(x, str) else x)

    df['full_lottery_percent'] = df.apply(calculate_full_lottery_percent, axis=1)
    df['full_lottery_percent'] = df['full_lottery_percent'].clip(upper=100)

    models = df['el_model'].unique()
    predictions = df['prediction_instance'].unique()

    bar_width = 0.2
    plt.figure(figsize=(12, 8))

    for i, model in enumerate(models):
        model_df = df[df['el_model'] == model]
        indices = model_df['prediction_instance'] + i * bar_width
        plt.bar(indices, model_df['full_lottery_percent'], width=bar_width, label=model)

    plt.xlabel('Prediction Instance')
    plt.ylabel('Full 7 Lottery Number %')
    plt.title('Full 7 Lottery Number % Over Draws')
    plt.legend(title='Model')
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(ticks=predictions, labels=predictions)

    plt.savefig('reports/full_lottery_percent.png')
    plt.show()

def plot_model_prediction_percent(df):
    """
    Plots each model's prediction percentage for each prediction over the draw history.

    Args:
    df (pd.DataFrame): Combined DataFrame with all predictions and results.
    """

    def calculate_model_prediction_percent(row):
        predicted = set(row['indices'])
        actual = set(row['label'])
        return (len(predicted & actual) / len(predicted)) * 100

    df['indices'] = df['indices'].apply(lambda x: eval(x) if isinstance(x, str) else x)
    df['label'] = df['label'].apply(lambda x: eval(x) if isinstance(x, str) else x)

    df['model_prediction_percent'] = df.apply(calculate_model_prediction_percent, axis=1)

    models = df['el_model'].unique()
    predictions = df['prediction_instance'].unique()

    bar_width = 0.2
    plt.figure(figsize=(12, 8))

    for i, model in enumerate(models):
        model_df = df[df['el_model'] == model]
        indices = model_df['prediction_instance'] + i * bar_width
        plt.bar(indices, model_df['model_prediction_percent'], width=bar_width, label=model)

    plt.xlabel('Prediction Instance')
    plt.ylabel('Model Prediction %')
    plt.title('Model Prediction % Over Draws')
    plt.legend(title='Model')
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(ticks=predictions, labels=predictions)

    plt.savefig('reports/model_prediction_percent.png')
    plt.show()

# Generate the plots
model_stats_df = count_predictions_and_matches(combined_df)
model_performance_df = calculate_statistics(model_stats_df)
plot_performance(model_performance_df, combined_df)
plot_full_lottery_percent(combined_df)
plot_model_prediction_percent(combined_df)
