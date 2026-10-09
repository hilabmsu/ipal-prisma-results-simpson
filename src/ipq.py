import utils as utils

INSTRUMENT_CODE = 'ipq'
XR_CONDITIONS = ['ar', 'mr', 'vr']
SCORING_SUBSCALES=['gp', 'sp', 'inv', 'real', 'total']

def main(cleaned_responses_long, figures_path):
    wide_responses_by_condition = utils.create_wide_responses_by_condition(cleaned_responses_long, INSTRUMENT_CODE, XR_CONDITIONS)

    # TODO: Determine data imputation and exclusion criteria

    # score each dataframe for this instrument and create summary dataframe
    for dataframe, xr_condition in zip(wide_responses_by_condition, XR_CONDITIONS):
        add_ipq_score_column(dataframe, INSTRUMENT_CODE, xr_condition)

    scores_by_condition = utils.combine_scores_by_condition(wide_responses_by_condition, INSTRUMENT_CODE, XR_CONDITIONS, SCORING_SUBSCALES)

    # Print response and summary dataframes
    utils.print_scores_by_condition(wide_responses_by_condition, INSTRUMENT_CODE)
    utils.print_score_summary_for_instrument(scores_by_condition, INSTRUMENT_CODE)

    # Generate visualizations and summary stats for data exploration
    utils.create_pirate_plots(scores_by_condition, INSTRUMENT_CODE, XR_CONDITIONS, SCORING_SUBSCALES, figures_path)

def add_ipq_score_column(responses_wide, instrument_code, xr_condition):
    '''
    The IPQ short form has 14 questions with 5 subscales: General Presence (GP) question 1,
    Spacial Presence (SP) questions 2-6, Involvement (INV) questions 7-10 , Experienced Realism (REAL)
    questions 11-14, and Total (total) questions 1-14. This implementation used a five-point
    scale ranging from -2 to +2. Three questions are reverse scored (Item[reversed] = 5 - Item[raw])
    subscale SP2 (question 3), subscale INV3 (question 9), subscale REAL1 (question 11).
    :param responses_wide: The dataframe for a specific XR immersion level
    :param instrument: A reference to the specific instrument
    :param xr_condition: A reference to the specific XR immersion level
    '''
    prefix = f"{xr_condition}-{instrument_code}"
    items = responses_wide.iloc[:, 0:14].copy()

    # reverse scoring
    reversed_items = ['ipq-03', 'ipq-09', 'ipq-11']
    items =  responses_wide.iloc[:, 0:14].copy()
    items[reversed_items] = 5 - items[reversed_items]

    responses_wide[f'{prefix}-gp-score'] = items.iloc[:, 0]
    responses_wide[f'{prefix}-sp-score'] = items.iloc[:, 1:6].mean(axis=1, skipna=False)
    responses_wide[f'{prefix}-inv-score'] = items.iloc[:, 6:10].mean(axis=1, skipna=False)
    responses_wide[f'{prefix}-real-score'] = items.iloc[:, 10:14].mean(axis=1, skipna=False)
    responses_wide[f'{prefix}-total-score'] = items.mean(axis=1, skipna=False)

if __name__ == "__main__":
    main()