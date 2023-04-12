# This exercise is to learn how to populate a CSV file with data form another source

# Lets import the modules we will be using
import requests
import csv
import time

# Let's use requests module function get to connect to the API
response = requests.get(url="https://thesimpsonsquoteapi.glitch.me/quotes")

# Verify its status
# print(response)

# Verify its output language
#print(response.headers.get('content-type'))

# Great! Now we know we are dealing with JSON. Requests can interpret json data, so we can create a variable named data
data = response.json()

# We can see the fields we can retrieve by printing it
#print(data)

# Great, we could get 'quote', 'character', 'image' and 'characterDirection
# We will want out CSV file to have a quote column and a character column, so we will retrieve the quote and the character
quote_s: str= data[0]['quote']
character_s: str= data[0]['character']

# Let's say we want to retrieve quotes from Lisa Simpson, we will make an IF statement that if character_s is equal to Lisa Simpson to add in the dictionary as csv file
if character_s == 'Lisa Simpson':
    dic_ = {'Quote': quote_s, 'Character': character_s}
    with open('/Lisa/Lisa.csv', 'a') as csvfile:
      w = csv.DictWriter(csvfile, dic_.keys())
      w.writerow(dic_)

# Lets do it for another Simpson as well
elif character_s == 'Homer Simpson':
    dic_ = {'Quote': quote_s, 'Character': character_s}
    with open('/Homer/Homer.csv', 'a') as csvfile:
      w = csv.DictWriter(csvfile, dic_.keys())

      w.writerow(dic_)

else:
    dic_ = {'Quote': quote_s, 'Character': character_s}
    with open('/General/General.csv', 'a') as csvfile:
      w = csv.DictWriter(csvfile, dic_.keys())
      w.writerow(dic_)

time.sleep(30) 
