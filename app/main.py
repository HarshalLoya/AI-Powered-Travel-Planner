from app.itinerary_generator import generate_itinerary
from app.prompts import SYSTEM_PROMPT, USER_PROMPT
from app.utils import extract_user_details

def main():
    # Example user input
    user_input = "I want to travel from New York to Paris for 5 days on a moderate budget with interests in history and art."
    
    # Extract details from the user input
    user_details = extract_user_details(user_input)
    print("Extracted User Details:", user_details)
    
    # Generate itinerary based on the extracted details
    itinerary = generate_itinerary(user_details)
    print("\nGenerated Itinerary:\n", itinerary)

if __name__ == "__main__":
    main()
