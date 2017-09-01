import time
import configparser

def current_time():
    t = time.strftime("%Y-%m-%d")
    return(t)

def key():
    api_key = ''
    if api_key == '':
        config = configparser.SafeConfigParser()
        config.read('apikey.ini')
        api_key = config.get('SectionOne','key')
        return(api_key)
