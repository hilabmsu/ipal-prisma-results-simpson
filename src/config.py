from pathlib import Path
# Project root
ROOT = Path(__file__).parent.parent

# Data paths
DATA_PATH = ROOT / 'data' / 'processed' / 'ipal-survey-results.csv'

# Output paths
FIGURES_PATH  = ROOT / 'outputs' / 'figures'
MARKDOWN_PATH = ROOT / 'outputs' / 'markdown'
LATEX_PATH    = ROOT / 'outputs' / 'latex'

# Codes for missing values
NOT_APPLICABLE        = -99
LEFT_BLANK            = -98
NOT_DELIVERED         = -97

MISSING_VALUES = [NOT_APPLICABLE, LEFT_BLANK, NOT_DELIVERED]

"""
Survey columns Naming
Abbreviations for intervention types.
-- ph = phone
-- ar = augmented reality
-- mr = mixed reality
-- vr = virtual reality
-- ei = exit interview
"""

# Simulator Sickness Questionnaire
SSQ_COLS = ['Participant', 'SSQ-01', 'SSQ-02', 'SSQ-03', 'SSQ-04', 'SSQ-05']

# Demographics Questionnaire
DM_COLS = ['Participant', 'DM-01', 'DM-02', 'DM-03', 'DM-04', 'DM-05', 'DM-06', 'DM-08', 'DM-09']

# Stability Scale
SS_COLS_AR = ['Participant', 'AR-SS-01', 'AR-SS-02', 'AR-SS-03']
SS_COLS_MR = ['Participant', 'MR-SS-01', 'MR-SS-02', 'MR-SS-03']
SS_COLS_VR = ['Participant', 'VR-SS-01', 'VR-SS-02', 'VR-SS-03']
SS_COLS_EI = ['Participant', 'EI-SS-01', 'EI-SS-02', 'EI-SS-03']

# System Usability Scale
SUS_COLS_PH = ['Participant', 'PH-SUS-01', 'PH-SUS-02', 'PH-SUS-03', 'PH-SUS-04', 'PH-SUS-05', 'PH-SUS-06', 'PH-SUS-07', 'PH-SUS-08', 'PH-SUS-09', 'PH-SUS-10']
SUS_COLS_AR = ['Participant', 'AR-SUS-01', 'AR-SUS-02', 'AR-SUS-03', 'AR-SUS-04', 'AR-SUS-05', 'AR-SUS-06', 'AR-SUS-07', 'AR-SUS-08', 'AR-SUS-09', 'AR-SUS-10']
SUS_COLS_MR = ['Participant', 'MR-SUS-01', 'MR-SUS-02', 'MR-SUS-03', 'MR-SUS-04', 'MR-SUS-05', 'MR-SUS-06', 'MR-SUS-07', 'MR-SUS-08', 'MR-SUS-09', 'MR-SUS-10']
SUS_COLS_VR = ['Participant', 'VR-SUS-01', 'VR-SUS-02', 'VR-SUS-03', 'VR-SUS-04', 'VR-SUS-05', 'VR-SUS-06', 'VR-SUS-07', 'VR-SUS-08', 'VR-SUS-09', 'VR-SUS-10']

# User Experience Scale
UES_COLS_PH = ['Participant', 'PH-UES-01', 'PH-UES-02', 'PH-UES-03', 'PH-UES-04', 'PH-UES-05', 'PH-UES-06', 'PH-UES-07', 'PH-UES-08', 'PH-UES-09', 'PH-UES-10', 'PH-UES-11', 'PH-UES-12']
UES_COLS_AR = ['Participant', 'AR-UES-01', 'AR-UES-02', 'AR-UES-03', 'AR-UES-04', 'AR-UES-05', 'AR-UES-06', 'AR-UES-07', 'AR-UES-08', 'AR-UES-09', 'AR-UES-10', 'AR-UES-11', 'AR-UES-12']
UES_COLS_MR = ['Participant', 'MR-UES-01', 'MR-UES-02', 'MR-UES-03', 'MR-UES-04', 'MR-UES-05', 'MR-UES-06', 'MR-UES-07', 'MR-UES-08', 'MR-UES-09', 'MR-UES-10', 'MR-UES-11', 'MR-UES-12']
UES_COLS_VR = ['Participant', 'VR-UES-01', 'VR-UES-02', 'VR-UES-03', 'VR-UES-04', 'VR-UES-05', 'VR-UES-06', 'VR-UES-07', 'VR-UES-08', 'VR-UES-09', 'VR-UES-10', 'VR-UES-11', 'VR-UES-12']

#iGroup Presence Questionnaire
IPQ_COLS_AR = ['Participant', 'AR-IPQ-01', 'AR-IPQ-02', 'AR-IPQ-03', 'AR-IPQ-04', 'AR-IPQ-05', 'AR-IPQ-06', 'AR-IPQ-07', 'AR-IPQ-08', 'AR-IPQ-09', 'AR-IPQ-10', 'AR-IPQ-11', 'AR-IPQ-12', 'AR-IPQ-13', 'AR-IPQ-14']
IPQ_COLS_MR = ['Participant', 'MR-IPQ-01', 'MR-IPQ-02', 'MR-IPQ-03', 'MR-IPQ-04', 'MR-IPQ-05', 'MR-IPQ-06', 'MR-IPQ-07', 'MR-IPQ-08', 'MR-IPQ-09', 'MR-IPQ-10', 'MR-IPQ-11', 'MR-IPQ-12', 'MR-IPQ-13', 'MR-IPQ-14']
IPQ_COLS_VR = ['Participant', 'VR-IPQ-01', 'VR-IPQ-02', 'VR-IPQ-03', 'VR-IPQ-04', 'VR-IPQ-05', 'VR-IPQ-06', 'VR-IPQ-07', 'VR-IPQ-08', 'VR-IPQ-09', 'VR-IPQ-10', 'VR-IPQ-11', 'VR-IPQ-12', 'VR-IPQ-13', 'VR-IPQ-14']

# iPAL Application and Intervention Scale
AIS_COLS_PH = ['Participant', 'PH-AIS-01', 'PH-AIS-02', 'PH-AIS-03', 'PH-AIS-04']
AIS_COLS_AR = ['Participant', 'AR-AIS-01', 'AR-AIS-02', 'AR-AIS-03', 'AR-AIS-04']
AIS_COLS_MR = ['Participant', 'MR-AIS-01', 'MR-AIS-02', 'MR-AIS-03', 'MR-AIS-04']
AIS_COLS_VR = ['Participant', 'VR-AIS-01', 'VR-AIS-02', 'VR-AIS-03', 'VR-AIS-04']

# Timeline Followback
TLFB_COLS = ['Participant', 'TLFB-01-01', 'TLFB-01-02', 'TLFB-02-01', 'TLFB-02-02', 'TLFB-03-01', 'TLFB-03-02', 'TLFB-04-01', 'TLFB-04-02', 'TLFB-05-01', 'TLFB-05-02']