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

df2['GDP (in USD)']=df2['GDP (in USD)'].str.replace(' billion', '') # removes the string 'billion' from the column GDP (in USD)

GDB_Year = df2[['Year', 'GDP (in USD)']].iloc[8:].dropna().astype(float)

print(GDB_Year)
