import datetime
import requests

API_KEY = "bjwjjRu6SQd72GYbcREwBTVp7msan3WcJ72dxGAS"

#Current Date
today = datetime.date.today()

formatted_date = today.strftime("%Y-%m-%d")

nasa_url = (
    f"https://api.nasa.gov/neo/rest/v1/feed?"
    f"start_date={formatted_date}&"
    f"end_date={formatted_date}&"
    f"api_key={API_KEY}"
)


print(f"Requesting Tracking Coordinates for {formatted_date}")

response = requests.get(nasa_url)

print(f"Connection Status Code: {response.status_code}")  # 200 signifies successful connection

if response.status_code == 429:
    print("\nNASA API Limit hit... Change the API Demo Key mate or whatever key is placed")
    exit()
elif response.status_code != 200:
    print(f"\nFailed to contact with NASA, server responded with the code {response.status_code}")
    exit()


#Json to python dictionary
data = response.json()

#Self explanatory: Asteroids/objects passing Earth Today.
asteroid_today = data["near_earth_objects"][formatted_date]

#Total Objects passin right now
print(f"Analysis Done: There are {len(asteroid_today)} objects passing Earth today.")

#TODO: Take out data, loop through, and find the details of these objects.


print("\n----------Object Details-----------")

for asteroid in asteroid_today:
    name = asteroid["name"]
    print(f"\n\n{name}") # Test Successful 

    # Average Diameter in meter 🗿
    dia_min = asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"]
    print(f"Min Dia: {dia_min}m") # Test Successful 
    dia_max = asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"]
    print(f"Max Dia: {dia_max}m") # Test Successful 

    dia_avg = (dia_max + dia_min)/2
    print(f"Average Dia: {dia_avg}m") # I'll avoid testing again and again needlesly to make sure API limits doesn't cause me trouble...

    # Relative Velocity (klicks/hr)
    approach = asteroid["close_approach_data"][0]
    # print(f"Approach Data: {approach}") # Printing it cause a whole lot of mess, so yeah, the next part is imp.

    velocity = float(approach["relative_velocity"]["kilometers_per_second"])
    print(f"Velocity data: {velocity} klicks/sec")


    # Checking Hazard
    is_hazard = asteroid["is_potentially_hazardous_asteroid"]
    print(f"The Hazard Status is {is_hazard}. \nTherefore {"💀 Hazardous" if is_hazard else "🦺 Safe"}")


    print("\n-----SUMMARY-----\n")
    print(f"Asteroid: {name} {is_hazard}")
    print(f"Avg Diameter = {dia_avg:.2f} meters")
    print(f"Velocity = {velocity:.2f} km/s")










#                                  TOMORROW
# ------------------------------PHYSICS CORE--------------------------------------------------



import math

