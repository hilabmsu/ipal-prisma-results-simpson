import utils as utils

INSTRUMENT_CODE = 'ues'
XR_CONDITIONS = ['ph', 'ar', 'mr', 'vr']
SCORING_SUBSCALES=['fa', 'pu', 'ae', 'rw', 'g']

def main(cleaned_responses_long, figures_path):
    wide_responses_by_condition = utils.create_wide_responses_by_condition(cleaned_responses_long, INSTRUMENT_CODE, XR_CONDITIONS)

    # TODO: Determine data imputation and exclusion criteria

    # score responses by condition for this instrument
    for dataframe, xr_condition in zip(wide_responses_by_condition, XR_CONDITIONS):
        add_eus_score_column(dataframe, INSTRUMENT_CODE, xr_condition)

    # summarize response scores by subscale for each condition
    scores_by_condition = utils.combine_scores_by_condition(wide_responses_by_condition, INSTRUMENT_CODE, XR_CONDITIONS, SCORING_SUBSCALES)

    # Print response and summary dataframes
    utils.print_scores_by_condition(wide_responses_by_condition, INSTRUMENT_CODE)
    utils.print_score_summary_for_instrument(scores_by_condition, INSTRUMENT_CODE)

    # Generate visualizations and summary stats for data exploration
    utils.create_pirate_plots(scores_by_condition, INSTRUMENT_CODE, XR_CONDITIONS, SCORING_SUBSCALES, figures_path)

def add_eus_score_column(responses_wide, instrument_code, xr_condition):
    '''
    The UES short form has 12 questions. Columns 4-6 (ues-04, ues-05, ues-06) are reverse scored before making calculations.
    A general score (G) averages all twelve question, and four subscale average three questions.
    Focused Attentions (FA) averages columns 1-3. Perceived Usability (PU) averages columns 4-6.
    Aesthetic Elements (AE) averages columns 7-9. Reward Factor (RW) averages columns 10-12.
    :param responses_wide: The dataframe for a specific XR immersion level
    :param instrument: A reference to the specific instrument
    :param xr_condition: A reference to the specific XR immersion level
    '''
    prefix = f"{xr_condition}-{instrument_code}"
    items = responses_wide.iloc[:, 0:12].copy()

    # reverse scoring
    reversed_items = ['ues-04', 'ues-05', 'ues-06']
    items =  responses_wide.iloc[:, 0:12].copy()
    items[reversed_items] = 6 - items[reversed_items]

    responses_wide[f'{prefix}-fa-score'] = items.iloc[:, 0:3].mean(axis=1, skipna=False)
    responses_wide[f'{prefix}-pu-score'] = items.iloc[:, 3:6].mean(axis=1, skipna=False)
    responses_wide[f'{prefix}-ae-score'] = items.iloc[:, 6:9].mean(axis=1, skipna=False)
    responses_wide[f'{prefix}-rw-score'] = items.iloc[:, 9:12].mean(axis=1, skipna=False)
    responses_wide[f'{prefix}-g-score'] = items.mean(axis=1, skipna=False)

if __name__ == "__main__":
    main()