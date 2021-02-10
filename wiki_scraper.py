from bs4 import BeautifulSoup
import requests
from requests.api import head
import csv

csv_file = open('knowledge_base.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow((['Subject','Predicate','Object']))

# urls will be a list containg all the links for famous people
Names = ['Alan_Turing','Albert_Einstein','Isaac_Newton','Elon_Musk','Jeff_Bezos','Steve_Jobs','Sundar_Pichai','Mark_Zuckerberg','Bill_Gates','The_Weeknd']

for name in Names:
    source = requests.get('https://en.wikipedia.org/wiki/'+name).text
    soup = BeautifulSoup(source,'lxml')
    table = soup.find('table',class_='infobox biography vcard')
    rows = table.find_all('tr')
    for info in rows:
        try:
            Predicate = info.th.text.replace('\n', ' ')
            Object = info.td.text.replace('\n', ', ')
            if (Object[0]==','):
                csv_writer.writerow([name,Predicate,Object[2:-2]])
            else:
                csv_writer.writerow([name,Predicate,Object])
        except Exception as e:
            pass
print("Go checkout the knowledge_base.csv file")
csv_file.close()
# This will generate a CSV file in which we have them in the Subject, Predicate and Object form