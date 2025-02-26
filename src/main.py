# src/main.py
import os
import openai
from dotenv import load_dotenv
from image_analysis import analyze_image
from claims_analysis import analyze_claim, get_image_filename

load_dotenv()  # Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_legitimacy_rating(anomaly_rating, image_rating):
    # Prepare the prompt for the OpenAI API
    prompt = f"Based on the following claim analysis: '{anomaly_rating}' and image analysis: '{image_rating}', provide a legitimacy rating from 0 to 5, where 0 is completely illegitimate and 5 is completely legitimate."

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract the legitimacy rating from the response
    legitimacy_rating = response['choices'][0]['message']['content']
    return legitimacy_rating

def main():
    # User inputs claim ID
    claim_id = int(input("Enter the Claim ID: "))

    # Analyze claim
    anomaly_rating = analyze_claim(claim_id)

    # Get image filename
    image_filename = get_image_filename(claim_id)
    image_path = os.path.join('..', 'claims', 'images', image_filename)  # Adjusted path

    # Print the image path for debugging
    print(f"Looking for image at: {image_path}")

    # Analyze image if it exists
    if os.path.exists(image_path):
        image_rating = analyze_image(image_path)
    else:
        image_rating = "Image not found."

    # Get legitimacy rating from OpenAI
    legitimacy_rating = get_legitimacy_rating(anomaly_rating, image_rating)

    # Output results
    print(f"Claim Information: {anomaly_rating}")
    print(f"Image Manipulation Status: {image_rating}")
    print(f"Claim Legitimacy Rating: {legitimacy_rating}")  # Updated output

    # Continue conversation with AI agent
    while True:
        user_input = input("Ask the AI agent a question (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()