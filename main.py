'''
File: main.py
Description: Demo script that builds a sample zoo, runs a daily routine and prints reports.
Author: Seyedvahid Hashemian
ID: 110426111
Username: HASSY043
This is my own work as defined by the University's Academic Integrity Policy.
'''


from animals import Mammal, Bird, Reptile, HealthRecord
from enclosures import Enclosure
from staff import Zookeeper, Veterinarian
from zoo import Zoo


def demo() -> None:
    zoo = Zoo("Simone's Zoo")

    # Animals
    leo = Mammal(name="Leo", species="Lion", age=6, diet="meat", category="mammal", fur_type="short")
    polly = Bird(name="Polly", species="Parrot", age=2, diet="seeds", category="bird", can_fly=True)
    snek = Reptile(name="Snek", species="Python", age=4, diet="rodents", category="reptile", is_venomous=False)

    for a in (leo, polly, snek):
        zoo.add_animal(a)

    # Enclosures
    savannah = Enclosure(name="Savannah Plains", environment="savannah", size_sq_m=1200, allowed_category="mammal", cleanliness=85)
    aviary = Enclosure(name="Big Aviary", environment="aviary", size_sq_m=300, allowed_category="bird", cleanliness=90)
    reptarium = Enclosure(name="Reptarium", environment="desert", size_sq_m=250, allowed_category="reptile", cleanliness=75)

    for e in (savannah, aviary, reptarium):
        zoo.add_enclosure(e)

    # Staff
    zk = Zookeeper(name="Sam", role="zookeeper")
    vet = Veterinarian(name="Vera", role="veterinarian")

    zoo.add_staff(zk)
    zoo.add_staff(vet)

    # Assignments
    zk.assign_enclosure(savannah)
    zk.assign_enclosure(aviary)
    zk.assign_enclosure(reptarium)

    # Health event prevents movement/display
    vet.health_check(leo, description="Minor paw injury", severity=2, treatment="Rest 3 days")
    try:
        zoo.assign_animal_to_enclosure(leo, savannah)
    except Exception as e:
        print(f"Could not move Leo yet: {e}")

    # Resolve and move
    vet.resolve_issue(leo, 0)
    zoo.assign_animal_to_enclosure(leo, savannah)
    zoo.assign_animal_to_enclosure(polly, aviary)
    zoo.assign_animal_to_enclosure(snek, reptarium)

    # Demo polymorphic behavior
    for a in (leo, polly, snek):
        print(a.make_sound())
        print(a.eat())
        print(a.sleep())

    # Daily routine
    for t in zoo.daily_routine():
        print(t)

    # Reports
    print("Animals by species:", zoo.animals_by_species())
    for line in zoo.enclosure_status_report():
        print(line)
    for line in zoo.health_report():
        print(line)


if __name__ == "__main__":
    demo()
