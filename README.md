# iPAL PRISMA Participant Database Structure

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
  - Data from 3-axis accelerometer sensor. The accelerometer is configured to measure acceleration in the range [-2g, 2g]. Therefore the unit in this file is 1/64g.
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

# iPAL PRISMA Data Dictionary

| ID | Name | Label | Values | Value Labels |
|----|------|-------|--------|---------------|
| 001 | Participant | Participant Number | range 001-026 | |
| 002 | SSQ-01 | Do you or have you had a history of migraine headaches? | 1<br>0 | yes<br>no |
| 003 | SSQ-02 | Do you or have you had a history of claustrophobia? | 1<br>0 | yes<br>no |
| 004 | SSQ-03 | Do you or have you had a history of frequent or severe motion sickness? | 1<br>0 | yes<br>no |
| 005 | SSQ-04 | Do you or have you had a history of any health problems (e.g., seizures, diabetes, heart problems, vertigo) that affect your ability to drive? | 1<br>0 | yes<br>no |
| 006 | SSQ-05 | If you are a female, are you or is there a possibility that you might be pregnant? | 1<br>0<br>-99 | yes<br>no<br>Not Applicable |
| 007 | DM-01 | What is your race/ethnicity? | 1<br>2<br>3<br>4<br>5<br>6 | American Indian or Alaskan Native<br>Asian / Pacific Islander<br>Black or African American<br>Hispanic<br>White / Caucasian<br>Multiple ethnicity |
| 008 | DM-02 | What is your gender? | 1<br>2<br>3<br>4 | Male<br>Female<br>Non-binary / third gender<br>Prefer not to say |
| 009 | DM-03 | How old are you? | range 18-75 | |
| 010 | DM-04 | What is the highest level of education you have completed? | 1<br>2<br>3<br>4<br>5 | 12th grade of less<br>High school graduate or GED<br>Some college/ Associates/ Technical school training<br>College graduate<br>Graduate school degree (Master's or Doctorate) |
| 011 | DM-05 | Which option best describes your current home? | 1<br>2<br>3<br>4<br>5<br>6 | It is owned or being bought by you or someone in household.<br>It is rented for money by you or someone in household.<br>It is occupied without payment, money, or rent.<br>I live with friends<br>I live with family.<br>I have no permanent residence. |
| 012 | DM-06 | How do you pay for healthcare? | 1<br>2<br>3 | Government funding (Medicaid, Medicare, Ryan White, VA)<br>Private insurance<br>Self-pay, out of pocket |
| 013 | DM-07 | Do you work for pay outside of the home? | 1<br>0 | Yes<br>No |
| 014 | DM-08 | Which best corresponds to your current work situation? | 1<br>2<br>3<br>4<br>5 | Working Full time<br>Working part time<br>Not working or looking for work.<br>Disabled or retired and not looking for work.<br>Currently in School |
| 015 | DM-09 | What is your combined family income for the past 12 months (from all sources) | 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8 | Less than $5,000<br>$5,000-$19,999<br>$20,000-$49,999<br>$50,000-$99,999<br>$100,000-$149,999<br>More than $150,000<br>Do not know<br>Choose not to answer |
| 016 | DM-10 | Have you used any of the following substances? | 1<br>2<br>3<br>4<br>5<br>6<br>7 | Amphetamine<br>Methamphetamine<br>Benzodiazepine<br>Cocaine<br>THC/Cannabis<br>Opiate<br>Oxycodone |
| 017 | PH-SUS-01 | I think that I would like to use this system frequently | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 018 | PH-SUS-02 | I found the system unnecessarily complex | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 019 | PH-SUS-03 | I thought the system was easy to use. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 020 | PH-SUS-04 | I think that I would need the support of a technical person to be able to use this system. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 021 | PH-SUS-05 | I found the various functions in this system were well integrated. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 022 | PH-SUS-06 | I thought there was too much inconsistency in this system. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 023 | PH-SUS-07 | I would imagine that most people would learn to use this system very quickly. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 024 | PH-SUS-08 | I found the system very cumbersome to use. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 025 | PH-SUS-09 | I felt very confident using the system. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 026 | PH-SUS-10 | I needed to learn a lot of things before I could get going with this system. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 027 | PH-UES-01 | I lost myself in this app experience. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 028 | PH-UES-02 | The time I spent in this app just slipped away. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 029 | PH-UES-03 | I was absorbed in the app task. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 030 | PH-UES-04 | I felt frustrated while using the app. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 031 | PH-UES-05 | I found this app to be confusing. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 032 | PH-UES-06 | Using this app was taxing. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 033 | PH-UES-07 | The app is attractive. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 034 | PH-UES-08 | The app is aesthetically appealing. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 035 | PH-UES-09 | The app appealed to my senses. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 036 | PH-UES-10 | Using this app was worthwhile. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 037 | PH-UES-11 | The therapy experience was rewarding. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 038 | PH-UES-12 | I felt interested in the therapy tasks. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 039 | PH-AIS-01 | The videos and breathing exercises were a good fit for the strength of my cravings. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 040 | PH-AIS-02 | The videos and breathing exercises matched my internal or external triggers. | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree |
| 041 | PH-AIS-03 | The videos were videos easy to understand. | 1<br>2<br>3<br>4<br>5<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Left Blank/Skipped |
| 042 | PH-AIS-04 | The breathing exercises were smooth and easy to do. | 1<br>2<br>3<br>4<br>5<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Left Blank/Skipped |
| 043 | AR-SS-01 | Which option best describes your current home? | 1<br>2<br>3<br>4<br>5<br>6<br>-97 | It is owned or being bought by you or someone in household.<br>It is rented for money by you or someone in household.<br>It is occupied without payment, money, or rent.<br>I live with friends<br>I live with family.<br>I have no permanent residence.<br>Intervention Not Delivered |
| 044 | AR-SS-02 | How do you pay for healthcare? | 1<br>2<br>3<br>-97 | Government funding (Medicaid, Medicare, Ryan White, VA)<br>Private insurance<br>Self-pay, out of pocket<br>Intervention Not Delivered |
| 045 | AR-SS-03 | Which best corresponds to your current work situation? | 1<br>2<br>3<br>4<br>5<br>-97 | Working Full time<br>Working part time<br>Not working or looking for work.<br>Disabled or retired and not looking for work.<br>Currently in School<br>Intervention Not Delivered |
| 046 | AR-IPQ-01 | In the computer-generated world, I had a sense of being there. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 047 | AR-IPQ-02 | I felt that the virtual world surround me. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 048 | AR-IPQ-03 | I felt like I was perceiving pictures. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 049 | AR-IPQ-04 | I did not feel present in the virtual space. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 050 | AR-IPQ-05 | I had a sense of acting in the virtual space, rather than operating something form the outside. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 051 | AR-IPQ-06 | I felt present in the virtual space | 1<br>2<br>3<br>4<br>5 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree |
| 052 | AR-IPQ-07 | How aware were you of the real world surrounding you while navigating in the virtual world? | 1<br>2<br>3<br>4<br>5<br>-97 | Very Aware<br>Somewhat Aware<br>Neither Aware nor Unaware<br>Somewhat Unaware<br>Completely Unaware<br>Intervention Not Delivered |
| 053 | AR-IPQ-08 | I was not aware of my real environment. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 054 | AR-IPQ-09 | I still paid attention to my real environment. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 055 | AR-IPQ-10 | I was completely captivated by the virtual world. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 056 | AR-IPQ-11 | How real did the virtual world seem to you? | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Very Unreal<br>Somewhat unreal<br>Neither real nor unreal<br>Somewhat real<br>Very Real<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 057 | AR-IPQ-12 | How much did your experience in the virtual environment seem consistent with your real-world experience? | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 058 | AR-IPQ-13 | How real did the virtual world seem to you? | 1<br>2<br>3<br>4<br>5<br>-97 | Very Unreal<br>Somewhat Unreal<br>Neither real nor unreal<br>Somewhat real<br>Very real<br>Intervention Not Delivered |
| 059 | AR-IPQ-14 | The virtual world seemed more realistic than the real world. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 060 | AR-SUS-01 | I think that I would like to use this system frequently | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 061 | AR-SUS-02 | I found the system unnecessarily complex | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 062 | AR-SUS-03 | I thought the system was easy to use. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 063 | AR-SUS-04 | I think that I would need the support of a technical person to be able to use this system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 064 | AR-SUS-05 | I found the various functions in this system were well integrated. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 065 | AR-SUS-06 | I thought there was too much inconsistency in this system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 066 | AR-SUS-07 | I would imagine that most people would learn to use this system very quickly. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 067 | AR-SUS-08 | I found the system very cumbersome to use. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 068 | AR-SUS-09 | I felt very confident using the system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 069 | AR-SUS-10 | I needed to learn a lot of things before I could get going with this system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 070 | AR-UES-01 | I lost myself in this app experience. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 071 | AR-UES-02 | The time I spent in this app just slipped away. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 072 | AR-UES-03 | I was absorbed in the app task. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 073 | AR-UES-04 | I felt frustrated while using the app. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 074 | AR-UES-05 | I found this app to be confusing. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 075 | AR-UES-06 | Using this app was taxing. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 076 | AR-UES-07 | The app is attractive. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 077 | AR-UES-08 | The app is aesthetically appealing. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 078 | AR-UES-09 | The app appealed to my senses. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 079 | AR-UES-10 | Using this app was worthwhile. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 080 | AR-UES-11 | The therapy experience was rewarding. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 081 | AR-UES-12 | I felt interested in the therapy tasks. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 082 | AR-AIS-01 | The videos and breathing exercises were a good fit for the strength of my cravings. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 083 | AR-AIS-02 | The videos and breathing exercises matched my internal or external triggers. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 084 | AR-AIS-03 | The videos were clear and easy to understand. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 085 | AR-AIS-04 | The breathing exercises were smooth and easy to do. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 086 | MR-SS-01 | Which option best describes your current home? | 1<br>2<br>3<br>4<br>5<br>6<br>-97 | It is owned or being bought by you or someone in household.<br>It is rented for money by you or someone in household.<br>It is occupied without payment, money, or rent.<br>I live with friends<br>I live with family.<br>I have no permanent residence.<br>Intervention Not Delivered |
| 087 | MR-SS-02 | How do you pay for healthcare? | 1<br>2<br>3<br>-97 | Government funding (Medicaid, Medicare, Ryan White, VA)<br>Private insurance<br>Self-pay, out of pocket<br>Intervention Not Delivered |
| 088 | MR-SS-03 | Which best corresponds to your current work situation? | 1<br>2<br>3<br>4<br>5<br>-97 | Working Full time<br>Working part time<br>Not working or looking for work.<br>Disabled or retired and not looking for work.<br>Currently in School<br>Intervention Not Delivered |
| 089 | MR-IPQ-01 | In the computer-generated world, I had a sense of being there. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 090 | MR-IPQ-02 | I felt that the virtual world surround me. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 091 | MR-IPQ-03 | I felt like I was perceiving pictures. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 092 | MR-IPQ-04 | I did not feel present in the virtual space. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 093 | MR-IPQ-05 | I had a sense of acting in the virtual space, rather than operating something form the outside. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 094 | MR-IPQ-06 | I felt present in the virtual space | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 095 | MR-IPQ-07 | How aware were you of the real world surrounding you while navigating in the virtual world? | 1<br>2<br>3<br>4<br>5<br>-97 | Very Aware<br>Somewhat Aware<br>Neither Aware nor Unaware<br>Somewhat Unaware<br>Completely Unaware<br>Intervention Not Delivered |
| 096 | MR-IPQ-08 | I was not aware of my real environment. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 097 | MR-IPQ-09 | I still paid attention to my real environment. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 098 | MR-IPQ-10 | I was completely captivated by the virtual world. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 099 | MR-IPQ-11 | How real did the virtual world seem to you? | 1<br>2<br>3<br>4<br>5<br>-97 | Very Unreal<br>Somewhat Unreal<br>Neither Real nor Unreal<br>Somewhat Real<br>Very Real<br>Intervention Not Delivered |
| 100 | MR-IPQ-12 | How much did your experience in the virtual environment seem consistent with your real-world experience? | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 101 | MR-IPQ-13 | How real did the virtual world seem to you? | 1<br>2<br>3<br>4<br>5<br>-97 | Very Unreal<br>Somewhat Unreal<br>Neither Real nor Unreal<br>Somewhat Real<br>Very Real<br>Intervention Not Delivered |
| 102 | MR-IPQ-14 | The virtual world seemed more realistic than the real world. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 103 | MR-SUS-01 | I think that I would like to use this system frequently | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 104 | MR-SUS-02 | I found the system unnecessarily complex | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 105 | MR-SUS-03 | I thought the system was easy to use. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 106 | MR-SUS-04 | I think that I would need the support of a technical person to be able to use this system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 107 | MR-SUS-05 | I found the various functions in this system were well integrated. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 108 | MR-SUS-06 | I thought there was too much inconsistency in this system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 109 | MR-SUS-07 | I would imagine that most people would learn to use this system very quickly. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 110 | MR-SUS-08 | I found the system very cumbersome to use. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 111 | MR-SUS-09 | I felt very confident using the system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 112 | MR-SUS-10 | I needed to learn a lot of things before I could get going with this system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 113 | MR-UES-01 | I lost myself in this app experience. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 114 | MR-UES-02 | The time I spent in this app just slipped away. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 115 | MR-UES-03 | I was absorbed in the app task. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 116 | MR-UES-04 | I felt frustrated while using the app. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 117 | MR-UES-05 | I found this app to be confusing. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 118 | MR-UES-06 | Using this app was taxing. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 119 | MR-UES-07 | The app is attractive. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 120 | MR-UES-08 | The app is aesthetically appealing. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 121 | MR-UES-09 | The app appealed to my senses. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 122 | MR-UES-10 | Using this app was worthwhile. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 123 | MR-UES-11 | The therapy experience was rewarding. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 124 | MR-UES-12 | I felt interested in the therapy tasks. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 125 | MR-AIS-01 | The videos and breathing exercises were a good fit for the strength of my cravings. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 126 | MR-AIS-02 | The videos and breathing exercises matched my internal or external triggers. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 127 | MR-AIS-03 | The videos were clear and easy to understand. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 128 | MR-AIS-04 | The breathing exercises were smooth and easy to do. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 129 | VR-SS-01 | Which option best describes your current home? | 1<br>2<br>3<br>4<br>5<br>6<br>-97 | It is owned or being bought by you or someone in household.<br>It is rented for money by you or someone in household.<br>It is occupied without payment, money, or rent.<br>I live with friends<br>I live with family.<br>I have no permanent residence.<br>Intervention Not Delivered |
| 130 | VR-SS-02 | How do you pay for healthcare? | 1<br>2<br>3<br>-97 | Government funding (Medicaid, Medicare, Ryan White, VA)<br>Private insurance<br>Self-pay, out of pocket<br>Intervention Not Delivered |
| 131 | VR-SS-03 | Which best corresponds to your current work situation? | 1<br>2<br>3<br>4<br>5<br>-97 | Working Full time<br>Working part time<br>Not working or looking for work.<br>Disabled or retired and not looking for work.<br>Currently in School<br>Intervention Not Delivered |
| 132 | VR-IPQ-01 | In the computer-generated world, I had a sense of being there. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 133 | VR-IPQ-02 | I felt that the virtual world surround me. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 134 | VR-IPQ-03 | I felt like I was perceiving pictures. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 135 | VR-IPQ-04 | I did not feel present in the virtual space. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 136 | VR-IPQ-05 | I had a sense of acting in the virtual space, rather than operating something form the outside. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 137 | VR-IPQ-06 | I felt present in the virtual space | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 138 | VR-IPQ-07 | How aware were you of the real world surrounding you while navigating in the virtual world? | 1<br>2<br>3<br>4<br>5<br>-97 | Very Aware<br>Somewhat Aware<br>Neither Aware nor Unaware<br>Somewhat Unaware<br>Completely Unaware<br>Intervention Not Delivered |
| 139 | VR-IPQ-08 | I was not aware of my real environment. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 140 | VR-IPQ-09 | I still paid attention to my real environment. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 141 | VR-IPQ-10 | I was completely captivated by the virtual world. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 142 | VR-IPQ-11 | How real did the virtual world seem to you? | 1<br>2<br>3<br>4<br>5<br>-97 | Very Unreal<br>Somewhat Unreal<br>Neither Real nor Unreal<br>Somewhat Real<br>Very Real<br>Intervention Not Delivered |
| 143 | VR-IPQ-12 | How much did your experience in the virtual environment seem consistent with your real-world experience? | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 144 | VR-IPQ-13 | How real did the virtual world seem to you? | 1<br>2<br>3<br>4<br>5<br>-97 | Very Unreal<br>Somewhat Unreal<br>Neither Real nor Unreal<br>Somewhat Real<br>Very Real<br>Intervention Not Delivered |
| 145 | VR-IPQ-14 | The virtual world seemed more realistic than the real world. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neither Agree nor Disagree<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 146 | VR-SUS-01 | I think that I would like to use this system frequently | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 147 | VR-SUS-02 | I found the system unnecessarily complex | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 148 | VR-SUS-03 | I thought the system was easy to use. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 149 | VR-SUS-04 | I think that I would need the support of a technical person to be able to use this system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 150 | VR-SUS-05 | I found the various functions in this system were well integrated. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 151 | VR-SUS-06 | I thought there was too much inconsistency in this system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 152 | VR-SUS-07 | I would imagine that most people would learn to use this system very quickly. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 153 | VR-SUS-08 | I found the system very cumbersome to use. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 154 | VR-SUS-09 | I felt very confident using the system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 155 | VR-SUS-10 | I needed to learn a lot of things before I could get going with this system. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 156 | VR-UES-01 | I lost myself in this app experience. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 157 | VR-UES-02 | The time I spent in this app just slipped away. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 158 | VR-UES-03 | I was absorbed in the app task. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 159 | VR-UES-04 | I felt frustrated while using the app. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 160 | VR-UES-05 | I found this app to be confusing. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 161 | VR-UES-06 | Using this app was taxing. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 162 | VR-UES-07 | The app is attractive. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 163 | VR-UES-08 | The app is aesthetically appealing. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 164 | VR-UES-09 | The app appealed to my senses. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 165 | VR-UES-10 | Using this app was worthwhile. | 1<br>2<br>3<br>4<br>5<br>-97 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered |
| 166 | VR-UES-11 | The therapy experience was rewarding. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 167 | VR-UES-12 | I felt interested in the therapy tasks. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 168 | VR-AIS-01 | The videos and breathing exercises were a good fit for the strength of my cravings. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 169 | VR-AIS-02 | The videos and breathing exercises matched my internal or external triggers. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 170 | VR-AIS-03 | The videos were clear and easy to understand. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 171 | VR-AIS-04 | The breathing exercises were smooth and easy to do. | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Completely Disagree<br>Somewhat Disagree<br>Neutral<br>Somewhat Agree<br>Completely Agree<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 172 | EI-SS-01 | Which option best describes your current home? | 1<br>2<br>3<br>4<br>5<br>6<br>-97<br>-98 | It is owned or being bought by you or someone in household.<br>It is rented for money by you or someone in household.<br>It is occupied without payment, money, or rent.<br>I live with friends<br>I live with family.<br>I have no permanent residence.<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 173 | EI-SS-02 | How do you pay for healthcare? | 1<br>2<br>3<br>-97<br>-98 | Government funding (Medicaid, Medicare, Ryan White, VA)<br>Private insurance<br>Self-pay, out of pocket<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 174 | EI-SS-03 | Which best corresponds to your current work situation? | 1<br>2<br>3<br>4<br>5<br>-97<br>-98 | Working Full time<br>Working part time<br>Not working or looking for work.<br>Disabled or retired and not looking for work.<br>Currently in School<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 175 | EI-01 | You experienced Cognitive Behavioral Therapy and Heart Rate Variance interventions in virtual, augmented, and mixed realities. How would you describe your experiences with each of those headsets? | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| 176 | EI-02 | Do you think these types of technologies have a place in OUD treatment and management? If YES, how? If NO, why not? | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| 177 | EI-03 | How would you describe the iPAL application, in terms of a cravings management tool? | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| 178 | EI-04 | How would you describe the interventions (CBT, HRV)? Were the interventions appropriate for the intensity level and triggers you reported? | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| 179 | EI-05 | Do you think the iPAL app, or similar digital interventions delivered via phone should be integrated into OUD treatment plans? If YES, how and in what capacity or role? if NO, why not? | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| 180 | EI-06 | If iPAL or a similar app was available, would you download the app and incorporate it into your OUD treatment and management plan? | string<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| 181 | TLFB-01-01 | Visit 1 date | YYYY-MM-DD | |
| 182 | TLFB-01-02 | Have you used opioids or any other substances during the assessment period? | 1<br>0 | yes<br>no |
| 183 | TLFB-01-03 | e-Cigarettes or nicotine vape: | 1<br>0 | yes<br>no |
| 184 | TLFB-01-04 | Other tobacco: | 1<br>0 | yes<br>no |
| 185 | TLFB-01-05 | Alcohol: | 1<br>0 | yes<br>no |
| 186 | TLFB-01-06 | Marijuana: | 1<br>0 | yes<br>no |
| 187 | TLFB-01-07 | Cocaine/crack: | 1<br>0 | yes<br>no |
| 188 | TLFB-01-08 | Methamphetamine: | 1<br>0 | yes<br>no |
| 189 | TLFB-01-09 | Amphetamine-type stimulants (including non-prescribed prescription stimulants) | 1<br>0 | yes<br>no |
| 190 | TLFB-01-10 | Methadone: | 1<br>0 | yes<br>no |
| 191 | TLFB-01-11 | Heroin: | 1<br>0 | yes<br>no |
| 192 | TLFB-01-12 | Buprenorphine: | 1<br>0 | yes<br>no |
| 193 | TLFB-01-13 | Fentanyl: | 1<br>0 | yes<br>no |
| 194 | TLFB-01-14 | Other opioids: | 1<br>0 | yes<br>no |
| 195 | TLFB-01-15 | Xylazine: | 1<br>0 | yes<br>no |
| 196 | TLFB-01-16 | Hallucinogens: | 1<br>0 | yes<br>no |
| 197 | TLFB-01-17 | Ketamine: | 1<br>0 | yes<br>no |
| 198 | TLFB-01-18 | Benzodiazepines: | 1<br>0 | yes<br>no |
| 199 | TLFB-02-01 | Visit 2 date | YYYY-MM-DD<br>-98 | <br>Left Blank/Skipped |
| 200 | TLFB-02-02 | Have you used opioids or any other substances during the assessment period? | 1<br>0<br>-98 | yes<br>no<br>Left Blank/Skipped |
| 201 | TLFB-02-03 | e-Cigarettes or nicotine vape: | 1<br>0 | yes<br>no |
| 202 | TLFB-02-04 | Other tobacco: | 1<br>0 | yes<br>no |
| 203 | TLFB-02-05 | Alcohol: | 1<br>0 | yes<br>no |
| 204 | TLFB-02-06 | Marijuana: | 1<br>0 | yes<br>no |
| 205 | TLFB-02-07 | Cocaine/crack: | 1<br>0 | yes<br>no |
| 206 | TLFB-02-08 | Methamphetamine: | 1<br>0 | yes<br>no |
| 207 | TLFB-02-09 | Amphetamine-type stimulants (including non-prescribed prescription stimulants) | 1<br>0 | yes<br>no |
| 208 | TLFB-02-10 | Methadone: | 1<br>0 | yes<br>no |
| 209 | TLFB-02-11 | Heroin: | 1<br>0 | yes<br>no |
| 210 | TLFB-02-12 | Buprenorphine: | 1<br>0 | yes<br>no |
| 211 | TLFB-02-13 | Fentanyl: | 1<br>0 | yes<br>no |
| 212 | TLFB-02-14 | Other opioids: | 1<br>0 | yes<br>no |
| 213 | TLFB-02-15 | Xylazine: | 1<br>0 | yes<br>no |
| 214 | TLFB-02-16 | Hallucinogens: | 1<br>0 | yes<br>no |
| 215 | TLFB-02-17 | Ketamine: | 1<br>0 | yes<br>no |
| 216 | TLFB-02-18 | Benzodiazepines: | 1<br>0 | yes<br>no |
| 217 | TLFB-03-01 | Visit 3 date | YYYY-MM-DD<br>-98 | <br>Left Blank/Skipped |
| 218 | TLFB-03-02 | Have you used opioids or any other substances during the assessment period? | 1<br>0<br>-98 | yes<br>no<br>Left Blank/Skipped |
| 219 | TLFB-03-03 | e-Cigarettes or nicotine vape: | 1<br>0 | yes<br>no |
| 220 | TLFB-03-04 | Other tobacco: | 1<br>0 | yes<br>no |
| 221 | TLFB-03-05 | Alcohol: | 1<br>0 | yes<br>no |
| 222 | TLFB-03-06 | Marijuana: | 1<br>0 | yes<br>no |
| 223 | TLFB-03-07 | Cocaine/crack: | 1<br>0 | yes<br>no |
| 224 | TLFB-03-08 | Methamphetamine: | 1<br>0 | yes<br>no |
| 225 | TLFB-03-09 | Amphetamine-type stimulants (including non-prescribed prescription stimulants) | 1<br>0 | yes<br>no |
| 226 | TLFB-03-10 | Methadone: | 1<br>0 | yes<br>no |
| 227 | TLFB-03-11 | Heroin: | 1<br>0 | yes<br>no |
| 228 | TLFB-03-12 | Buprenorphine: | 1<br>0 | yes<br>no |
| 229 | TLFB-03-13 | Fentanyl: | 1<br>0 | yes<br>no |
| 230 | TLFB-03-14 | Other opioids: | 1<br>0 | yes<br>no |
| 231 | TLFB-03-15 | Xylazine: | 1<br>0 | yes<br>no |
| 232 | TLFB-03-16 | Hallucinogens: | 1<br>0 | yes<br>no |
| 233 | TLFB-03-17 | Ketamine: | 1<br>0 | yes<br>no |
| 234 | TLFB-03-18 | Benzodiazepines: | 1<br>0 | yes<br>no |
| 235 | TLFB-04-01 | Visit 4 date | YYYY-MM-DD<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| 236 | TLFB-04-02 | Have you used opioids or any other substances during the assessment period? | 1<br>0<br>-97<br>-98 | yes<br>no<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 237 | TLFB-04-03 | e-Cigarettes or nicotine vape: | 1<br>0 | yes<br>no |
| 238 | TLFB-04-04 | Other tobacco: | 1<br>0 | yes<br>no |
| 239 | TLFB-04-05 | Alcohol: | 1<br>0 | yes<br>no |
| 240 | TLFB-04-06 | Marijuana: | 1<br>0 | yes<br>no |
| 241 | TLFB-04-07 | Cocaine/crack: | 1<br>0 | yes<br>no |
| 242 | TLFB-04-08 | Methamphetamine: | 1<br>0 | yes<br>no |
| 243 | TLFB-04-09 | Amphetamine-type stimulants (including non-prescribed prescription stimulants) | 1<br>0 | yes<br>no |
| 244 | TLFB-04-10 | Methadone: | 1<br>0 | yes<br>no |
| 245 | TLFB-04-11 | Heroin: | 1<br>0 | yes<br>no |
| 246 | TLFB-04-12 | Buprenorphine: | 1<br>0 | yes<br>no |
| 247 | TLFB-04-13 | Fentanyl: | 1<br>0 | yes<br>no |
| 248 | TLFB-04-14 | Other opioids: | 1<br>0 | yes<br>no |
| 249 | TLFB-04-15 | Xylazine: | 1<br>0 | yes<br>no |
| 250 | TLFB-04-16 | Hallucinogens: | 1<br>0 | yes<br>no |
| 251 | TLFB-04-17 | Ketamine: | 1<br>0 | yes<br>no |
| 252 | TLFB-04-18 | Benzodiazepines: | 1<br>0 | yes<br>no |
| 253 | TLFB-05-01 | Visit 5 date | YYYY-MM-DD<br>-97<br>-98 | <br>Intervention Not Delivered<br>Left Blank/Skipped |
| 254 | TLFB-05-02 | Have you used opioids or any other substances during the assessment period? | 1<br>0<br>-97<br>-98 | yes<br>no<br>Intervention Not Delivered<br>Left Blank/Skipped |
| 255 | TLFB-05-03 | e-Cigarettes or nicotine vape: | 1<br>0 | yes<br>no |
| 256 | TLFB-05-04 | Other tobacco: | 1<br>0 | yes<br>no |
| 257 | TLFB-05-05 | Alcohol: | 1<br>0 | yes<br>no |
| 258 | TLFB-05-06 | Marijuana: | 1<br>0 | yes<br>no |
| 259 | TLFB-05-07 | Cocaine/crack: | 1<br>0 | yes<br>no |
| 260 | TLFB-05-08 | Methamphetamine: | 1<br>0 | yes<br>no |
| 261 | TLFB-05-09 | Amphetamine-type stimulants (including non-prescribed prescription stimulants) | 1<br>0 | yes<br>no |
| 262 | TLFB-05-10 | Methadone: | 1<br>0 | yes<br>no |
| 263 | TLFB-05-11 | Heroin: | 1<br>0 | yes<br>no |
| 264 | TLFB-05-12 | Buprenorphine: | 1<br>0 | yes<br>no |
| 265 | TLFB-05-13 | Fentanyl: | 1<br>0 | yes<br>no |
| 266 | TLFB-05-14 | Other opioids: | 1<br>0 | yes<br>no |
| 267 | TLFB-05-15 | Xylazine: | 1<br>0 | yes<br>no |
| 268 | TLFB-05-16 | Hallucinogens: | 1<br>0 | yes<br>no |
| 269 | TLFB-05-17 | Ketamine: | 1<br>0 | yes<br>no |
| 270 | TLFB-05-18 | Benzodiazepines: | 1<br>0 | yes<br>no |
