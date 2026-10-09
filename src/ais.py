import utils as utils

INSTRUMENT_CODE = 'ais'
XR_CONDITIONS = ['ph', 'ar', 'mr', 'vr']
SCORING_SUBSCALES=['cr', 'tr', 'un', 'ea', 'total']

def main(cleaned_responses_long, figures_path):
    wide_responses_by_condition = utils.create_wide_responses_by_condition(cleaned_responses_long, INSTRUMENT_CODE, XR_CONDITIONS)

    # TODO: Determine data imputation and exclusion criteria

    # score each dataframe for this instrument and create summary dataframe
    for dataframe, xr_condition in zip(wide_responses_by_condition, XR_CONDITIONS):
        add_ais_score_column(dataframe, INSTRUMENT_CODE, xr_condition)

    scores_by_condition = utils.combine_scores_by_condition(wide_responses_by_condition, INSTRUMENT_CODE, XR_CONDITIONS, SCORING_SUBSCALES)

    # Print response and summary dataframes
    utils.print_scores_by_condition(wide_responses_by_condition, INSTRUMENT_CODE)
    utils.print_score_summary_for_instrument(scores_by_condition, INSTRUMENT_CODE)

    # Generate visualizations and summary stats for data exploration
    utils.create_pirate_plots(scores_by_condition, INSTRUMENT_CODE, XR_CONDITIONS, SCORING_SUBSCALES, figures_path)

def add_ais_score_column(responses_wide, instrument_code, xr_condition):
    '''
    The AIE has 5 subscales: Craving (cr) question ais-01,
    trigger (tr) questions ais-02, Understanding (un) questions ais-03, and ease (ea)
    questions ais-04, and total (total) questions 1-4.
    :param responses_wide: The dataframe for a specific XR immersion level
    :param instrument: A reference to the specific instrument
    :param xr_condition: A reference to the specific XR immersion level
    '''
    prefix = f"{xr_condition}-{instrument_code}"

    responses_wide[f'{prefix}-cr-score'] = responses_wide['ais-01']
    responses_wide[f'{prefix}-tr-score'] = responses_wide['ais-02']
    responses_wide[f'{prefix}-un-score'] = responses_wide['ais-03']
    responses_wide[f'{prefix}-ea-score'] = responses_wide['ais-04']
    responses_wide[f'{prefix}-total-score'] = responses_wide.iloc[:, 0:4].mean(axis=1, skipna=False)

if __name__ == "__main__":
    main()