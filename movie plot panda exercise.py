#2. Let's inspect the data. Display the first rows and get the summary (.info)

#3. Print out the number of movies for each Origin/Ethnicity: 

import pandas as pd
df = pd.read_csv("movie_plots.csv")

pd.set_option('display.max_columns', 9)
pd.set_option('display.max_colwidth', 10)

filtered_row = df[ df["Origin/Ethnicity"] == "American" ]
print(filtered_row) 

# 17377 films zijn American

filtered_row = df[ df["Origin/Ethnicity"] == "British" ]
print(filtered_row) 

# 3670 films zijn British

filtered_row = df[ df["Origin/Ethnicity"] == "Bollywood" ]
print(filtered_row) 

# 2931 films zijn uit Bollywood

filtered_row = df[ df["Origin/Ethnicity"] == "Tamil" ]
print(filtered_row) 

# 2599 films zijn Tamil

filtered_row = df[ df["Origin/Ethnicity"] == "Telugu" ]
print(filtered_row) 

# 2599 films zijn Telugu

#4. Subsetting: select only the rows with Bollywood movies:

df = pd.read_csv("movie_plots.csv")
filtered_row = df[ df["Origin/Ethnicity"] == "Bollywood" ]
print(filtered_row) 

#5. Subsetting: select only the rows with Turkish movies released after 2000

print(df[(df["Release Year"] > 2000 ) & (df["Origin/Ethnicity"] == "Turkish") ])

#6. Subsetting: create a new df with only Title, Release Year, Origin/Ethnicity,Plot

newdf = df[["Title", "Release Year", "Origin/Ethnicity", "Plot"]]
print(newdf)

#7. Change the column names to Title, Year, Origin, Plot. Find online how to this.

newnames = newdf.rename(columns={'Release Year':'Year'} {'Origin/Ethnicity':'Origin'})
print(newnames)
#ik kan niet vinden hoe je meerdere columns kan wijzigen

