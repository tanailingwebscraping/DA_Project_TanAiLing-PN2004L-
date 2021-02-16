#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse the top 3 countries in SEA with the most number of visitors to Singapore 
#Name: <Tan Ai Ling>
#Group Name: <JAS>
#Class: <PN2004L>
#Date: <9 Febuary 2021
#Version: <1.0>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthlyVisitors(SEA)1996 - 2006.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)

  #display a specific country (e.g.Philippines ) in column #5
  country_label = df.columns[5]
  print("\n\n" + country_label + "was selected.")

  #display a sorted dataframe based on selected country
  print(" The" + country_label + "was sorted in ascending order. \n")
  sorted_df =df.sort_values(country_label,ascending=[0])
  print(sorted_df)

  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################