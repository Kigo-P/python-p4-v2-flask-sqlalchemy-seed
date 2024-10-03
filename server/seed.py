#!/usr/bin/env python3
#server/seed.py
#importing faker and rc(random choice)
from faker import Faker
from random import choice as rc

from app import app
from models import db, Pet

with app.app_context():

    # Creating and initializing the faker generator
    fake = Faker()
    
    # Deleting all the rows in the pets table before adding them
    Pet.query.delete()
    # Create an empty list
    pets = []

    # creating a varible called species
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    # Add some Pet instances to the list
    for n in range(10):
        pet = Pet(name = fake.first_name(), species = rc(species)) 
        pets.append(pet)
    pets.append(Pet(name = "Fido", species = "Dog"))
    pets.append(Pet(name = "Whiskers", species = "Cat"))
    pets.append(Pet(name = "Hermie", species = "Hamster"))
    pets.append(Pet(name = "Slither", species = "Snake"))

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()