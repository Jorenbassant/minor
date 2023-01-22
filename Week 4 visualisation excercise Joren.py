import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("movie_plots.csv")


data = df['Genre']
countgenre = data.value_counts()

#make a barchart of the different types of Genre

countgenre.plot(kind='bar')

#create the table

plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Genre Count')

plt.show()