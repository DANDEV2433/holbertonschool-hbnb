import unittest
from app.models.user import User

class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password")
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.email == "john.doe@example.com"
        assert user.is_admin is False  # Default value
        print("User creation test passed!")

if __name__ == "__main__":
    unittest.main()
