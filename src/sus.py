import pandas as pd
import config
from utils import validate_columns
from figures import bar_chart, violin_plot, pirate_plot
from output import save_latex, save_markdown

# Rows to exclude from analysis for each intervention type based on review of raw SUS data
# A row is excluded if all the values for that participant are blank.
# TODO: set up multiple imputation is only select values are blank
DROP_ROWS = {
    'PH': [0,3],
    'AR': [0, 3, 10, 19],
    'MR': [0, 3, 10, 19],
    'VR': [0, 10, 19]
}

INTERVENTIONS = {
    'Phone': ('PH', config.SUS_COLS_PH),
    'AR':    ('AR', config.SUS_COLS_AR),
    'MR':    ('MR', config.SUS_COLS_MR),
    'VR':    ('VR', config.SUS_COLS_VR),
}

def calc_sus(subset):
    odd = [subset.columns[i] for i in [1, 3, 5, 7, 9]]
    even = [subset.columns[i] for i in [2, 4, 6, 8, 10]]
    odd_converted = subset[odd] - 1
    even_converted = 5 - subset[even]
    converted = odd_converted.join(even_converted)
    return converted.sum(axis=1) * 2.5

def validate_sus_scores(df, label):
    scores = df['sus_score']
    invalid = ~scores.between(0, 100)
    if invalid.any():
        raise ValueError(
            f"{label} SUS scores out of valid range (0-100):\n"
            f"  Row indices: {list(df.index[invalid])}\n"
            f"  Values: {list(scores[invalid])}"
        )

def compute_sus(df, label):
    validate_columns(df, label)
    result = df.assign(sus_score=calc_sus)
    return result

def prepare_subset(df, label, cols):
    subset = df[cols]
    if label in DROP_ROWS:
        subset = subset.drop(DROP_ROWS[label])
    return compute_sus(subset, label)

def print_raw_data(subsets):
    for label, subset in subsets.items():
        print(f"\n--- {label} Raw SUS Data ---")
        print(subset.to_string(index=False))

def build_score_table(scored_dfs, labels):
    first = list(scored_dfs.values())[0]
    frames = [first['Participant']] + [scored_dfs[label]['sus_score'] for label in labels]
    result = pd.concat(frames, axis=1)
    result.columns = ['Participant'] + labels
    return result

def print_means(means, labels):
    for label, mean in zip(labels, means):
        print(f"{label} SUS score: {mean: .2f}")

def run(df):
    # Prepare raw subsets with excluded rows removed
    # Create dataframes of survey-specific responses (e.g., VR SUS Survey).
    subsets = {
        label: prepare_subset(df, key, cols)
        for label, (key, cols) in INTERVENTIONS.items()
    }

    # Print raw data for review before scoring
    print_raw_data(subsets)

    # Compute SUS scores
    scored = {
        label: compute_sus(subset, label)
        for label, subset in subsets.items()
    }

    labels = list(scored.keys())
    means = [scored[label]['sus_score'].mean() for label in labels]
    scores = [scored[label]['sus_score'] for label in labels]

    df_sus_ind_scores = build_score_table(scored, labels)

    print_means(means, labels)
    print("\nIndividual Scores")
    print(df_sus_ind_scores.to_string(index=False))

    # Generate data tables in markdown and LaTeX and save to file
    save_markdown(df_sus_ind_scores, 'table_sus_ind_scores.md', False)
    save_latex(df_sus_ind_scores, 'table_sus_ind_scores.tex', 'SUS Participant Scores by Intervention')

    # Create Figures and save to file
    bar_chart(
        values = means,
        labels = labels,
        title = 'SUS Scores by Intervention',
        ylabel = 'Mean SUS Score',
        output_path = config.FIGURES_PATH / 'sus_scores.png'
    )

    violin_plot(
        data = scores,
        labels = labels,
        title = 'SUS Score Distribution by Intervention',
        ylabel = 'SUS score',
        output_path = config.FIGURES_PATH / 'sus_violin.png'
    )

    pirate_plot(
        data=scores,
        labels=labels,
        title='SUS Score Distribution by Intervention',
        ylabel='SUS Score',
        output_path=config.FIGURES_PATH / 'sus_pirate.png'
    )