from pathlib import Path

# iPAL Study Constants
EXCLUDED_PARTICIPANT_IDS = [3]

# Project root
ROOT = Path(__file__).parent.parent

# Data paths
DATA_PATH = ROOT / 'data' / 'analysis-ready'

# Output paths
FIGURES_PATH  = ROOT / 'outputs' / 'figures'
MARKDOWN_PATH = ROOT / 'outputs' / 'markdown'
LATEX_PATH    = ROOT / 'outputs' / 'latex'

SESSION_NAMES = {
    "oi": "Onboarding Interview",
    "ph": "Phone App",
    "ar": "Augmented Reality",
    "mr": "Mixed Reality",
    "vr": "Virtual Reality",
    "ei": "Exit Interview",
}

SEQUENCE_ASSIGNMENT = {
    1: ['ph','vr','mr','ar'],
    2: ['ph','vr','ar','mr'],
    3: ['ph','mr','vr','ar'],
    4: ['ph','mr','ar','vr'],
    5: ['ph','ar','vr','mr'],
    6: ['ph','ar','mr','vr']
}

MISSING_VALUES_CATEGORIES = {
    99: "NOT_APPLICABLE",
    98: "LEFT_BLANK",
    97: "LOST TO FOLLOWUP",
    96: "DISQUALIFIED FROM STUDY"
}