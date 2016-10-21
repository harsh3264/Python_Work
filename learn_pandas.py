1- Set index as 1

d = pd.read_csv('demo.csv')
d.index = np.arange(1,len(d)+1)

2- Ignore Warnings 

import warnings
warnings.filterwarnings("ignore")

3- Select only specific column of csv

import pandas
colnames = ['year', 'name', 'city', 'latitude', 'longitude']
data = pandas.read_csv('test.csv', names=colnames)
names = data.name.tolist()
latitude = data.latitude.tolist()
longitude = data.longitude.tolist()


4- Set fist column as index col

data = pd.read_csv('demo.csv',index_col=0)


5- How to change dtypes of the column

6- pandas read_csv and read_table has two options skiprow and skipfooter read documantation

7-  to add new column in a table 

data.['Location'] = data.city +  " ,   " + data.states

8- data.describe() describes all the possible int func 
     data.describr(include=['object'])

9- data.drop and data.drop_duplicates

10- data.rename(columns = {'colors' : 'Cols', 'size' : 'SZ'}, inplace = True)
       above one is just for one or two col replace
       if all the cols change data.columns = new_cols
       to replace space with _ in all columns
       data.columns = data.columns.str.replace(' ','_')

11 sort the rows by a column or two
	movies.sort_value('title',ascending=False)
    movies.sort_value(['title','duration'])


12 filter the dataframe by a column 
	is_long = movies.duration >= 200  # bool values
	print movies[is.long]
	print movies[movies.duration >= 200]  # simpler manner
	print movies[movies.duration >= 200].genre # Select only genre
	print movies.loc[movies.duration >= 200, 'genre'] # Better practice
	print movies[(movies.duration >= 200) & (movies.genre == 'Drama')]  # Combine with AND with & if OR then use | pipe operator
	print movies[movies.genre.isin(['Crime','Drama','Action'])]

 13 for loop look a like
 	for index,row in movie.iterrows():
 		print (index, row.title, row.genre)

 14 keep only numeric rows
 	movies.select_dtypes(include=[np.number]).dtypes