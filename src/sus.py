import utils as utils
import pandas as pd

INSTRUMENT_CODE = 'sus'
XR_CONDITIONS = ['ph', 'ar', 'mr', 'vr']
SCORING_SUBSCALES=['total']

def main(cleaned_responses_long, figures_path):
    wide_responses_by_condition = utils.create_wide_responses_by_condition(cleaned_responses_long, INSTRUMENT_CODE, XR_CONDITIONS)

    # TODO: Determine data imputation and exclusion criteria

    # score each dataframe for this instrument
    for dataframe, xr_condition in zip(wide_responses_by_condition, XR_CONDITIONS):
        add_sus_score_column(dataframe, INSTRUMENT_CODE, xr_condition)

    # Create a single table of SUS Scores to use with data visualizations
    scores_by_condition = utils.combine_scores_by_condition(wide_responses_by_condition, INSTRUMENT_CODE, XR_CONDITIONS, SCORING_SUBSCALES)

    # Print response and summary dataframes
    utils.print_scores_by_condition(wide_responses_by_condition, INSTRUMENT_CODE)
    utils.print_score_summary_for_instrument(scores_by_condition, INSTRUMENT_CODE)

    # Generate visualizations and summary stats for data exploration
    utils.create_pirate_plots(scores_by_condition, INSTRUMENT_CODE, XR_CONDITIONS, SCORING_SUBSCALES, figures_path)

def add_sus_score_column(responses_wide, instrument_code, xr_condition):
    """ # Odd-numbered SUS items are positively worded, so subtract 1.
        # Even-numbered SUS items are negatively worded, so reverse score by subtracting from 5.
        # Add 1 because item_position is zero-based"""
    prefix = f"{xr_condition}-{instrument_code}"
    summed_item_points = pd.Series(0.0, index=responses_wide.index)

    for item_position in range(10):
        item_responses = responses_wide.iloc[:, item_position]
        if (item_position + 1) % 2 ==1:
            summed_item_points += item_responses - 1
        else:
            summed_item_points += 5 - item_responses

    responses_wide[f"{prefix}-total-score"] = summed_item_points * 2.5

if __name__ == "__main__":
    main()