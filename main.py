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
    def get_role(self) -> str:
        pass

    def __str__(self):
        return f"{self._name} ({self.get_role()})"


# -------------------------------
# 2. INHERITANCE
# -------------------------------
class Staff(Person):
    """Base class for hospital staff."""

    def __init__(self, name: str, age: int, staff_id: str):
        super().__init__(name, age)
        self._staff_id = staff_id

    @abstractmethod
    def perform_duty(self) -> str:
        pass


class Doctor(Staff):
    """Doctor who diagnoses patients."""

    def get_role(self):
        return "Doctor"

    def perform_duty(self):
        return f"👨‍⚕️ Dr. {self._name} is diagnosing patients."


class Nurse(Staff):
    """Nurse who assists doctors and cares for patients."""

    def get_role(self):
        return "Nurse"

    def perform_duty(self):
        return f"👩‍⚕️ Nurse {self._name} is caring for patients."

# -------------------------------
# 3. ENCAPSULATION
# -------------------------------
class Patient(Person):
    """Patient who receives care in the hospital."""
    def __init__(self, name:str, age:int, patient_id:str):
        super().__init__(name, age)
        self.__patient_id = patient_id
        self.__medical_history = []

    def get_role(self):
        return "Patient"

    def add_record(self, record: str):
        """Add a medical record to the patient's history."""
        self.__medical_history.append(record)
        return f"Record added for {self._name}:{record}"

    def view_records(self):
        return self.__medical_history
    

# -------------------------------
# 4. POLYMORPHISM
# -------------------------------
def hospital_round(staff_list):
    """Polymorphism: Each staff performs their duty differently."""
    for staff in staff_list:
        print(staff.perform_duty())

    
