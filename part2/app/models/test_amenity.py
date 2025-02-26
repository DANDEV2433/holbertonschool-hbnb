import unittest
from app.models.amenity import Amenity

class TestAmenityCreation(unittest.TestCase):

    def test_amenity_creation(self):
        amenity = Amenity(name="Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")  # Utilisation de assertEqual pour une assertion correcte
        print("Amenity creation test passed!")

if __name__ == "__main__":
    unittest.main()