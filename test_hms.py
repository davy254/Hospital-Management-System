import unittest
from main import  Doctor, Nurse

class TestHospitalManagementSystem(unittest.TestCase):
    def setUp(self):
        """Set up test cases with sample data."""
        self.doctor = Doctor("Alice Smith", 40, "D67890")
        self.nurse = Nurse("Bob Johnson", 35, "N54321")

    def test_doctor_role(self):
        self.assertEqual(self.doctor.get_role(), "Doctor")
        self.assertEqual(str(self.doctor), "Alice Smith (Doctor)")
        self.assertEqual(self.doctor.perform_duty(), "👨‍⚕️ Dr. Alice Smith is diagnosing patients.")

    def test_nurse_role(self):
        self.assertEqual(self.nurse.get_role(), "Nurse")
        self.assertEqual(str(self.nurse), "Bob Johnson (Nurse)")
        self.assertEqual(self.nurse.perform_duty(), "👩‍⚕️ Nurse Bob Johnson is caring for patients.")


if __name__ == "__main__":
    unittest.main()