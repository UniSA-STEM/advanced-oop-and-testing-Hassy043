"""
File: animals.py
Description: Defines animal domain classes and health records for the Zoo Management System.
Author: Seyedvahid Hashemian
ID: 110426111
Username: HASSY043
This is my own work as defined by the University's Academic Integrity Policy.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


class ValidationError(ValueError):
    """Raised when invalid data is supplied to domain objects."""


@dataclass
class HealthRecord:
    description: str
    date_reported: str  # ISO date string for simplicity
    severity: int  # 1 (low) - 5 (critical)
    treatment_plan: str = ""
    active: bool = True

    def __post_init__(self) -> None:
        if not (1 <= self.severity <= 5):
            raise ValidationError("Severity must be between 1 and 5.")
        if not self.description.strip():
            raise ValidationError("Health description cannot be empty.")


@dataclass
class Animal(ABC):
    name: str
    species: str
    age: int
    diet: str
    category: str  # 'mammal', 'bird', 'reptile', etc.
    health_records: List[HealthRecord] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.age < 0:
            raise ValidationError("Age must be non-negative.")
        if self.category not in {"mammal", "bird", "reptile"}:
            raise ValidationError("Category must be one of: mammal, bird, reptile.")

    def add_health_issue(self, record: HealthRecord) -> None:
        self.health_records.append(record)

    def resolve_health_issue(self, index: int) -> None:
        if not (0 <= index < len(self.health_records)):
            raise ValidationError("Invalid health record index.")
        self.health_records[index].active = False

    @property
    def under_treatment(self) -> bool:
        return any(r.active for r in self.health_records)

    @abstractmethod
    def make_sound(self) -> str: ...

    def eat(self) -> str:
        return f"{self.name} the {self.species} eats {self.diet}."

    def sleep(self) -> str:
        return f"{self.name} the {self.species} is sleeping."


@dataclass
class Mammal(Animal):
    fur_type: str = "varied"

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.category != "mammal":
            raise ValidationError("Mammal must have category 'mammal'.")

    def make_sound(self) -> str:
        return f"{self.name} (mammal) makes a growl or call."


@dataclass
class Bird(Animal):
    can_fly: bool = True

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.category != "bird":
            raise ValidationError("Bird must have category 'bird'.")

    def make_sound(self) -> str:
        return f"{self.name} (bird) chirps or squawks."


@dataclass
class Reptile(Animal):
    is_venomous: bool = False

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.category != "reptile":
            raise ValidationError("Reptile must have category 'reptile'.")

    def make_sound(self) -> str:
        return f"{self.name} (reptile) hisses."
