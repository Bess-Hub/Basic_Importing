# This exercise consists in making an app that gives 10 cultural activities to do in Madrid
# The data is from Ayuntamiento de Madrid and consists in cultural events in the next 100 days
import requests
import pandas as pd
from tabulate import tabulate
import json

# Using requests module, get the data
response = requests.get('https://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.json').text

# I printed the code bellow to confirm we were dealing with .json - I LIKE DOING THIS JUST BECAUSE BETTER SAFE THAN SORRY
# print(response.headers.get('content-type'))

# Using json module to load the response into a new variable
response_info = json.loads(response)

# Create a variable that contain the information within @graph
list = response_info["@graph"]

# Using pandas module create the dataframe
df = pd.DataFrame(data=list, columns=['title','description','event-location', 'dtstart'])
# Since it is a very long list we will filter just 10 events out of it
df_filtered=df. head(10)

# Set the initial message and interaction with the user
print()
print()
print("Welcome to your Madrid activity finder!")
print()
run = str(input("Do you want to check the upcoming activities? (Y/N) "))

# Create the IF / ELIF and ELSE
if run in ("Y", "y", "yes", "YES"):
    print(tabulate(df_filtered, showindex=True, tablefmt="double_grid", maxcolwidths=[20,20,20,9], headers=['Title','Details','Location','When']))

elif run in ("N", "n", "no", "NO"):
    print()
    print("Run this code again if you change your mind, Madrid is fun and has plenty of activities to enjoy!")
    print()

else:
    print()
    print("Upsie, something went wrong. Try again!")
    print()
    
# Done. :)
