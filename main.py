import requests
import time

import config

url = 'http://' + config.base_url + '/json/state'

print("Call payload One")
response = requests.post(url, config.bodyOne)
print("Response code: " + str(response.status_code))

time.sleep(5)

print("Call payload Two")
requests.post(url, config.bodyTwo)
print("Response code: " + str(response.status_code))

time.sleep(5)

print("Call payload Three")
requests.post(url, config.bodyThree)
print("Response code: " + str(response.status_code))

time.sleep(5)

print("Call payload Two")
requests.post(url, config.bodyTwo)
print("Response code: " + str(response.status_code))

time.sleep(5)

print("Call payload One")
requests.post(url, config.bodyOne)
print("Response code: " + str(response.status_code))

time.sleep(5)

print("Call payload Two")
requests.post(url, config.bodyTwo)
print("Response code: " + str(response.status_code))

print("Complete.")
