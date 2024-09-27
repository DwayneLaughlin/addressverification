import pandas as pd
import csv
import numpy as np
from flask import Flask


app = Flask(__name__)
df = pd.read_csv('addresses.csv')


address1 = "42 Fairhaven Commons Way"
city1 = "Fairhaven"
state1 = "MA"
zip1 = 2719

def address_search(address, city, state, zip):
   if address == None:
      raise Exception("Address cannot be empty")
   if city == None:
      raise Exception("City cannot be empty")
   if state == None:
      raise Exception("State cannot be empty")
   if zip == None:
      raise Exception("Zip cannot be empty")
   
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
         return ("Ambiguous address information submitted. Multiple records found. Please double check information and resubmit")
      else:
         return (df.iloc[address_index].to_string())
   else:
      return ('Address not found')
   
def add_address(address, city, state, zip):
   if address == None:
      raise Exception("Address cannot be empty")
   if city == None:
      raise Exception("City cannot be empty")
   if state == None:
      raise Exception("State cannot be empty")
   if zip == None or zip == "":
      raise Exception("Zip cannot be empty")
   df.loc[len(df.index)] = [address1, city1, state1, zip1]
   print(len(df))

        
# Flask
# @app.route('/')
# def get_address():
#    results = add_address(address1, city1, state1, zip1)
#    return results


# if __name__ == "__main__":
#     app.run()