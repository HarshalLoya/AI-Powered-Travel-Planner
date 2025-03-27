# System and user prompts
SYSTEM_PROMPT = "You are a helpful travel planner assistant."
USER_PROMPT = "Please provide your travel details including budget, dates, destination, and preferences."

# Template for generating an itinerary.
# Expected keys: destination, days, budget, interests.
ITINERARY_PROMPT_TEMPLATE = (
    "Generate a day-by-day travel itinerary for a trip to {destination} lasting {days} days. "
    "The traveler has a {budget} budget and is interested in {interests}. "
    "Include suggestions for sightseeing, dining, and relaxation."
)
