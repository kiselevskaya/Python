**Pet shop simulation**


**factory.py**
    
    Class PetFactory contains all necesary information about each species.
    

**animals.py**

    Super class Animal contains information about animals (species, gender, name, age, etc.).
    Simulate aging, growth, death.
    Each class for species creates this species animal (wolf, lizard, parrot, raven or some new).


**names.py**

    Creates and returns male or female or random gender name from text files for male and female names.


**main.py**

    Creates shop with first few animals.
    Simulates changes after some time.
    Return new table with all animals and their characteristic at that time and logs with changes like death, newborn.

**pet_shop.py**

    Contains a list of animals in the shop with all information and a log of events.
    Keeps track of aging, growth, death, incidents (one animal swallowed another), reproduction.
    Return all information on the screen.

**shop_assistant.py**

    A new animal with all characteristics can be input and added to the shop manually.

