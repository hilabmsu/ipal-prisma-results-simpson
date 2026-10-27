# iPAL PRISMA Participant Database Structure

## Running the Analysis with Python
The python scripts for running the analysis are located in the `src` directory.
Running the `main.py` file will load the data and present a menu of instruments
on which to run the analysis.

Navigate to the src folder in a terminal window, and run the following command:
> `python main.py`

List of important files:
* `main.py` the primary executable for the analysis program
* `config.py` global variables
* `utils.py` shared functions
* `figure.py` data visualization plots

Each instrument has a dedicated file which for generating instrument
specific dataframes, scoring, etc.
* `ais.py` iPAL Application Evaluation
* `dm.py` Demographics Questionnaire
* `ipq.py` iGroup Presence Questionnaire
* `ss.py` Stability Survey
* `ssq.py` Kennedy Simulator Sickness Questionnaire
* `sus.py` System Usability Scale
* `ues.py` User Engagement Scale


## Folder Structure:


```
ipal-prisma-results-simpson/
├── data/
│   └── analysis-ready/
│       └── # used for analysis and reported results
│   └── processed/
│       └── # After filtering, decomposition, and artifact marking
│   └── raw # unaltered data
│       └── SX
│           └── PhysiologicalData_XXX
│               └── 1-1-xxx_metadata.csv
│               └── AR_X
│                   └── # Empatica CSV data files
│                   └── # Empatica AVRO data files
│               └── MR_X
│                   └── # Empatica CSV data files
│                   └── # Empatica AVRO data files
│               └── PH_X
│                   └── # Empatica CSV data files
│                   └── # Empatica AVRO data files
│               └── VR_X        
│                   └── # Empatica CSV data files
│                   └── # Empatica AVRO data files
│           └── SelfReportData_X
│               └──  iPALRedCapData_xxx.pdf
├── notebooks/
├── output/
│   └── figures
│   └── latex
│   └── markdown
├── src/
├── tests/
└── README.md
```

The dataset is organized so that each subject has a folder (SX, where X = subject ID). Each subject folder contains the following subfolders:

## Physiological Data Folder (PhysiologicalData_X)

- AR_X
  - S or L
- MR_X
  - S or L
- VR_X
  - S or L
- Phone_X
  - S or L

> **Note:** S and L above are placeholders while we resolve questions related to the Empatica data files. The Empatica data that was shared has the files organized in two different ways. One is referred to as S (for short), and the other as L (for long).

### S file structure

- ACC.csv
- BVP.csv
- EDA.csv
- HR.csv
- IBI.csv
- info.txt
- tags.csv
- TEMP.csv

### L file structure

- accelerometers-std.csv
- acticounts.csv
- actigraphy-counts.csv
- activity-classification.csv
- activity-counts.csv
- activity-intensity.csv
- body-position.csv
- eda.csv
- met.csv
- prv.csv
- pulse-rate.csv
- respiratory-rate.csv
- sleep-detection.csv
- step-counts.csv
- temperature.csv
- wearing-detection.csv

The L structure indicates "aggregated_per_minute." **Open question:** What does this mean for our analysis?

## Subjective Measures Data (Subjective_X)

- iPALRedCapData_X.pdf

## Example

```
S001/
├── PhysiologicalData_001/
│   ├── AR_001/
│   │   └── S or L
│   ├── MR_001/
│   │   └── S or L
│   ├── VR_001/
│   │   └── S or L
│   └── Phone_001/
│       └── S or L
└── SubjectiveData_001/
    └── iPALRedCapData_001.pdf
```

---

# Participants

- 25 subjects participated in the study
- Mean Age: 38.52 (± 7.03)
- 16 male
- 9 female

## Data Collection

- Empatica EmbracePlus

## Collected Data Have Channels

- **ACC**
  - Data from 3-axis accelerometer sensor. The accelerometer is configured to measure acceleration in the range [-2g, 2g]. Therefore, the unit in this file is 1/64g.
  - Data from x, y, and z axis are respectively in the first, second, and third column.
- **BVP**
  - Data from photoplethysmograph.
- **EDA**
  - Data from the electrodermal activity sensor, expressed as microsiemens (μS).
- **HR**
  - Average heart rate extracted from the BVP signal. The first row is the initial time of the session expressed as a Unix timestamp in UTC. The second row is the sample rate expressed in Hz.
