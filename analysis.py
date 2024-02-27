import lib
'''here creates two dataframes from two datasets'''
df = lib.pd.read_csv("data.csv")
df2 = lib.pd.read_csv("Israel-Palestine.csv")

'''This is first data frame, It shows two columns Year and Housing Units.
 Here removes the rows where the elements in Year or in Housing Units are Nan.
we then convert the data to integer using astype method.
'''

Year_House = df[['Year', 'Housing Units']].dropna().astype(int)
df_sorted = Year_House.groupby('Year').sum()

#print(df_sorted)

'''Here shows two columns Year and GDP (in USD) and then we remove the rows where 
the elements are Nan. This show the data from 2004 like the first dataframe.'''

df2['GDP (in USD)']=df2['GDP (in USD)'].str.replace(' billion', '').astype(float)# removes the string 'billion' from the column GDP (in USD) and make it float
#print(df2)
df2['Year'] = df2['Year'].astype(int) # The data-type is converted to integer
GDB_Year = df2[['Year', 'GDP (in USD)', 'Country']].iloc[8:].dropna() # add one more column
GDB_Year=GDB_Year.set_index('Country') # make the country as index
GDB_Palestine = GDB_Year.loc['Palestine']
GDB_Israel = GDB_Year.loc['Israel']
