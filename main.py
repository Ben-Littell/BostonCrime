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

lar_df = d_df[d_df['OFFENSE_CODE_GROUP'] == 'Larceny']
# print(lar_df.info())
lar_lat_df2 = lar_df['Lat'].dropna()
lar_long_df2 = lar_df['Long'].dropna()
# print(lar_df.info())
# lar_df.Lat.dropna()
# print(lar_lat_df2)
lar_lat_list = lar_lat_df2.values.tolist()
lar_long_list = lar_long_df2.values.tolist()

# print(lar_lat_list)
for v in lar_lat_list:
    if v == -1.0:
        lar_lat_list.remove(v)
for v in lar_long_list:
    if v == -1.0:
        lar_long_list.remove(v)
# print(len(lar_lat_list), len(lar_long_list))
m = folium.Map([42.32, -71.0589], zoom_start=12)
for val in range(len(lar_lat_list)):
    folium.Marker(location=(lar_lat_list[val], lar_long_list[val])).add_to(m)

m.save('index.html')





