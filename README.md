# Surf's Up
## Overview and Deliverables
A surf professional requested additional weather information regarding temperature on the island of Oahu ahead of an investment meeting.  Specifically, he wanted to know about temperature data for the months of June and December on Oahu to help determine if a surf and ice cream shop business would be sustainable year-round.  The following deliverables were requested:
  - Summary statistics for temperature for the month of June for Oahu
  - Summary statistics for temperature for the month of December for Oahu

## Resources
- Data Sources: hawaii.sqlite
- Software and Programming Languages: Jupyter Notebook v. 6.4.6; pandas v. 1.0.5; numpy v. 1.18.5; Python v. 3.8.3 :: Anaconda, Inc.; conda v. 4.11.0; SQLAlchemy v. 1.3.18; Matplotlib v. 3.2.2; flask v. 1.1.2

## Results
Temperature findings for June and December were based on daily temperature recordings from nine weather stations on the island of Oahu.  June temperatures included data from 2010 to 2017 whereas December temperatures included data from 2010 to 2016. Some weather stations were more active that others, which resulted in a maximum of nine temperatures being recorded for some days and fewer temperatures recorded on other days.

### Overall Findings
  - Mean temperature for June was 74.9 F and 71 F for December
  - Max temperature for June was 85 F and 83 F for December
  - Min temperature for June was 64 F and 56 F for December
  - The upper three quartiles show June temperatures above 73 F and December temperatures above 69 F.

![June temps](https://user-images.githubusercontent.com/95387273/153902405-e3e78b99-6158-436b-a482-3b2292d01ea0.png)

Fig. 1.  Summary statistics for temperature (deg F) for the month of June on the island of Oahu.


![Dec temps](https://user-images.githubusercontent.com/95387273/153902458-c5b06f1e-35f3-4a6a-9712-8f33599772f1.png)

Fig. 2.  Summary statistics for temperature (deg F) for the month of December on the island of Oahu.

## Summary
A majority of temperatures for June and December fall above 69 F, an acceptable surfing temperature. Considering that the standard deviation is +/- 3.2 F and 3.7 F for June and December, respectively, temperatures in December could fall around 67 F, about 4 degrees below the mean, which is still an acceptable surfing temperature.

### Additional Recommended Analyses
- Plot temperature data for June and December separately to see how many days fall above 60 deg F.

- Filter based on precipitation for the months of June and December across the same years, then plot precipitation along with temperature in a single bar graph in order to understand basic trends.

- Filter for both precipitation and temperature for each of the nine weather stations for June and December across the same years.  Some weather stations may be located in mountainous areas, so would not be found in warmer areas along the ocean where the surf and ice cream shop would be located.  Mountainous weather stations could be identified to determine if the temperature and precipitation data from these sites differ from those located along shore sites. This would help determine where the minimum temperatures originate.
### Limitations of the Data
- These data do not include information fo climate change.  It is highly recommended that projections for sea level rise, prevailing winds, and temperature changes be included in the business plan.
