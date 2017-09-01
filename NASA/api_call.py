import call_data
import requests

def call():
    day = call_data.current_time()
    api_key = call_data.key()
    payload = {'end_date': day, 'start_date': day, 'api_key': api_key}
    nasa = requests.get ('https://api.nasa.gov/neo/rest/v1/feed', params=payload)
    return (nasa)