- **IBI**
  - Time between individual heartbeats extracted from the BVP signal.
  - No sample rate is needed for this file.
  - The first column is the time (relative to the initial time) of the detected inter-beat interval, expressed in seconds (s).
  - The second column is the duration in seconds (s) of the detected inter-beat interval (i.e., the distance in seconds from the previous beat).
- **TEMP**
  - Data from the temperature sensor, expressed in degrees Celsius (°C).

---

# Survey Order of Delivery
* Onboarding
  * Kenndey Simulator Sickness Questionnaire SSQ
* Phone
  * Demographic 
  * Stability survey (SS)
  * Timeline followback  (TLFB)
  * System Usability Study (SUS)
  * User Engagement Scale (UES)
  * iPAL Application Evaluation (IAE)
* AR/VR/MR 
  * Stability survey (SS)
  * Timeline followback  (TLFB)
  * iGroup Presence Questionnaire (IPQ)
  * System Usability Study (SUS)
  * User Engagement Scale (UES)
  * iPAL Application Evaluation (IAE)
* Exit Interviews
  * Stability survey (SS)
  * Timeline followback  (TLFB)
  * Exit Interview (EI)

# Instrument Descriptions and Item Dictionaries

## Codes for missing Data
| code | description                     |
|------|---------------------------------|
| 99   | Not applicable                  |
| 98   | Left Blank/Skipped              |
| 97   | Lost to follow up/not delivered |
| 96   | Disqualified from study         |

## Kennedy Simulation Sickness Questionnaire (SSQ)
| item_id | label                                                                                                                                          | values | value labels |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------|
| ssq-01  | Do you or have you had a history of migraine headaches?                                                                                        | 1<br>0 | yes<br>no    |
| ssq-02  | Do you or have you had a history of claustrophobia?                                                                                            | 1<br>0 | yes<br>no    |
| ssq-03  | Do you or have you had a history of frequent or severe motion sickness?                                                                        | 1<br>0 | yes<br>no    |
| ssq-04  | Do you or have you had a history of any health problems (e.g., seizures, diabetes, heart problems, vertigo) that affect your ability to drive? | 1<br>0 | yes<br>no    |
| ssq-05  | If you are a female, are you or is there a possibility that you might be pregnant?                                                             | 1<br>0 | yes<br>no    |

