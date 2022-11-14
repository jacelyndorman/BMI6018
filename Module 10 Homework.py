#In this assignment you will experiment on your own. Using a health dataset of your choice (check with us if you are not sure), write code to demonstrate the following Pandas functions:

#Melt

import pandas as pd
import numpy as np

data = pd.read_csv("diabetic_data.csv")

melted = pd.melt(data, id_vars = ["race"], value_vars = ["gender", "age"]) #getting info on race, gender, and age of data pool

print(melted)


#Pivot

pivoted = data.pivot_table(index = "age", columns = "time_in_hospital", values = "num_medications") #seeing potential correlation between time in hospital and number of medications, grouped by age
print(pivoted)

#Aggregation

aggregated = data.agg({"age" : ["max", "min"], "weight" : ["max"], "num_lab_procedures" : ["min", "mean", "max", "std"]})

print(aggregated)  #finding max and min age and max weight for patients, getting statistics on number of lab procedures

#Iteration

for column in data: #printing column names, maybe we didn't know what kind of information the file contained
    print(column)
    
#Groupby

groupby = data.groupby(["gender"]).mean(numeric_only = True) #finding mean of columns based on gender, obviously some columns do not give useful data when they are averaged, but this is just to show how it's done

print(groupby)

