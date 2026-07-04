import pandas as pd
import config
from utils import validate_columns
from figures import pirate_plot
from output import save_markdown, save_latex

# Rows to exclude per intervention based on review of raw UES data
DROP_ROWS = {
    'PH': [],
    'AR': [],
    'MR': [],
    'VR': []
}

INTERVENTIONS = {
    'Phone': ('PH', config.UES_COLS_PH),
    'AR':    ('AR', config.UES_COLS_AR),
    'MR':    ('MR', config.UES_COLS_MR),
    'VR':    ('VR', config.UES_COLS_VR),
}

# Sum all responses (UES-04, UES-05 and UES-06 are reverse coded) and divide by 12
def calc_ues(subset):
   return

# Sum questions EUS-01 to EUS-03 and divide by 3
def calc_ues_focused_attention(subset):
   return

# Sum questions EUS-04 to EUS-06 (reverse coded) and divide by 3
def calc_ues_perceived_usability(subset):
   return

# Sum questions EUS-07 to EUS-09 and divide by 3
def calc_ues_aesthetic_appeal(subset):
   return

# Sum questions EUS-10 to EUS-12 and divide by 3
def calc_ues_reward(subset):
   return

def validate_ues_scores(df, label):
    scores = df['ues_score']
    invalid = ~ scores.between(0, 100)
    if invalid.any():
        raise ValueError(
            f"{label} UES scores out of valid range (0-100):\n"
            f"  Row indices: {list(df.index[invalid])}\n"
            f"  Values: {list(scores[invalid])}"
        )
    return

def compute_ues(df, label):
    validate_columns(df, label)
    result = df.assign(ues_score=calc_ues)
    return result

def prepare_subset(df, label, cols):
    subset = df[cols]
    if label in DROP_ROWS:
        subset = subset.drop(DROP_ROWS[label])
    return compute_ues(subset, label)

def print_raw_data(subsets):
    for label, subset in subsets.items():
        print(f"\n--- {label} Raw SUS Data ---")
        print(subset.to_string(index=False))

def build_score_table(scored_dfs, labels):
    first = list(scored_dfs.values())[0]
    frames = [first['Participant']] + [scored_dfs[label]['ues_score'] for label in labels]
    result = pd.concat(frames, axis=1)
    result.columns = ['Participant'] + labels
    return result

def print_means(means, labels):
    for label, mean in zip(labels, means):
        print(f"{label} UES score: {mean: .2f}")

def run(df):
    # Prepare raw subsets with excluded rows removed
    subsets = {
        label: prepare_subset(df, key, cols)
        for label, (key, cols) in INTERVENTIONS.items()
    }

    #print raw data for review before scoring
    print_raw_data(subsets)

    #compute UES scores
    # scored = {
    #     label: compute_ues(subset, label)
    #     for label, subset in subsets.items()
    # }
    #
    # labels = list(scored.keys())
    # means = [scored[label]['ues_score'].mean() for label in labels]
    # scores = [scored][label][['ues_score'] for label in labels]
    #
    # df_ues_ind_scores = build_score_table(scored, labels)
    #
    # print_means(means, labels)
    # print("\nInividual Scores")
    # print(df_ues_ind_scores.to_string(index=False))

    # Generate data tables in markdown and LaTeX and save to file
    # save_markdown(df_ues_ind_scores, 'table_ues_ind_scores.md', False)
    # save_latex(df_ues_ind_scores, 'table_ues_ind_scores.md', 'UES Participant Scores by Intervention')

    # Create Figures and save to file
    # pirate_plot(
    #     data=scores,
    #     labels=labels,
    #     title='UES Score Distribution by Intervention',
    #     ylabel='UES Score',
    #     output_path=config.FIGURES_PATH / 'ues_pirate.png'
    # )
