import unittest
from main import  Doctor, Nurse, Patient

class TestHospitalManagementSystem(unittest.TestCase):
    def setUp(self):
        """Set up test cases with sample data."""
        self.doctor = Doctor("Alice Smith", 40, "D67890")
        self.nurse = Nurse("Bob Johnson", 35, "N54321")
        self.patient = Patient("Charlie Brown", 30, "P12345")	

    def test_doctor_role(self):
        self.assertEqual(self.doctor.get_role(), "Doctor")
        self.assertEqual(str(self.doctor), "Alice Smith (Doctor)")
        self.assertEqual(self.doctor.perform_duty(), "👨‍⚕️ Dr. Alice Smith is diagnosing patients.")

    def test_nurse_role(self):
        self.assertEqual(self.nurse.get_role(), "Nurse")
        self.assertEqual(str(self.nurse), "Bob Johnson (Nurse)")
        self.assertEqual(self.nurse.perform_duty(), "👩‍⚕️ Nurse Bob Johnson is caring for patients.")

    def test_patient_role(self):
        self.assertEqual(self.patient.get_role(), "Patient")
        self.assertEqual(str(self.patient), "Charlie Brown (Patient)")
        self.assertEqual(self.patient.add_record("Flu"), "Record added for Charlie Brown:Flu") 
        self.assertIn("Flu", self.patient.view_records())


        
if __name__ == "__main__":
    unittest.main()