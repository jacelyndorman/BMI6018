#%% Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%% Importing Data
flights_data = pd.read_csv(r"C:\Users\jacel\OneDrive\Desktop\Python Projects\flights.csv") #you will need to change the path on your computer
flights_data.head(10)
weather_data_pd = pd.read_csv(r"C:\Users\jacel\OneDrive\Desktop\Python Projects\weather.csv")#you will need to change the path on your computer
weather_data_np = weather_data_pd.to_numpy()
#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data
#Question 1 How many flights were there from JFK to SLC? Int

howmany = flights_data.loc[(flights_data["origin"] == "JFK") & (flights_data["dest"] == "SLC")]

q_1 = len(howmany.index)
print(q_1)

#Question 2 How many airlines fly to SLC? Should be int

airlines = flights_data.loc[flights_data["dest"] == "SLC"]

q_2 = len(airlines.groupby(["carrier"]).count())
print(q_2)

#Question 3 What is the average arrival delay for flights to RDU? float

average = flights_data.loc[flights_data["dest"] == "RDU"]

q_3 = average["arr_delay"].mean()
print(q_3)

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float

toseattle = flights_data.loc[flights_data["dest"] == "SEA"]
proportion = toseattle.loc[(toseattle["origin"] == "LGA") | (toseattle["origin"] == "JFK")]

numbertoseattle = len(toseattle.index)
numberfromjfk = len(proportion.index)
q_4 = numberfromjfk / numbertoseattle
print(q_4)

#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)

year = flights_data['year']
month = flights_data['month']
day = flights_data['day']
date = pd.concat([year,month,day], axis = 1)
hotdates = pd.to_datetime(date).dt.strftime('%Y/%m/%d')

flights_data["Date"] = hotdates
dep_delay_sorted = flights_data.groupby(["Date"]).mean(numeric_only = True).sort_values("dep_delay", ascending = False)

q_5 = dep_delay_sorted["dep_delay"].head(1) #wasn't sure if you wanted just the date or the delay as well
print(q_5)

#Question 6 Which date has the largest average arrival delay? pd slice with date and float
#date column previously added in question 5
arr_delay_sorted = flights_data.groupby(["Date"]).mean(numeric_only = True).sort_values("arr_delay", ascending = False)

q_6 = arr_delay_sorted["arr_delay"].head(1) #wasn't sure if you wanted just the date or the delay as well
print(q_6)

#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime

flights_data["Speed"] = flights_data["distance"]/flights_data["air_time"]
jfk_lga = flights_data.loc[(flights_data["origin"] == "LGA") | (flights_data["origin"] == "JFK")]
sorted_jfk_lga = jfk_lga.sort_values("Speed", ascending = False)
q_7 = sorted_jfk_lga[["tailnum", "Speed"]].head(1)

print(q_7)

#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans

q_8 = weather_data_pd.fillna(0)
print(q_8)

#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int

array = weather_data_np[:, 3] == 2.0 #makes array of "months = 2"
q_9 = np.count_nonzero(array) 
print(q_9)

#Question 10 What was the mean for humidity in February? Float

months = weather_data_np[:, [3]]
humidity = weather_data_np[:, [8]]
mask = months == 2
just_humidity_february = humidity[mask]
q_10 = np.nanmean(just_humidity_february)
print(q_10)


#Question 11 What was the std for humidity in February? Float

q_11 = np.std(just_humidity_february) #created array in last question

print(q_11)

