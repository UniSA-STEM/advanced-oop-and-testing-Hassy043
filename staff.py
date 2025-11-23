'''
File: staff.py
Description: Defines Staff, Zookeeper and Veterinarian classes and their responsibilities in the zoo.
Author: Seyedvahid Hashemian
ID: 110426111
Username: HASSY043
This is my own work as defined by the University's Academic Integrity Policy.
'''


from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from animals import Animal, ValidationError, HealthRecord
from enclosures import Enclosure


@dataclass
class Staff:
    name: str
    role: str

    def __post_init__(self) -> None:
        if self.role not in {"zookeeper", "veterinarian"}:
            raise ValidationError("Role must be 'zookeeper' or 'veterinarian'.")


@dataclass
class Zookeeper(Staff):
    assigned_enclosures: List[Enclosure] = field(default_factory=list)

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.role != "zookeeper":
            raise ValidationError("Zookeeper must have role 'zookeeper'.")

    def assign_enclosure(self, enclosure: Enclosure) -> None:
        if enclosure not in self.assigned_enclosures:
            self.assigned_enclosures.append(enclosure)

    def feed(self, animal: Animal) -> str:
        return f"{self.name} feeds {animal.name}. {animal.eat()}"

    def clean_enclosure(self, enclosure: Enclosure) -> str:
        if enclosure not in self.assigned_enclosures:
            raise ValidationError("Zookeeper not assigned to this enclosure.")
        enclosure.clean()
        return f"{self.name} cleaned enclosure '{enclosure.name}'."


@dataclass
class Veterinarian(Staff):
    assigned_animals: List[Animal] = field(default_factory=list)

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.role != "veterinarian":
            raise ValidationError("Veterinarian must have role 'veterinarian'.")

    def assign_animal(self, animal: Animal) -> None:
        if animal not in self.assigned_animals:
            self.assigned_animals.append(animal)

    def health_check(self, animal: Animal, description: str, severity: int, treatment: str = "") -> HealthRecord:
        record = HealthRecord(description=description, date_reported="2025-10-26", severity=severity, treatment_plan=treatment)
        animal.add_health_issue(record)
        return record

    def resolve_issue(self, animal: Animal, index: int) -> None:
        animal.resolve_health_issue(index)
