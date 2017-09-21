# Incoming
Queries NASA Near Earth Asteroid API

This script displays the number of asteriods that are on there closest aproatch to the earth today.
Potential real world aplications of this technology include: curing parinoia, insomnia, and other end of the world related worrys.

To run the script get a api key from nasa (you only need an email) at this address: https://api.nasa.gov/index.html#apply-for-an-api-key
Or you can just use the api key: DEMO_KEY
DEMO_KEY is limited to 30 requests per IP address per hour/50 requests per IP address per day
A requested key is limited to 1,000 requests per hour

Either way place your chosen api key in the space provided on line 5
If that sounds to easy you may use a .ini file 
Name the file apikey.ini then fill it in as following:

[SectionOne]

key: your api key here


You also need to install the requests library.
Help with that: http://docs.python-requests.org/en/master/user/install/


Happy asteroid hunting!!!
