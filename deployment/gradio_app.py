import gradio as gr
from app.itinerary_generator import generate_itinerary
from app.utils import extract_user_details

def travel_planner_interface(user_input):
    # Extract details from the user's input
    user_details = extract_user_details(user_input)
    # Generate itinerary based on the details
    itinerary = generate_itinerary(user_details)
    return itinerary

iface = gr.Interface(
    fn=travel_planner_interface,
    inputs=gr.Textbox(lines=2, placeholder="Enter your travel details here..."),
    outputs="text",
    title="AI-Powered Travel Planner",
    description="Enter your travel details to get a personalized itinerary."
)

if __name__ == "__main__":
    iface.launch()
