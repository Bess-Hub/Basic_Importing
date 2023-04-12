# Decided to create this code after examining the website to obtain "Cita Previa"
# Upon inspecting the website I noticed that:
  # 1. when there are no available slots for scheduling a ¨Cita Previa¨ a warning is displayed; and 
  # 2. when there are available slots no warning is displayed
# So all I had to do is create a code that would download and monitor if any change happens (meaning, if the warning appear or disappear) 

# We will be using some modules
import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime

# Define the target URL (in this case it must be the url of the search for Valencia specifically)
url = "https://icp.administracionelectronica.gob.es/icpplus/citar?p=46&locale=es&appkey=null"
# Set the headers, so it act like a browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

PrevVersion = ""
FirstRun = True
while True:

    # Start by downloading the page
    r = requests.get(url, headers=headers)
    # Then we parse the URL
    soup = BeautifulSoup(r.text, "lxml")
    
    # We do not need to monitor scripts or style, so lets get rid of it
    for script in soup(["script", "style"]):
        script.extract() 
    soup = soup.get_text()
    # Now we need to compare the page text to the previous version
    if PrevVersion != soup:
        # Well, the first time there is nothing to compaere to, just memorize it.
        if FirstRun == True:
            PrevVersion = soup
            FirstRun = False
            print ("We are monitoring ", url , "", str(datetime.now()))
        else:
            print ("Changes detected at: "+ str(datetime.now()))
            OldPage = PrevVersion.splitlines()
            NewPage = soup.splitlines()
            # compare versions and highlight changes using difflib
            d = difflib.Differ()
            diff = d.compare(OldPage, NewPage)
            out_text = "\n".join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip()])
            print (out_text)
            OldPage = NewPage
            #print ('\n'.join(diff))
            PrevVersion = soup
    else:
        print( "Nothing has changed by ", str(datetime.now()))
    time.sleep(60)
    continue