## Demographics Questionnaire (DM)
| item_id | label                                                                         | values                               | value labels                                                                                                                                                                                                                                             |
|---------|-------------------------------------------------------------------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dm-01   | What is your race/ethnicity?                                                  | 1<br>2<br>3<br>4<br>5<br>6<br>7      | American Indian or Alaskan Native<br>Asian / Pacific Islander<br>Black or African American<br>Hispanic<br>White / Caucasian<br>Multiple ethnicity<br> Hispanic and White / Caucasian                                                                     |
| dm-02   | What is your gender?                                                          | 1<br>2<br>3<br>4                     | Male<br>Female<br>Non-binary / third gender<br>Prefer not to say                                                                                                                                                                                         |
| dm-03   | How old are you?                                                              | range 18-75                          |                                                                                                                                                                                                                                                          |
| dm-04   | What is the highest level of education you have completed?                    | 1<br>2<br>3<br>4<br>5                | 12th grade of less<br>High school graduate or GED<br>Some college/ Associates/ Technical school training<br>College graduate<br>Graduate school degree (Master's or Doctorate)                                                                           |
| dm-05   | Which option best describes your current home?                                | 1<br>2<br>3<br>4<br>5<br>6           | It is owned or being bought by you or someone in household.<br>It is rented for money by you or someone in household.<br>It is occupied without payment, money, or rent.<br>I live with friends<br>I live with family.<br>I have no permanent residence. |
| dm-06   | How do you pay for healthcare?                                                | 1<br>2<br>3                          | Government funding (Medicaid, Medicare, Ryan White, VA)<br>Private insurance<br>Self-pay, out of pocket                                                                                                                                                  |
| dm-07   | Do you work for pay outside of the home?                                      | 1<br>0                               | Yes<br>No                                                                                                                                                                                                                                                |
| dm-08   | Which best corresponds to your current work situation?                        | 1<br>2<br>3<br>4<br>5                | Working Full time<br>Working part time<br>Not working or looking for work.<br>Disabled or retired and not looking for work.<br>Currently in School                                                                                                       |
| dm-09   | What is your combined family income for the past 12 months (from all sources) | 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8 | Less than $5,000<br>$5,000-$19,999<br>$20,000-$49,999<br>$50,000-$99,999<br>$100,000-$149,999<br>More than $150,000<br>Do not know<br>Choose not to answer                                                                                               |
| dm-10   | Have you used any of the following substances?                                | 1<br>2<br>3<br>4<br>5<br>6<br>7      | Amphetamine<br>Methamphetamine<br>Benzodiazepine<br>Cocaine<br>THC/Cannabis<br>Opiate<br>Oxycodone                                                                                                                                                       |

*Notes:*
* Item DM-05, DM-06 and DM-08 are the SS questions for the initial Phone intervention session.
* Item DM-07 was blank
* Item DM-10 was not planned, but not asked in the demographics. I think I was split out when the Timeline Follow Back was added.


## System Usability Scale (SUS)
| item_id | label                                                                                      | values                | value labels                                                                              |
|---------|--------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------------------------------------------------------|
| sus-01  | I think that I would like to use this system frequently                                    | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| sus-02  | I found the system unnecessarily complex                                                   | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| sus-03  | I thought the system was easy to use.                                                      | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| sus-04  | I think that I would need the support of a technical person to be able to use this system. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| sus-05  | I found the various functions in this system were well integrated.                         | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| sus-06  | I thought there was too much inconsistency in this system.                                 | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| sus-07  | I would imagine that most people would learn to use this system very quickly.              | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| sus-08  | I found the system very cumbersome to use.                                                 | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| sus-09  | I felt very confident using the system.                                                    | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| sus-10  | I needed to learn a lot of things before I could get going with this system.               | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |

## User Engagement Scale (UES)
| item_id | label                                           | values                | value labels                                                                              |
|---------|-------------------------------------------------|-----------------------|-------------------------------------------------------------------------------------------|
| ues-01  | I lost myself in this app experience.           | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-02  | The time I spent in this app just slipped away. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-03  | I was absorbed in the app task.                 | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-04  | I felt frustrated while using the app.          | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-05  | I found this app to be confusing.               | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-06  | Using this app was taxing.                      | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-07  | The app is attractive.                          | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-08  | The app is aesthetically appealing.             | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-09  | The app appealed to my senses.                  | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-10  | Using this app was worthwhile.                  | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-11  | The therapy experience was rewarding.           | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ues-12  | I felt interested in the therapy tasks.         | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |

# iGroup Presence Questionnaire (IPQ)
| item_id | label                                                                                                    | values                | value labels                                                                                                 |
|---------|----------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------------------------------------------------------------------------------|
| ipq-01  | In the computer-generated world, I had a sense of being there.                                           | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| ipq-02  | I felt that the virtual world surround me.                                                               | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| ipq-03  | I felt like I was perceiving pictures.                                                                   | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| ipq-04  | I did not feel present in the virtual space.                                                             | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| ipq-05  | I had a sense of acting in the virtual space, rather than operating something form the outside.          | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| ipq-06  | I felt present in the virtual space                                                                      | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| ipq-07  | How aware were you of the real world surrounding you while navigating in the virtual world?              | 1<br>2<br>3<br>4<br>5 | Very Aware<br>Somewhat Aware<br>Neither Aware nor Unaware<br>Somewhat Unaware<br>Completely Unaware          |
| ipq-08  | I was not aware of my real environment.                                                                  | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| ipq-09  | I still paid attention to my real environment.                                                           | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| ipq-10  | I was completely captivated by the virtual world.                                                        | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| ipq-11  | How real did the virtual world seem to you?                                                              | 1<br>2<br>3<br>4<br>5 | Very Unreal<br>Somewhat Unreal<br>Neither Real nor Unreal<br>Somewhat Real<br>Very Real                      |
| ipq-12  | How much did your experience in the virtual environment seem consistent with your real-world experience? | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| ipq-13  | How real did the virtual world seem to you?                                                              | 1<br>2<br>3<br>4<br>5 | Very Unreal<br>Somewhat Unreal<br>Neither Real nor Unreal<br>Somewhat Real<br>Very Real                      |
| ipq-14  | The virtual world seemed more realistic than the real world.                                             | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |

## iPAL Application Evaluation (AIE)
| item_id | label                                                                               | values                              | value labels                                                                              |
|---------|-------------------------------------------------------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------|
| ais-01  | The videos and breathing exercises were a good fit for the strength of my cravings. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ais-02  | The videos and breathing exercises matched my internal or external triggers.        | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ais-03  | The videos were clear and easy to understand.                                       | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| ais-04  | The breathing exercises were smooth and easy to do.                                 | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |

## Timeline Follow Back (TLFB)
| item_id | label                                                                          | values     | value labels |
|---------|--------------------------------------------------------------------------------|------------|--------------|
| tlfb-01 | Visit 1 date                                                                   | YYYY-MM-DD |              |
| tlfb-02 | Have you used opioids or any other substances during the assessment period?    | 1<br>0     | yes<br>no    |
| tlfb-03 | e-Cigarettes or nicotine vape:                                                 | 1<br>0     | yes<br>no    |
| tlfb-04 | Other tobacco:                                                                 | 1<br>0     | yes<br>no    |
| tlfb-05 | Alcohol:                                                                       | 1<br>0     | yes<br>no    |
| tlfb-06 | Marijuana:                                                                     | 1<br>0     | yes<br>no    |
| tlfb-07 | Cocaine/crack:                                                                 | 1<br>0     | yes<br>no    |
| tlfb-08 | Methamphetamine:                                                               | 1<br>0     | yes<br>no    |
| tlfb-09 | Amphetamine-type stimulants (including non-prescribed prescription stimulants) | 1<br>0     | yes<br>no    |
| tlfb-10 | Methadone:                                                                     | 1<br>0     | yes<br>no    |
| tlfb-11 | Heroin:                                                                        | 1<br>0     | yes<br>no    |
| tlfb-12 | Buprenorphine:                                                                 | 1<br>0     | yes<br>no    |
| tlfb-13 | Fentanyl:                                                                      | 1<br>0     | yes<br>no    |
| tlfb-14 | Other opioids:                                                                 | 1<br>0     | yes<br>no    |
| tlfb-15 | Xylazine:                                                                      | 1<br>0     | yes<br>no    |
| tlfb-16 | Hallucinogens:                                                                 | 1<br>0     | yes<br>no    |
| tlfb-17 | Ketamine:                                                                      | 1<br>0     | yes<br>no    |
| tlfb-18 | Benzodiazepines:                                                               | 1<br>0     | yes<br>no    |

## Exit Interview (EI)
| item_id | label                                                                                                                                                                                               | values               | value labels                                         |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| ei-01   | You experienced Cognitive Behavioral Therapy and Heart Rate Variance interventions in virtual, augmented, and mixed realities. How would you describe your experiences with each of those headsets? | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| ei-02   | Do you think these types of technologies have a place in OUD treatment and management? If YES, how? If NO, why not?                                                                                 | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| ei-03   | How would you describe the iPAL application, in terms of a cravings management tool?                                                                                                                | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| ei-04   | How would you describe the interventions (CBT, HRV)? Were the interventions appropriate for the intensity level and triggers you reported?                                                          | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| ei-05   | Do you think the iPAL app, or similar digital interventions delivered via phone should be integrated into OUD treatment plans? If YES, how and in what capacity or role? if NO, why not?            | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| ei-06   | If iPAL or a similar app was available, would you download the app and incorporate it into your OUD treatment and management plan?                                                                  | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |


## Data Table for Repeat Measures Instruments (SS, SUS, UES, IPQ, AIS, TLFB)
| Label          | Values                                 |
|----------------|----------------------------------------|
| participant_id | range 1 - 25                           |
| instrument     | ss<br>sus<br>ues<br>ipq<br>ais<br>tlfb |
| condition      | ph<br>ar<br>mr<br>vr                   |
| visit          | range 1-5                              |
| item           | Instrument item_id                     |
| value          | Instrument item value                  |

## Data Table for Initial Interview
* One row per participant labelled with the participant_id
* One column per question on the SSQ, and DM instruments
* column values text


## Data Table for Exit Interview
* One row per participant labelled with the participant_id
* One column per question on the exit interview
* column values text



# Anomalies
* Empatica has raw data for participant 010 on 6/10, but there is no intervention scheduled that day.
* Missing Empatica data files earlier than 2025-02-27
  * 001_PH_20241119
  * 002_PH_20241211
  * 004_PH_20241217
  * 001_VR_20241217
  * 002_VR_20250102
  * 005_PH_20250109
  * 004_VR_20250114
  * 006_PH_20250123
  * 007_PH_20250127
  * 004_AR_20250130
  * 007_MR_20250131
  * 008_PH_20250205
  * 009_PH_20250210
  * 006_MR_20250213
 |
