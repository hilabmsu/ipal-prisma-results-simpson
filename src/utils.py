import config
import figures
import numpy as np
import pandas as pd

def exclude_participants(responses, excluded_participant_ids):
    is_excluded = responses['participant_id'].isin(excluded_participant_ids)
    return responses[~is_excluded]

def replace_missing_codes_with_nan(responses):
    is_missing_code =  responses.isin(list(config.MISSING_VALUES_CATEGORIES))
    return responses.mask(is_missing_code, np.nan)

def create_wide_responses_by_condition(long_responses, instrument_code, xr_conditions):
    wide_responses = []
    for xr_condition in xr_conditions:
        session_data = select_instrument_condition_responses(long_responses, instrument_code, xr_condition)
        session_data = pivot_to_wide(session_data)
        wide_responses.append(session_data)
    return wide_responses

def select_instrument_condition_responses(original_data, instrument_code, xr_condition):
    condition_responses = original_data[
        (original_data['instrument'] == instrument_code) &
        (original_data['condition'] == xr_condition)
    ]
    return condition_responses

def pivot_to_wide(responses_long):
    responses_wide = responses_long.pivot(
        index='participant_id',
        columns='item_id',
        values='value'
    )
    return responses_wide

def combine_scores_by_condition(wide_responses_by_condition, instrument_code, xr_conditions, scoring_subscales):
    score_by_condition = {}
    for subscale in scoring_subscales:
        subscale_score_by_condition_dict = {}
        for dataframe, xr_condition in zip(wide_responses_by_condition, xr_conditions):
            score_column_name = f"{xr_condition}-{instrument_code}-{subscale}-score"
            subscale_score_by_condition_dict[xr_condition] = dataframe[score_column_name]
        score_by_condition[subscale] = pd.DataFrame(subscale_score_by_condition_dict)
    return score_by_condition

def print_scores_by_condition(scored_condition, instrument_code):
    for condition in scored_condition:
        print(f"{instrument_code.upper()} scored responses for CONDITION")
        print(condition.to_string())
        print()
        print(condition.describe().to_string())
        print('\n' * 2)

def print_score_summary_for_instrument(scored_summary, instrument_code):
    for score_type, summary_dataframe in scored_summary.items():
        print(f"Summary {instrument_code.upper()} Scores for {score_type.upper()} Scale")
        print(summary_dataframe.to_string())
        print()
        print(summary_dataframe.describe().to_string())
        print()

def create_pirate_plots(scored_responses, instrument_code, xr_conditions, scoring_subscales, figures_path):
    # Pirate Plots
    for type in scoring_subscales:
        score_series_per_condition = [scored_responses[type][level].dropna() for level in xr_conditions]
        figures.pirate_plot(score_series_per_condition, xr_conditions,
            f"{instrument_code.upper()} Scores by XR Level and Subscale ({type.upper()})",
            f"{instrument_code.upper()} Score",
            f"{figures_path}/{instrument_code}-{type}-pirate")
