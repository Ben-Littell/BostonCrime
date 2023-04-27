import func
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import folium

plt.style.use('Solarize_Light2')

d_df = pd.read_csv('crime.csv', encoding='latin1', low_memory=False)
# print(d_df.info())
ti_s = d_df.HOUR.value_counts()
ti_s.sort_index(inplace=True)

# ti_s.plot.bar()
# plt.title('Hour to Crimes Committed for 2015-2017')
# plt.ylabel('Number of Crimes Committed')
# plt.show()

# 2016
df_16 = d_df[d_df['YEAR'] == 2016]

# Months

aug_16 = df_16[df_16['MONTH'] == 8]

aug_16_wed = aug_16[aug_16['DAY_OF_WEEK'] == 'Wednesday']
aug_16_wed_hours = aug_16_wed.HOUR.value_counts()
aug_16_day_counts = aug_16.DAY_OF_WEEK.value_counts()

aug_16_wed_hours.sort_index(inplace=True)

# aug_16_day_counts.plot.bar()
# plt.show()
# print(aug_16_day_counts)
# df_17 = d_df[d_df['YEAR'] == 2017]


# for val in range(1, 13):
#     func.find_data(d_df, 2016, val, 'Monday')
# Fire Related Reports
# Homicide
boston_districts = {'Downtown': 'A1', 'Charleston': 'A15',
                    'East Boston': 'A7', 'Roxbury': 'B2',
                    'Mattapan': 'B3', 'South Boston': 'C6',
                    'Dorchester': 'C11', 'South End': 'D4',
                    'Brighton': 'D14', 'West Roxbury': 'E5',
                    'Jamaica Plain': 'E13', 'Hyde Park': 'E18'}

func.map_crime(d_df, 'Homicide', 'E13')

func.dis_crime_accurance(boston_districts, d_df)
