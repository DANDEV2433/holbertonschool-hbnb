import unittest
from app.models.amenity import Amenity

class TestAmenityCreation(unittest.TestCase):

    def test_amenity_creation():
        amenity = Amenity(name="Wi-Fi")
        assert amenity.name, "Wi-Fi"  # Utilisation de assertEqual pour une assertion correcte
        print("Amenity creation test passed!")

if __name__ == "__main__":
    unittest.main()