"""
File: enclosures.py
Description: Implements the Enclosure class for housing animals with environment and capacity rules.
Author: Seyedvahid Hashemian
ID: 110426111
Username: HASSY043
This is my own work as defined by the University's Academic Integrity Policy.
"""


from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Literal

from animals import Animal, ValidationError

Environment = Literal["aquatic", "savannah", "aviary", "desert", "rainforest", "temperate"]


@dataclass
class Enclosure:
    name: str
    environment: Environment
    size_sq_m: float
    allowed_category: str  # 'mammal' | 'bird' | 'reptile'
    cleanliness: int = 100  # 0-100
    animals: List[Animal] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.size_sq_m <= 0:
            raise ValidationError("Enclosure size must be positive.")
        if self.allowed_category not in {"mammal", "bird", "reptile"}:
            raise ValidationError("allowed_category must be 'mammal', 'bird', or 'reptile'.")
        if not (0 <= self.cleanliness <= 100):
            raise ValidationError("Cleanliness must be between 0 and 100.")

    def can_accept(self, animal: Animal) -> bool:
        if animal.category != self.allowed_category:
            return False
        if animal.under_treatment:
            return False
        return True

    def add_animal(self, animal: Animal) -> None:
        if not self.can_accept(animal):
            raise ValidationError(f"Cannot add {animal.name}: incompatible or under treatment.")
        self.animals.append(animal)
        # A bit of dirt gets added with new arrival
        self.cleanliness = max(0, self.cleanliness - 5)

    def remove_animal(self, animal: Animal) -> None:
        self.animals.remove(animal)

    def clean(self) -> None:
        self.cleanliness = 100

    def status(self) -> str:
        names = ", ".join(a.name for a in self.animals) or "No animals"
        return (f"Enclosure '{self.name}': {self.environment}, {self.size_sq_m} m^2, "
                f"cleanliness {self.cleanliness}/100, animals: {names}")
