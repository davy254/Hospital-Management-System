from abc import ABC, abstractmethod
from datetime import datetime


# -------------------------------
# 1. ABSTRACTION
# -------------------------------
class Person(ABC):
    """Abstract base class for people in the hospital."""

    def __init__(self, name: str, age: int):
        self._name = name  # Encapsulation
        self._age = age

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self._name} ({self.get_role()})"