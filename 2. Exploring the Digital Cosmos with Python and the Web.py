# Problem Statement: Imagine you are a developer tasked with creating a feature for a 
# web application that provides users with insightful information about various space objects. 
# Your application will fetch data from a publicly available space API, process this data, and 
# display it in a user-friendly format.

# Task 1: Set up a Python Virtual Environment and Install Required Packages

# Create a new virtual environment in Python. Activate the virtual environment. 
# Install the `requests` package for making HTTP requests.

# Expected Outcome: A successfully created and activated virtual environment with the `requests` package installed.

#  Task 2: Fetch Data from a Space API Write a Python script that makes a GET request to a 
# space API (e.g., [The Solar System OpenData](https://api.le-systeme-solaire.net/en/)) to fetch data about planets.

# Parse the JSON response and extract information about each planet, such as its name, mass, and orbit period.



import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies'] 

    for planet in planets:
        if planet['isPlanet']:
            name = planet.get("englishName", "No name")
            mass = planet.get('mass', {}).get('massValue', 'Unknown')
            orbit_period = planet.get("sideralOrbit")
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    return planets


def find_heaviest_planet(planets):
    heaviest_mass = -1
    heaviest_planet = None

    for planet in planets:
        if planet['isPlanet']:
            mass_value = planet.get('mass', {}).get('massValue')
            if mass_value and mass_value != 'Unknown':
                mass_value = float(mass_value)
                if mass_value > heaviest_mass:
                    heaviest_mass = mass_value
                    heaviest_planet = planet

    if heaviest_planet:
        name = heaviest_planet.get('englishName', 'Unknown')
        mass = heaviest_planet.get('mass', {}).get('massValue', 'Unknown')
        return name, mass
    else:
        print("Error.")


planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")

#Expected Outcome: A more structured and formatted output, along with an analysis result, such as 
# identifying the heaviest planet in the solar system.
