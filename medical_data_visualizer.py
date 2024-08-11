import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df = None
# Add 'overweight' column
df['overweight'] = None

# Normalize data by making the  0 always good and 1 always bad. If the value of 'cholesterol' or 'glucose' is 1, make the value 0. If the value is more than 1, make the value 1.
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'glucose', 'smoke', 'alcohol', 'active', and 'overweight'.
    df_cat = None

    # Group and reformat the data to split it by 'cardio vascular disease'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None
    # Draw the catplot with 'sns.catplot()'

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig
def draw_heat_map():
    # Clean the data
    df_heat = None

    corr = None

    mask = None

    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'
    fig.savefig('heatmap.png')
    return fig
