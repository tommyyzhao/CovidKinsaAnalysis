# Analysis of Kinsa data and Covid data

Exploratory data analysis on Kinsa data with Covid data

## Kinsa data:
Obtained from Kinsa's Health Weather public API

Data Returned:
- Region_id string 
- Region_name string
- State string
- Date string
- Observed_ili float - Daily influenza-like illness incidence in the specified region on the specified date. Null starting on current date.
- Atypical_ili float - Will contain the observed ILI if it is atypical, otherwise is null
- Anomaly_diff  float - Measure of much atypical illness is present in the region. It is quantified by subtracting the upper bound of the typical illness range from the observed illness. If anomaly_diff is 0 it means that the observed illness is either in the typical range or lower than typical. Null starting on current date, otherwise if anomaly_diff is null Kinsa does not have enough data from the county to identify atypical illness levels.
- Forecast_expected  float - Where Kinsa expects illness to be based on the time of year – specific to each individual county. Null before March 2. For details on how we determine expected illness, please review our technical approach.
- Forecast_lower  float - The lower bound of Forecast_expected
- Forecast_upper  float - The upper bound of Forecast_expected

For more details on how these values are determined: https://content.kinsahealth.com/covid-detection-technical-approach

## Covid-19 (county-level) data
County level data on Covid-19 from the New York Times (https://github.com/nytimes/covid-19-data)

Data:
- date string
- county string 
- state string
- fips string
- cases int
- deaths int
