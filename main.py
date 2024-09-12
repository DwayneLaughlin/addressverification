import pandas as pd
import numpy as np
from flask import Flask

app = Flask.__name__
df = pd.read_csv('addresses.csv')


address = "42 Fairhaven Commons Way"
city = "Fairhaven"
state = "MA"
zip = 2719

def address_search():
   #boolean checks to make sure that the city, state, address, and zip are present in dataset
   city_check = df['city'].eq(city).any()
   address_check = df['address'].eq(address).any()
   state_check = df['state'].eq(state ).any()
   zip_check = df['zip'].eq(zip).any()


   #if all info is present in the database, this will check that all address info points to the same index in database
   if((city_check) and (address_check) and (state_check) and (zip_check)):
      address_index = df.index[df['address'] == address][0]
      
      #Check to make sure that the city, state, and zip for the given address matches the submitted information for city, state, and zip. If all information matches, the index/row location for the address is returned
      city_comparison = str(df.query("address=='" + address + "'")["city"].values)
      zip_comparison = str(df.query("address=='" + address + "'")["zip"].values)
      state_comparison = str(df.query("address=='" + address + "'")["state"].values)
      formatted_zip = str([zip])
   
      if not ((city_comparison == "['" + city + "']") and (state_comparison == "['" + state + "']") and (zip_comparison == formatted_zip)):
         print ("Ambiguous address information submitted. Multiple records found. Please double check information and resubmit")
      else:
         print("Found at index: " + str(address_index))
   else:
      print ('Address not found')
        
address_search()