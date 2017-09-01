import requests
import time
import configparser

api_key = ''

if api_key == '':
    config = configparser.SafeConfigParser()
    config.read('apikey.ini')
    api_key = config.get('SectionOne','key')

t = time.strftime("%Y-%m-%d")
print (t)

payload = {'end_date': t, 'start_date': t, 'api_key': api_key}
nasa = requests.get ('https://api.nasa.gov/neo/rest/v1/feed', params=payload)

n = nasa.json()
print("Number of Objects:", n["element_count"])

print ('end')
