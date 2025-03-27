from models.ai_model import get_model_response
from app.prompts import ITINERARY_PROMPT_TEMPLATE

def generate_itinerary(user_details):
    # Fill the itinerary prompt template with user details
    prompt = ITINERARY_PROMPT_TEMPLATE.format(**user_details)
    # Get itinerary response from the AI model
    itinerary = get_model_response(prompt)
    return itinerary
