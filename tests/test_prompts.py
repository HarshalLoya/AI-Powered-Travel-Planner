import unittest
from app.prompts import ITINERARY_PROMPT_TEMPLATE

class TestPrompts(unittest.TestCase):
    def test_itinerary_prompt_template(self):
        user_details = {
            "destination": "Paris",
            "days": 5,
            "budget": "moderate",
            "interests": "history and art"
        }
        prompt = ITINERARY_PROMPT_TEMPLATE.format(**user_details)
        self.assertIn("Paris", prompt)
        self.assertIn("5 days", prompt)

if __name__ == "__main__":
    unittest.main()
