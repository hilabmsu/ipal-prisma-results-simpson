import config
import utils as utils
import sus
import ues
import ipq
import ais
from functools import partial
import pandas as pd

# Retrieve and preprocess data in long format
raw_responses_long = pd.read_csv(f'{config.DATA_PATH}/ipal-survey-results-long.csv')
cleaned_responses_long = utils.exclude_participants(raw_responses_long, config.EXCLUDED_PARTICIPANT_IDS).copy()
cleaned_responses_long = utils.replace_missing_codes_with_nan(cleaned_responses_long).copy()

menu_options = {
    '1': {"label": "System Usability Scale (SUS)", "action": partial(sus.main,cleaned_responses_long, config.FIGURES_PATH)},
    '2': {"label": "User Engagement Scale (UES)", "action": partial(ues.main, cleaned_responses_long, config.FIGURES_PATH)},
    '3': {"label": "iGroup Presence Questionnaire (IPQ)", "action": partial(ipq.main, cleaned_responses_long, config.FIGURES_PATH)},
    '4': {"label": "iPAL Application Evaluation (AIS)", "action": partial(ais.main, cleaned_responses_long, config.FIGURES_PATH)},
    '0': {"label": "Exit program", "action": exit},
}
while True:
    # menu user interface
    print()
    print("Main Menu")
    print("=" * 50)
    for key in menu_options:
        print(f"{key}. {menu_options[key]['label']}")
    choice = input("\nEnter the number of you selection: ").strip().lower()

    # execute menu actions
    if choice in menu_options:
        menu_options[choice]['action']()
    else:
        print('Invalid choice. Please choose again')