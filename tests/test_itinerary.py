import unittest
from app.itinerary_generator import generate_itinerary

class TestItineraryGenerator(unittest.TestCase):
    def test_generate_itinerary(self):
        user_details = {
            "destination": "Paris",
            "days": 5,
            "budget": "moderate",
            "interests": "history and art"
        }
        itinerary = generate_itinerary(user_details)
        self.assertIn("Day 1", itinerary)
        self.assertIn("Paris", itinerary)

if __name__ == "__main__":
    unittest.main()
