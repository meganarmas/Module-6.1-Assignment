# Objective: The aim of this assignment is to deepen your understanding and practical skills in 
# web technologies and Python programming. You will explore the functionalities of the World Wide Web, 
# web architectures, and the Python programming language, particularly focusing on setting up environments, 
# API interactions, and data handling.

# Problem Statement: You are tasked with creating a Python application that interfaces with a 
# public API, fetches data, and processes it. This application should provide insights into how 
# different web architectures work and demonstrate your ability to set up a Python environment, 
# make API requests, and handle JSON data.

# Task 1: Setting Up a Python Virtual Environment and Installing Packages

# 1. Create a new Python virtual environment in your project directory.

# 2. Activate the virtual environment.

# 3. Install the `requests` packages.

# Expected Outcome: A successfully created and activated virtual environment with the required packages installed.

# Task 2: Fetching Data from the Pokémon API

# 1. Write a Python script to make a GET request to the Pokémon API (`https://pokeapi.co/api/v2/pokemon/pikachu`).

# 2. Extract and print the name and abilities of the Pokémon.

import requests
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

json_data = response.text

pikachu_data = json.loads(json_data)

print(pikachu_data["name"])
print(pikachu_data["abilities"])


# Expected Outcome: The script should output the name of the Pokémon (Pikachu) and a list of its abilities.

# Task 3: Analyzing and Displaying Data

# 1. Modify the script to fetch data for three different Pokémon.

# 2. Create a function to calculate and return the average weight of these Pokémon.

# 3. Print the names, abilities, and average weight of the three Pokémon. **Code Example:**

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        pokemon = response.json()

        name = pokemon.get("name", "No name")
        abilities = pokemon.get("abilities", [])
        weight = pokemon.get("weight", 0)
        print(f"Name: {name} \n Abilities: {abilities}")
        
        for ability_info in abilities:
            ability = ability_info.get("ability", {})
            ability_name = ability.get("name", "Unknown")
            print(f" - {ability_name}")
        return weight   
    except:
        print("Error in Request")
        return None

def calculate_average_weight(pokemon_list):
    total_weight = 0
    count = 0
    for pokemon_name in pokemon_list:
        weight = fetch_pokemon_data(pokemon_name)
        if weight is not None:
            total_weight += weight
            count += 1
    if count > 0:
        average_weight = total_weight / count
        print(f"Average weight: {average_weight:.2f}")
    else:
        print("No valid Pokémon weights found.")


pokemon_list = ["pikachu", "bulbasaur", "charmander"]
calculate_average_weight(pokemon_list)
# Expected Outcome: The script should display the names and abilities of the three chosen 
# Pokémon and their average weight. The function should correctly calculate and return the average 
# weight based on the data fetched from the API. 