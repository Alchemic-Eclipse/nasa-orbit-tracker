import datetime
import requests
import time
import math

API_KEY = "DEMO_KEY"

def impact_nrg(avg_dia, velocity_km_s):

    # Avg Radius
    radius = avg_dia / 2

    # Volume, assuming it to be a sphere (approximation).
    volume = (4/3) * math.pi * (radius)**3

    # Avg Mass, assuming avg density to be 3000 kg/m^3
    density = 3000
    mass = density * volume

    # Velocity km/s --> m/s
    velocity_m_s = velocity_km_s * 1000

    # Kinetic Energy
    T = (1/2) * mass * (velocity_m_s)**2 # Joules

    # Converting to hiroshima bomb equivalents for better estimate 
    hiro_eq = T / (6.3 * 10**13) # 1 bomb on an avg
    return T, hiro_eq

today = datetime.date.today()

formatted_date = today.strftime("%Y-%m-%d")

nasa_url = (
    f"https://api.nasa.gov/neo/rest/v1/feed?"
    f"start_date={formatted_date}&"
    f"end_date={formatted_date}&"
    f"api_key={API_KEY}"
)



print("Welcome to NASA Orbit Tracker\n")
print(f"Requesting Tracking Coordinates for {formatted_date}")

response = requests.get(nasa_url)

# print(f"Connection Status Code: {response.status_code}")  # 200 signifies successful connection

if response.status_code == 429:
    print("\nNASA API Limit hit... Change the API Demo Key mate or whatever key is placed")
    exit()
elif response.status_code != 200:
    print(f"\nFailed to contact with NASA, server responded with the code {response.status_code}")
    exit()
else:
    print(f"🟩 Connection Established! \nCode: {response.status_code}\n")

# JSON to Py dict
data = response.json()

# Self explanatory: Asteroids/objects passing Earth Today.
asteroid_today = data["near_earth_objects"][formatted_date]

print("Kindly wait a few moments till we complete the analysis of tonight's sky.\n\n\n")
time.sleep(2)

#Total Objects passin right now
print(f"🟩 Analysis Done: There are {len(asteroid_today)} objects passing Earth today.\n")

for asteroid in asteroid_today:
    name = asteroid["name"]
    print(f"\n{name}\n")

input("Please press Enter for further details ")
time.sleep(1.5)

print("\n\n----------Object Details-----------")

for asteroid in asteroid_today: 
    name = asteroid["name"]
    print(f"\n\n{name}") 

    # Average Diameter in meter 🗿
    dia_min = asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"]
    print(f"Min Dia: {dia_min}m") # Test Successful 
    dia_max = asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"]
    print(f"Max Dia: {dia_max}m") # Test Successful 

    dia_avg = (dia_max + dia_min)/2
    print(f"Average Dia: {dia_avg}m") 

    # Relative Velocity (klicks/hr)
    approach = asteroid["close_approach_data"][0]
    # print(f"Approach Data: {approach}") # Printing it cause a whole lot of mess, so yeah, the next part is imp.

    velocity = float(approach["relative_velocity"]["kilometers_per_second"])
    print(f"Velocity data: {velocity} klicks/sec")
   
    # Checking Hazard
    is_hazard = asteroid["is_potentially_hazardous_asteroid"]
    print(f"The Hazard Status is {is_hazard}. \nTherefore {'💀 Hazardous' if is_hazard else '🦺 Safe'}")

    # Checking Impact
    joules, bombs = impact_nrg(dia_avg, velocity)
    print(f"Energy: {joules:.2e} J")
    print(f"Destructive Force: {bombs:.1f} Hiroshima Atomic bombs")


    print("\n-----SUMMARY-----\n")
    print(f"Asteroid: {name}, Hazardous: {"Yes" if is_hazard else "No"}")
    print(f"Avg Diameter = {dia_avg:.2f} meters")
    print(f"Velocity = {velocity:.2f} km/s")
    print(f"Equivalent to {bombs:.1f} Hiroshima Bombs")







                                



