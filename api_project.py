import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
import csv


@dataclass
class Bird:
    name: str
    latin_name: str
    active_time: str
    length_min: float = field(metadata={"units": "feet"})
    length_max: float = field(metadata={"units": "feet"})
    weight_min: float = field(metadata={"units": "lbs"})
    weight_max: float = field(metadata={"units": "lbs"})
    lifespan: float = field(metadata={"units": "years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id_: int


@dataclass
class Reptile:
    name: str
    latin_name: str
    active_time: str
    length_min: float = field(metadata={"units": "feet"})
    length_max: float = field(metadata={"units": "feet"})
    weight_min: float = field(metadata={"units": "lbs"})
    weight_max: float = field(metadata={"units": "lbs"})
    lifespan: float = field(metadata={"units": "years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id_: int


@dataclass
class Mammal:
    name: str
    latin_name: str
    active_time: str
    length_min: float = field(metadata={"units": "feet"})
    length_max: float = field(metadata={"units": "feet"})
    weight_min: float = field(metadata={"units": "lbs"})
    weight_max: float = field(metadata={"units": "lbs"})
    lifespan: float = field(metadata={"units": "years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id_: int


@dataclass
class Marsupial:
    name: str
    latin_name: str
    active_time: str
    length_min: float = field(metadata={"units": "feet"})
    length_max: float = field(metadata={"units": "feet"})
    weight_min: float = field(metadata={"units": "lbs"})
    weight_max: float = field(metadata={"units": "lbs"})
    lifespan: float = field(metadata={"units": "years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id_: int


@dataclass
class Amphibian:
    name: str
    latin_name: str
    active_time: str
    length_min: float = field(metadata={"units": "feet"})
    length_max: float = field(metadata={"units": "feet"})
    weight_min: float = field(metadata={"units": "lbs"})
    weight_max: float = field(metadata={"units": "lbs"})
    lifespan: float = field(metadata={"units": "years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id_: int


@dataclass
class Fish:
    name: str
    latin_name: str
    active_time: str
    length_min: float = field(metadata={"units": "feet"})
    length_max: float = field(metadata={"units": "feet"})
    weight_min: float = field(metadata={"units": "lbs"})
    weight_max: float = field(metadata={"units": "lbs"})
    lifespan: float = field(metadata={"units": "years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id_: int


#### Create Instances of Classes

# Set url for API call
path = "https://zoo-animal-api.herokuapp.com/animals/rand/10"

# Create Class Dictionary for concise Instance Creations
class_dictionary = {
    "Amphibian": Amphibian,
    "Bird": Bird,
    "Marsupial": Marsupial,
    "Mammal": Mammal,
    "Reptile": Reptile,
    "Fish": Fish,
}

# Create list to store instances
object_list = []

# Get a list of all classes in dictionary
# Possibly unnecessary as the same could be achieved using the actual dictionary
animal_classes = [_ for _ in class_dictionary.keys()]

# Create a list to store the ids of found animals so that we don't repeat objects
animal_ids = []

# start a counter that will be used to determine if we can break the api call loop early
cntr = 0

# Create a loop for 100 (99 in reality) calls to the api due to limit of how many
# objects can be returned in each call.
for iteration in range(100):

    # Get the json response from the API
    data = requests.get(path).json()

    # Check to see if the call loop can be broken early
    if cntr > 30:
        print("\nPossibly have got most of the animals")
        print(f"It took {iteration} rounds.")
        print(f"We found {len(object_list)} animals")
        break

    # Check each returned item for the information that we need
    for item in data:

        # Get a list of all the keys in the item that we want to use
        interest_list = [_ for _ in item.keys() if _ != "animal_type"]

        # Get a list of all the aspects of the item that we want to use
        animal = [item[key] for key in interest_list]

        # Check if we already have the animal
        if item["id"] not in animal_ids:

            # Create an instance of the animal and add it to the object list
            try:
                object_list.append(class_dictionary[item["animal_type"]](*animal))
            except:
                # If the animal type is not in our classes then the attempt to add it will fail
                if item["animal_type"] not in animal_classes:
                    print(f"It looks like we do not have {item['animal_type']} yet")
                else:
                    print(
                        "Not really sure what happened here. Let me ponder this for a while..."
                    )
                    print("Starting infinite loop...")

            # Add the id of the animal to our list of found animals so that we don't add it again
            animal_ids.append(item["id"])
            cntr = 0
        else:
            # Advance the cntr if the animal is already in the data
            # (this helps to determine how frequently all of the random animals have already been added)
            cntr += 1
